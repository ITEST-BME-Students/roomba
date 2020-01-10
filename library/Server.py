import logging
import os
import socket
import sys
import threading
import time
import json
from library import Misc
from library import MyRoomba
from library import Logger
from library import Sensors

sys.path.insert(0,'/home/pi/grove.py/grove')
import adc_8chan_12bit

import os

def default_function(*args):
    return args


class Server:
    def __init__(self):
        self.logger = Logger.Logger('Server')
        # some defaults
        self.break_character = '*'

        host = socket.gethostname()
        self.buffer = 1024
        self.host = host
        self.log = []
        self.sockets = []
        self.print_log('Starting server at ' + host)
        self.print_log('Server working directory: ' + os.getcwd())

        # Connect to robot
        #self.roomba = MyRoomba.MyRoomba()

        # connect to adc
        self.adc = adc_8chan_12bit.Pi_hat_adc()
        # connect to sonar sensor
        self.sonar = Sensors.SonarSensors()
        #self.thermal = Sensors.ThermalCamera()

        # Bind functions
        self.open_connection(12345, self.shutdown)
        self.open_connection(10000, bind_function=self.test_communiction)
        self.open_connection(10001, bind_function=self.toggle_server_logging)

        self.open_connection(10010, bind_function=self.process_roomba_command)
        self.open_connection(10011, bind_function=self.get_adc)
        self.open_connection(10012, bind_function=self.get_external_sensor)
        self.logger.info('Function binding completed')

    ########################################
    # ROBOT FUNCTIONS
    ########################################
    def test_communiction(self, args):
        if not type(args) == list: args = [args]
        print('Test Communication Function Arguments', args)
        return 'success'

    # There is only function to handle input to the robot (and we're listening only on a single port)
    # The reason for this is that the serial port to the robot can only accept 1 command at a time any way
    def process_roomba_command(self, args):
        if not type(args) == list: args = [args]
        command = Misc.lst2command(args, end_character=False)
        result = self.roomba.handle_roomba_text_command(command)
        return result

    ########################################
    # ADC FUNCTIONS
    ########################################
    def get_adc(self, args):
        if not type(args) == list: args = [args]
        #unit = 0.1 percent!!
        result = self.adc.get_all_ratio_0_1_data()
        result = json.dumps(result)
        return result

    ########################################
    # Non ADC SENSOR FUNCTIONS
    ########################################
    def get_external_sensor(self, args):
        if not type(args) == list: args = [args]
        sensor = args[1]
        if sensor == 'sonar1': data = self.sonar.get_data()
        if sensor == 'thermal': data = self.thermal.get_data()
        print(data)
        result = json.dumps(data)
        return result
    ########################################
    # SERVER COMM FUNCTIONS
    ########################################
    def toggle_server_logging(self, args):
        if not type(args) == list: args = [args]
        state = args[0] == 'True'
        set_state = not state
        self.logger.logger.disabled = set_state

    ########################################
    # SERVER FUNCTIONS
    ########################################

    def print_log(self, text, level='i'):
        text = Misc.lst2str(text)
        if level == 'i': self.logger.info(text)
        if level == 'w': self.logger.warning(text)
        if level == 'c': self.logger.critical(text)

    def open_socket(self, port_number):
        self.sockets.append(port_number)
        skt = socket.socket()
        skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        skt.bind(('', port_number))
        skt.listen(1)
        return skt

    def receive_data(self, connection):
        data = ''
        while 1:
            packet = connection.recv(self.buffer)
            packet = packet.decode()
            if not packet: break
            data += packet
            if data.endswith(self.break_character): break
        data = data.rstrip(self.break_character + '\n')
        return data

    def open_connection(self, port_number, bind_function=default_function):
        t = threading.Thread(target=self.open_single_connection, args=(port_number, bind_function))
        t.start()

    def close_connection(self, port_number):
        message = 'close' + self.break_character
        message = message.encode()
        self.print_log(['Closing', port_number])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', port_number)
        sock.connect(server_address)
        sock.sendall(message)
        sock.close()

    def shutdown(self):
        ports = self.sockets
        self.print_log(['Shutting down Ports'] + ports)
        if 12345 in ports: ports.remove(12345)
        for port_number in ports: self.close_connection(port_number)
        self.close_connection(12345)
        self.print_log(['Finished shutting down'])
        self.sockets = []

    def open_single_connection(self, port_number, bind_function=default_function):
        function_name = bind_function.__name__
        self.print_log(['Opening connection for', function_name, 'on port', port_number])
        skt = self.open_socket(port_number)
        while 1:
            self.print_log(['Listening for', function_name, 'on port', port_number])
            connection, address = skt.accept()
            start = time.time()
            arguments = self.receive_data(connection)
            arguments = arguments.split(',')
            if function_name == 'shutdown':
                self.shutdown()
                break
            if 'close' in arguments[0]: break
            results = bind_function(arguments)
            results = str(results)
            if not results.endswith(self.break_character): results += self.break_character
            results = str(results)
            results = results.encode()
            connection.sendall(results)
            connection.close()
            stop = time.time()
            delta = round((stop - start) * 1000)
            self.print_log(['Response time for', function_name, ':', delta, 'ms'])
        self.print_log(['Closing connection for', function_name, 'on port', port_number])
        message = 'closed ' + str(port_number) + self.break_character
        message = message.encode()
        if 'close' in arguments[0]: connection.sendall(message)
        connection.close()
        skt.close()
