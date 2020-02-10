import glob
import sys

import serial


def match_variables(data, variables):
    names = list(data.columns)
    if not isinstance(variables , (list, tuple)): variables = [variables]
    variables_lower = list2lower(variables)
    names_lower = list2lower(names)
    matched_variables = []
    failed_variables = []
    for lower, original in zip(variables_lower, variables):
        try:
            index = names_lower.index(lower)
            matched = names[index]
            matched_variables.append(matched)
        except:
            failed_variables.append(original)
    return matched_variables, failed_variables


def list2lower(lst):
    result = [x.lower() for x in lst]
    return result

def name_range(base, n):
    names = []
    for x in range(0, n): names.append(base + str(x))
    return names


def serial_ports(try_ports=False):
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    if not try_ports: return ports
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def normalize(value, min_value, max_value):
    delta = max_value - min_value
    new = value - min_value
    new = new / delta
    if new < 0: new = 0
    if new > 1: new = 1
    return new
