import socket
import paramiko
import logging
import threading
import sys
import os
import errno
import time
import easygui
import json
import natsort
import numpy
from library import Logger
from library import Misc
from library import Kinematics

def read_filelist():
    current_dir = os.path.dirname(__file__)
    list_file = os.path.join(current_dir, 'filelist.txt')
    f = open(list_file, 'r')
    files = f.readlines()
    f.close()
    while '\n' in files: files.remove('\n')
    new = []
    for x in files: new.append(x.rstrip('\n'))
    return new

def get_bumper_data(sensor_data, binary=False):
    a = sensor_data['light_bumper_left']
    b = sensor_data['light_bumper_front_left']
    c = sensor_data['light_bumper_center_left']
    d = sensor_data['light_bumper_center_right']
    e = sensor_data['light_bumper_front_right']
    f = sensor_data['light_bumper_right']
    analog_data = numpy.array([a, b, c, d, e, f])
    binary_data = numpy.array(sensor_data['light_bumper'])
    if binary: return binary_data
    if not binary: return analog_data



class Client:
    def __init__(self, do_upload=True, run_locally=False):
        self.logger = Logger.Logger('Client')
        self.run_locally = run_locally
        self.logging = False
        self.logfile = None
        self.__stop_loop = False

        if not self.run_locally:
            self.remote = '192.168.0.249'
            self.remote_python = 'python3'
            self.remote_dir = '/home/pi/Desktop/server/'
            self.remote_script = 'start_server.py'
            self.local_dir = os.getcwd()
            self.user = 'pi'
            self.password = 'raspberry'

        if self.run_locally:
            self.remote = 'localhost'
            self.remote_python = '/home/dieter/anaconda3/envs/roomba/bin/python'
            self.remote_dir = '/home/dieter/Desktop/server/'
            self.remote_script = 'start_server.py'
            self.local_dir = os.getcwd()
            self.user = 'dieter'
            self.password = None

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
        self.sftp = paramiko.SFTPClient.from_transport(transport)

        # Do Upload
        if do_upload: self.upload_files(verbose=True)

    def stop_logging(self):
        self.file_logger.close()

    def print_log(self, text, level='i'):
        text = Misc.lst2str(text)
        text = Misc.lst2str(text)
        if level == 'i': self.logger.info(text)
        if level == 'w': self.logger.warning(text)
        if level == 'c': self.logger.critical(text)

    def __del__(self):
        self.ssh.close()
        self.sftp.close()

    ##################################
    # SERVER CONTROL FUNCTIONS
    ##################################
    def test_communication(self, message=[]):
        arguments = ['Test communication', 1, 2, 3] + message
        command = Misc.lst2command(arguments)
        reply = self.send_command(command, 10000)
        self.print_log([reply])

    def toggle_logging(self, state=True):
        #This disables/enables the logging for both the server and the client
        self.logger.logger.disabled = not state
        reply = self.send_command(str(state), 10001)
        self.print_log([reply])

    ##################################
    # ROBOT CONTROL FUNCTIONS
    ##################################

    def send_raw_command(self, command):
        reply = self.send_command(command, 10010)
        return reply

    ##################################
    # ADC FUNCTIONS
    ##################################

    def get_adc(self):
        reply = self.send_command('get_adc', 10011)
        reply = json.loads(reply)
        converted = []
        for x in reply: converted.append(x*0.1) #to get percentage 0-100. Orginal data is in 0.1%
        return converted

    ##################################
    # BUILD RAW COMMANDS FOR THE ROOMBA
    ##################################
    def set_motors(self, left, right):
        command = ['MT', left, right]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def set_display(self, text):
        command = ['DP', text]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def get_roomba_sensors(self):
        result = self.send_raw_command('SD')
        result = json.loads(result)
        return result

    def move(self, distance):
        distance = int(distance)
        command = ['MD', distance]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    def turn(self, degrees):
        degrees = int(degrees)
        command = ['TD', degrees]
        command = Misc.lst2command(command, end_character=False)
        result = self.send_raw_command(command)
        return result

    ##################################
    # SUPPORT/SECONDARRY FUNCTIONS
    ##################################
    def formatted_sensor_data(self):
        text=''
        self.logger.logger.disabled = True
        data = self.get_roomba_sensors()
        self.logger.logger.disabled = False
        keys = data.keys()
        keys = natsort.natsorted(keys)
        for x in keys:
            item = x.ljust(30, '.')
            value = str(data[x])
            text+=item+value+'\n'
        return text

    def get_bumper_data(self, binary=False):
        sensor_data = self.get_roomba_sensors()
        bumper_data = get_bumper_data(sensor_data, binary)
        return bumper_data

    def set_velocity(self, linear, angular):
        # linear: mm/s
        # angular: degrees/sec
        result = Kinematics.kinematics(linear, angular)
        left_wheel_speed = result[0]
        right_wheel_speed = result[1]
        self.set_motors(left_wheel_speed, right_wheel_speed)

    ##################################
    # SERVER CONTROL FUNCTIONS
    ##################################

    def send_command(self, command, port, answer=True):
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
        a = self.send_command('close', 12345, answer=True)
        self.print_log([a])
        self.__stop_loop = True

    def start_remote_server(self):
        if not self.run_locally: self.stop_remote_python()
        t = threading.Thread(target=self.remote_server_process)
        t.start()
        time.sleep(5)

    def stop_remote_python(self):
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
        command = self.remote_python + ' ' + self.remote_dir + self.remote_script
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
        if not self.run_locally: self.stop_remote_python()
        self.ssh.close()

    ##################################
    # SFTP FUNCTIONS
    ##################################

    def remote_folder_exists(self, folder):
        try:
            self.sftp.stat(folder)
        except IOError as e:
            if e.errno == errno.ENOENT: return False
            raise
        else:
            return True

    def delete_remote_folder(self, folder):
        files = self.sftp.listdir(folder)
        for file_name in files:
            file_path = os.path.join(folder, file_name)
            try:
                self.sftp.remove(file_path)
            except IOError:
                self.delete_remote_folder(file_path)
        self.sftp.rmdir(folder)

    def upload_files(self, verbose=False):
        if verbose: print('Uploading files')
        if self.remote_folder_exists(self.remote_dir): self.delete_remote_folder(self.remote_dir)
        if not self.remote_folder_exists(self.remote_dir): self.sftp.mkdir(self.remote_dir)
        files = read_filelist()
        for local_file in files:
            parts = os.path.split(local_file)
            remote_file = os.path.join(self.remote_dir, parts[0], parts[1])
            remote_dir = os.path.join(self.remote_dir, parts[0])
            if not self.remote_folder_exists(remote_dir): self.sftp.mkdir(remote_dir)
            self.sftp.put(local_file, remote_file)
            if verbose: print(local_file, '---->', remote_file)
