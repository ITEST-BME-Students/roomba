import socket
import paramiko
import threading
import sys
import os
import errno
import time
import easygui
import json
import natsort
import numpy
from matplotlib import pyplot
from . import Logger
from . import Misc
from . import Kinematics
from . import SFTPClient


def get_bumper_data(sensor_data, binary=False):
    """
    Helper function to extract the bumper data. Should not be called directly.

    For student use: No

    :param sensor_data: raw sensor data
    :param binary: boolean
    :return: list of bumpter values
    """
    max_sensor_reading = 4905
    numpy.interp

    a = sensor_data['light_bumper_left']
    b = sensor_data['light_bumper_front_left']
    c = sensor_data['light_bumper_center_left']
    d = sensor_data['light_bumper_center_right']
    e = sensor_data['light_bumper_front_right']
    f = sensor_data['light_bumper_right']
    analog_data = numpy.array([a, b, c, d, e, f])
    analog_data = analog_data / max_sensor_reading
    analog_data[analog_data > 1] = 1
    analog_data[analog_data < 0] = 0
    # invert to make these into 'distance readings'
    analog_data = 1 - analog_data
    # map onto a much smaller range, as the sensors don't seem to use the whole range
    analog_data = numpy.interp(analog_data, [0, 0.85, 1], [0, 0, 1])
    binary_data = numpy.array(sensor_data['light_bumper'])
    if binary: return binary_data
    if not binary: return analog_data


