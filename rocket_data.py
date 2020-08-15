# Object to hold all of the rocket's instantaneous data and maximum data.
# Object has function to set all of the rocket's data from one call and a function to save all data to a text file.
#
# Authors: Ethan Visscher


class RocketData:
    def __init__(self):
        self.time = 0   # Used for save_data(). Keeps track of what time interval the data was saved at.

        # Instantaneous data
        self.x = 0
        self.y = 0
        self.z = 0
        self.alt = 0
        self.gforce = 0
        self.pressure = 0
        self.temp = 0

        self.roll = 0
        self.yaw = 0
        self.pitch = 0

        # Maximum data
        self.max_x = 0
        self.max_y = 0
        self.max_z = 0
        self.max_alt = 0
        self.max_gforce = 0
        self.max_pressure = 0
        self.max_temp = 0

    # Function updates all of the rocket's data at once. Done in one single function because if
    # one piece of data is getting updated, they all will need to be updated. Also updates
    # the maximum data if applicable.
    #
    # args: all of the data that the rocket holds, information will be received from SerialReader
    def update_data(self, x, y, z, alt, gforce, pressure, temp):
        self.time += 1

        # Update instant data
        self.x = x
        self.y = y
        self.z = z
        self.alt = alt
        self.gforce = gforce
        self.pressure = pressure
        self.temp = temp

        # Update maximum data
        self.max_x = self.x if self.x > self.max_x else self.max_x
        self.max_y = self.y if self.y > self.max_y else self.max_y
        self.max_z = self.z if self.z > self.max_z else self.max_z
        self.max_alt = self.alt if self.alt > self.max_alt else self.max_alt
        self.max_gforce = self.gforce if self.gforce > self.max_gforce else self.max_gforce
        self.max_pressure = self.pressure if self.pressure > self.max_pressure else self.max_pressure
        self.max_temp = self.temp if self.temp > self.max_temp else self.max_temp

    # Function saves all of the rockets data to a text file.
    # Data is written in a way that another part of the ground station can read, not necessarily human-readable.
    def save_data(self):
        # Save instantaneous data
        with open('saved-data/instant_rocket_data.txt', 'a') as f:
            f.write(f'{self.time};'
                    f'{self.x};'
                    f'{self.y};'
                    f'{self.z};'
                    f'{self.alt};'
                    f'{self.gforce};'
                    f'{self.pressure};'
                    f'{self.temp}\n')
            f.close()

        # Save maximum data
        with open('saved-data/max_rocket_data.txt', 'w') as f:
            f.write(f'{self.max_x};'
                    f'{self.max_y};'
                    f'{self.max_z};'
                    f'{self.max_alt};'
                    f'{self.max_gforce};'
                    f'{self.max_pressure};'
                    f'{self.max_temp};')
            f.close()

    # Print all rocket data to terminal
    def print_data(self):
        print(f'Time/Ping: {self.time}\n'
              f'x: {self.x}\n'
              f'Speed (y): {self.y}\n'
              f'z: {self.z}\n'
              f'Altitude:  {self.alt}\n'
              f'G-Force: {self.gforce}\n'
              f'Pressure: {self.pressure}\n'
              f'Temperature: {self.temp}\n'
              f'Max Altitude: {self.max_alt}\n'
              f'x: {self.max_x}\n'
              f'Max Speed (y): {self.max_y}\n'
              f'z: {self.max_z}\n'
              f'Max G-Force: {self.max_gforce}\n'
              f'Max Pressure: {self.max_pressure}\n'
              f'Max Temperature: {self.max_temp}\n')







