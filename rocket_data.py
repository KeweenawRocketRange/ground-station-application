# Object to hold all of the rocket's instantaneous data and maximum data.
# Object has function to set all of the rocket's data from one call and a function to save all data to a text file.
#
# Authors: Ethan Visscher
# Last Modified: 06/11/2020


class RocketData:
    def __init__(self):
        # Instantaneous data
        self.alt = 0
        self.speed = 0
        self.gforce = 0
        self.pressure = 0
        self.bat_temp = 0
        self.cube_temp = 0
        self.motor_temp = 0
        self.gps_lat = 0
        self.gps_long = 0

        # Maximum data
        self.max_alt = 0
        self.max_speed = 0
        self.max_gforce = 0
        self.max_pressure = 0
        self.max_bat_temp = 0
        self.max_cube_temp = 0
        self.max_motor_temp = 0

    # Function updates all of the rocket's data at once. Done in one single function because if
    # one piece of data is getting updated, they all will need to be updated. Also updates
    # the maximum data if applicable.
    #
    # args: all of the data that the rocket holds, information will be received from SerialReader
    def update_data(self, alt, speed, gforce, pressure, bat_temp, cube_temp, motor_temp, gps_lat, gps_long):
        self.alt = alt
        self.speed = speed
        self.gforce = gforce
        self.pressure = pressure
        self.bat_temp = bat_temp
        self.cube_temp = cube_temp
        self.motor_temp = motor_temp
        self.gps_lat = gps_lat
        self.gps_long = gps_long

        # Update maximum data
        self.max_alt = alt if alt > self.max_alt else None
        self.max_speed = speed if speed > self.max_speed else None
        self.max_gforce = gforce if gforce > self.max_gforce else None
        self.max_pressure = pressure if pressure > self.max_pressure else None
        self.max_bat_temp = bat_temp if bat_temp > self.max_bat_temp else None
        self.max_cube_temp = cube_temp if cube_temp > self.cube_temp else None
        self.max_motor_temp = motor_temp if motor_temp > self.motor_temp else None

    # Function saves all of the rockets data to a text file
    def save_data(self):
        pass







