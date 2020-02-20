from setuptools import setup

setup(
    name='PD2030',
    version='0.3',
    packages=['PD2030', 'PD2030.roomba', 'PD2030.maestro'],
    url='https://github.com/BME-ITEST-Students/roomba',
    license='',
    author='dieter',
    author_email='',
    description='',
    install_requires=['paramiko', 'easygui', 'natsort', 'pyserial', 'numpy'],
)
