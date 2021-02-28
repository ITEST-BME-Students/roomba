#sudo chmod +x install_packages.sh
#./install_packages.sh

# Required python packages -->

pip3 install adafruit-circuitpython-mlx90640
pip3 install sounddevice
pip3 install matplotlib

# Installing Scipy and pandas -->
# do not used pip3. That does not seem to work

sudo apt install python3-scipy
sudo apt install python3-pandas

# Portaudio not found -->

sudo apt-get install libasound-dev
sudo apt-get install portaudio19-dev
sudo apt-get install python3-pyaudio

# libf77blas.so.3 not found: -->

sudo apt-get install libatlas-base-dev