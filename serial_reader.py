import serial

# Object used to establish a connection from the ground station to the Arduino on the rocket.
# Reads serial data from the Arduino then decodes it and puts it in the RocketData object.
#
# Authors: Ethan Visscher


class SerialReader:
    def __init__(self):
        self.ser = None
        self.reading_data = False
        self.camera_recording = False
        self.foo = 1
        self.msg = ''

    # Function used to grab serial data from Ardunio, decode it, and put all the data in the RocketData object
    #
    # args: RocketData object passed as reference so changes will happen to the RocketData object in main.py
    def get_data(self, rocket_data):
        if self.reading_data:
            try:
                s = self.ser.readline().decode().rstrip()   # Get and decode serial data
                arr = s.split(';')                          # Put data in array
                arr = [float(i) for i in arr]               # Change all values to floats

                # Update all of the data in the RocketData object
                # rocket_data was passed as a reference so changes will reflect in main.py
                rocket_data.update_data(alt=arr[0], spd=arr[1], gforce=arr[2], pressure=arr[3],
                                        bat_temp=arr[4], cube_temp=arr[5], motor_temp=arr[6],
                                        gps_lat=arr[7], gps_long=arr[8])
            except UnicodeDecodeError:
                self.msg = 'Serial data could not be decoded'

    # Establish serial connection if not made already
    #
    # Return: True if connection establish and False if connection failed
    def start_serial(self):
        try:
            if self.ser is None:
                self.ser = serial.Serial('COM3', 9600)
            self.msg = 'Serial connection secured at COM3 port with 9600 baud rate'
            return True
        except Exception:
            self.msg = "Serial connection failed to connect at COM3 port with 9600 baud rate"
            return False

    # Start/Stop taking information from the Arduino
    def start_stop_reading(self):
        if not self.reading_data:
            if self.start_serial():
                self.reading_data = True
                self.msg = 'Started reading serial data'
        else:
            self.reading_data = False
            self.msg = 'Stopped reading serial data'

    # Tell the Arduino to start the camera
    def start_stop_camera(self):
        if not self.camera_recording:
            if self.start_serial():
                self.camera_recording = True
                self.msg = 'Camera has been started'
        else:
            self.camera_recording = False
            self.msg = 'Camera has been stopped'

        if self.ser is not None:
            self.foo += 1
            self.ser.write(f'{self.foo}'.encode())
