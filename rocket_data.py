# Object to hold all of the rocket's instantaneous data and maximum data.
# Object has function to set all of the rocket's data from one call and a function to save all data to a text file.
#
# Authors: Ethan Visscher


class RocketData:
    def __init__(self):
        self.time = 0   # Used for save_data(). Keeps track of what time interval the data was saved at

        # Instantaneous data
        self.alt = 0
        self.spd = 0
        self.gforce = 0
        self.pressure = 0
        self.bat_temp = 0
        self.cube_temp = 0
        self.motor_temp = 0
        self.gps_lat = 0
        self.gps_long = 0

        # Maximum data
        self.max_alt = 0
        self.max_spd = 0
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
    def update_data(self, alt, spd, gforce, pressure, bat_temp, cube_temp, motor_temp, gps_lat, gps_long):
        self.time += 1

        # Update instant data
        self.alt = alt
        self.spd = spd
        self.gforce = gforce
        self.pressure = pressure
        self.bat_temp = bat_temp
        self.cube_temp = cube_temp
        self.motor_temp = motor_temp
        self.gps_lat = gps_lat
        self.gps_long = gps_long

        # Update maximum data
        self.max_alt = self.alt if self.alt > self.max_alt else None
        self.max_spd = self.spd if self.spd > self.max_spd else None
        self.max_gforce = self.gforce if self.gforce > self.max_gforce else None
        self.max_pressure = self.pressure if self.pressure > self.max_pressure else None
        self.max_bat_temp = self.bat_temp if self.bat_temp > self.max_bat_temp else None
        self.max_cube_temp = self.cube_temp if self.cube_temp > self.max_cube_temp else None
        self.max_motor_temp = self.motor_temp if self.motor_temp > self.max_motor_temp else None

    # Function saves all of the rockets data to a text file.
    # Data is written in a way that another part of the ground station can read, not necessarily human-readable.
    def save_data(self):
        # Save instantaneous data
        with open('saved-data/instant_rocket_data.txt', 'a') as f:
            f.write(f'{self.time};'
                    f'{self.alt};'
                    f'{self.spd};'
                    f'{self.gforce};'
                    f'{self.pressure};'
                    f'{self.bat_temp};'
                    f'{self.cube_temp};'
                    f'{self.motor_temp};'
                    f'{self.gps_lat};'
                    f'{self.gps_long}\n')
            f.close()

        # Save maximum data
        with open('saved-data/max_rocket_data.txt', 'w') as f:
            f.write(f'{self.max_alt};'
                    f'{self.max_spd};'
                    f'{self.max_gforce};'
                    f'{self.max_pressure};'
                    f'{self.max_bat_temp};'
                    f'{self.max_cube_temp};'
                    f'{self.max_motor_temp}')
            f.close()

    # Print all rocket data to terminal
    def print_data(self):
        print(f'Time/Ping: {self.time}\n'
              f'Altitude:  {self.alt}\n'
              f'Speed: {self.spd}\n'
              f'G-Force: {self.gforce}\n'
              f'Pressure: {self.pressure}\n'
              f'Battery Temperature: {self.bat_temp}\n'
              f'Cubesat Temperature: {self.cube_temp}\n'
              f'Motor Temperature: {self.motor_temp}\n'
              f'Latitude: {self.gps_lat}\n'
              f'Longitude: {self.gps_long}\n\n'
              f'Max Altitude: {self.max_alt}\n'
              f'Max Speed: {self.max_spd}\n'
              f'Max G-Force: {self.max_gforce}\n'
              f'Max Pressure: {self.max_pressure}\n'
              f'Max Battery Temperature: {self.max_bat_temp}\n'
              f'Max Cubesat Temperature: {self.max_cube_temp}\n'
              f'Max Motor Temperature: {self.max_motor_temp}\n')