class Client:
    """
    This class is used to communicate with the robot.

    For student use: Yes

    :param ip: The IP address of the raspberry pi controlling the roomba robot.
    :param do_upload: Boolean, indicating whether code should be uploaded to the raspberry pi.
    """

    def __init__(self, name=False, do_upload=True):
        self.logger = Logger.Logger('Client')
        self.logging = False
        self.logfile = None
        self.__stop_loop = False

        self.remote = Misc.get_ip_by_name(name)
        self.remote_python = 'python3'
        self.remote_dir = Misc.convert_path('/home/pi/Desktop/PD2030')
        self.remote_script = 'start_server.py'
        self.local_dir = os.getcwd()
        self.user = 'pi'
        self.password = 'raspberry'

        if self.password is None: self.password = easygui.passwordbox('password for the remote computer')

        # Open Ssh
        # self.start_logging()
        self.print_log('Starting Client')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.remote, username=self.user, password=self.password, timeout=3)
        # Open FTP
        transport = paramiko.Transport((self.remote, 22))
        transport.default_window_size = 10 * 1024 * 1024
        transport.connect(username=self.user, password=self.password)
        self.sftp = SFTPClient.SFTPClient.from_transport(transport)

        # Do Upload
        if do_upload: self.upload_files(verbose=True)

    def print_log(self, text, level='i'):
        """
        Function that handles writing text to the log.

        For student use: No

        :param text: Log message as string.
        :param level: The level of importance of the message: (i)nfo, (w), or (c)ricical
        """
        text = Misc.lst2str(text)
        text = Misc.lst2str(text)
        if level == 'i': self.logger.info(text)
        if level == 'w': self.logger.warning(text)
        if level == 'c': self.logger.critical(text)

    def __del__(self):
        """
        Destructor for the class.

        For student use: No

        """
        self.ssh.close()
        self.sftp.close()

    ##################################
    # SERVER CONTROL FUNCTIONS
    ##################################
    def test_communication(self, message=[]):
        """
        Function to test the communication between the host computer and the raspberry. Sends a test string to the raspberry and prints a returned message.

        For student use: No

        :param message: A list of message parts to be sent.
        :return: None, the function prints output to the console.
        """
        arguments = ['Test communication', 1, 2, 3] + message
        command = Misc.lst2command(arguments)
        reply = self.send_command(command, 10000)
        self.print_log([reply])

    def toggle_logging(self, state=True):
        """
        This functions can be used to toggle whether logging messages are generated and written to the console.

        For student use: No

        :param state:  Boolean
        :return: None
        """
        # This disables/enables the logging for both the server and the client
        self.logger.logger.disabled = not state
        reply = self.send_command(str(state), 10001)
        self.print_log([reply])

    ##################################
    # ROBOT CONTROL FUNCTIONS
    ##################################

    def send_raw_command(self, command):
        """
        Sends a raw string to the server. The server will process this string as a command for the robot.

        For student use: No

        :param command: A string
        :return: None
        """
        reply = self.send_command(command, 10010)
        return reply

    ##################################
    # ADC FUNCTIONS
    ##################################
    def get_adc(self):
        """
        Get all the analog values from the seeed ADC shield, as percentages in the range 0-100

        For student use: Yes

        :return: A list of values.
        """
        reply = self.send_command('get_adc', 10011)
        reply = json.loads(reply)
        converted = []
        for x in reply: converted.append(x * 0.1)  # to get percentage 0-100. Orginal data is in 0.1%
        return converted

    ##################################
    # External non ADC sensors
    ##################################
    def get_external_sensor(self, sensor):
        """
        Generic function to get sensor readings from sensors that are not attached to the Seeed shield and are not roomba sensors.

        For student use: No

        :param sensor: A string specifying which sensor to read.
        :return: Sensor data
        """
        command = Misc.lst2command(['get_sensor', sensor])
        reply = self.send_command(command, 10012)
        reply = json.loads(reply)
        return reply

    ##################################
    # BUILD RAW COMMANDS FOR THE ROOMBA
    ##################################
    def set_motors(self, left, right):
        """
        A low level function to set the speed of the motors of the roomba.

        For student use: Yes

        :param left: Left speed as an integer in the range -500,500 mm/s
        :param right: Right speed as an integer in the range -500,500 mm/s
        :return: A return message from the robot.
        """
        command = ['MT', left, right]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def set_display(self, text):
        """
        Sets the display screen of the root to a specified text value.

        For student use: Yes

        :param text: The message to be shown. Only the first 4 characters can be displayed.
        :return: A return message from the robot.
        """
        command = ['DP', text]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def get_roomba_sensors(self):
        """
        Gets the values of all roomba sensors.

        For student use: Yes

        :return: A dictionary of sensors values
        """
        result = self.send_raw_command('SD')
        result = json.loads(result)
        return result

    def move(self, distance):
        """
        Moves the robot foward by a given distance.

        For student use: Yes

        :param distance: distance in mm
        :return: A return message from the robot.
        """
        distance = int(distance)
        command = ['MD', distance]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def turn(self, degrees):
        """
        Turns the robot a number of degrees.

        For student use: Yes

        :param degrees: turn angle in degrees.
        :return: A return message from the robot.
        """
        degrees = int(degrees)
        command = ['TD', degrees]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    ##################################
    # SUPPORT/SECONDARRY FUNCTIONS
    ##################################
    def formatted_sensor_data(self):
        """
        Reads out all roomba sensors and formats the results into a text that can be printed to the console.

        For student use: Yes

        :return: Formatted text containing all sensor values.
        """
        text = ''
        self.logger.logger.disabled = True
        data = self.get_roomba_sensors()
        self.logger.logger.disabled = False
        keys = data.keys()
        keys = natsort.natsorted(keys)
        for x in keys:
            item = x.ljust(30, '.')
            value = str(data[x])
            text += item + value + '\n'
        return text

    def get_bumper_data(self, binary=False):
        """
        Gets the roomba bumper data.

        For student use: Yes

        :param binary: Boolean, specifies whether the raw or the binary values should be returned.
        :return: A list of values.
        """
        sensor_data = self.get_roomba_sensors()
        bumper_data = get_bumper_data(sensor_data, binary)
        return bumper_data

    def set_velocity(self, linear, angular):
        """
        Sets the linear and angular velocity of the roomba.

        For student use: Yes

        :param linear: Linear speed in mm/s
        :param angular: Angular speed in degrees/s
        :return: None
        """
        # linear: mm/s, angular: degrees/sec
        result = Kinematics.kinematics(linear, angular)
        left_wheel_speed = result[0]
        right_wheel_speed = result[1]
        self.set_motors(left_wheel_speed, right_wheel_speed)

    def get_thermal_image(self, plot=False):
        """
        Gets the image from the thermal camera.

        For student use: Yes

        :param plot: boolean, should be the image be plotted?
        :return: A numpy array of temperature values (pixels).
        """
        data = self.get_external_sensor('thermal')
        data = numpy.array(data)
        data = data.reshape(24, 32)
        data = numpy.transpose(data)
        if plot:
            pyplot.matshow(data, cmap='hot')
            pyplot.colorbar()
            pyplot.show()
        return data

    ##################################
    # SERVER CONTROL FUNCTIONS
    ##################################
    def send_command(self, command, port, answer=True):
        """
        Low level function sending a string command to the remote server.

        For student use: No

        :param command: Command as a string.
        :param port: Port to use
        :param answer: Boolean specifying whether an answer should be read out.
        :return: The returned data, if any.
        """
        if not command.endswith('*'): command += '*'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.remote, port)
        sock.connect(server_address)
        sock.send(command.encode())
        data = ''
        if not answer: return data
        while 1:
            packet = sock.recv(1024)
            packet = packet.decode()
            data += packet
            if data.endswith('*'): break
        data = data.rstrip('*')
        return data

    def stop_remote_server(self):
        """
        Sends a command stopping the remote server on port 12345

        For student use: No

        :return: None
        """
        a = self.send_command('close', 12345, answer=True)
        self.print_log([a])
        self.__stop_loop = True

    def start_remote_server(self):
        """
        Starts the remote server as a Python thread.

        For student use: No

        :return: None
        """
        self.stop_remote_python()
        t = threading.Thread(target=self.remote_server_process)
        t.start()
        time.sleep(5)

    def stop_remote_python(self):
        """
        Stops all Python processes on the remote raspberry pi.

        For student use: No

        :return: The return value as generated by the raspberry pi.
        """
        stdin, stdout, stderr = self.ssh.exec_command('killall python')
        time.sleep(2.5)
        self.print_log(['Stopping Remote Python'])
        a = stdout.read()
        b = stderr.read()
        a = a.decode()
        b = b.decode()
        output = a + b
        output = output.replace('\n', '')
        self.print_log([output])

    def remote_server_process(self):
        """
        A function implementing the process of reading the output generated by the server and printing it to the local console.

        For student use: No

        :return: None.
        """
        path = os.path.join(self.remote_dir, self.remote_script)
        path = Misc.linux_path(path)
        command = self.remote_python + ' ' + path

        channel = self.ssh.get_transport()
        channel = channel.open_session()
        channel.get_pty()
        channel.exec_command(command)
        while True:
            if channel.recv_ready():
                data = channel.recv(10)
                data = data.decode()
                sys.stdout.write(data)
            else:
                # only break if there is no more data to be read from the remote session
                if self.__stop_loop: break
        self.__stop_loop = False
        self.stop_remote_python()
        self.ssh.close()

    ##################################
    # SFTP FUNCTIONS
    ##################################

    def remote_folder_exists(self, folder):
        """
        Function testing whether a folder exists on the raspberry.

        For student use: No

        :param folder: The folder to be tested.
        :return: Boolean
        """
        folder = Misc.convert_path(folder)
        try:
            self.sftp.stat(folder)
        except IOError as e:
            if e.errno == errno.ENOENT: return False
            raise
        else:
            return True

    def delete_remote_folder(self, folder):
        """
        Function to delete a remote folder.

        For student use: No

        :param folder: Folder to be deleted.
        :return: None
        """
        files = self.sftp.listdir(folder)
        for file_name in files:
            file_path = os.path.join(folder, file_name)
            file_path = Misc.convert_path(file_path)
            print(file_path, file_path)
            try:
                self.sftp.remove(file_path)
            except IOError:
                self.delete_remote_folder(file_path)
        self.sftp.rmdir(folder)

    def upload_files(self, verbose=False):
        """
        This function uploads all the files specified in filelist.txt to the raspberry pi.

        For student use: No

        :param verbose: Boolean
        :return: None
        """
        if verbose: print('Uploading files')
        if self.remote_folder_exists(self.remote_dir): self.delete_remote_folder(self.remote_dir)
        if not self.remote_folder_exists(self.remote_dir): self.sftp.mkdir(self.remote_dir)
        self.sftp.put_dir('PD2030', self.remote_dir)
