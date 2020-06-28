from serial_reader import SerialReader
from rocket_data import RocketData
from graphics_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# Main python file to connect all parts of the ground station.
#
# Authors: Ethan Visscher


# Button function for the data button
# Starts the reading of serial data
def data_btn_clicked():
    serial_reader.start_stop_reading()
    ui.data_btn.setText("Stop") if serial_reader.reading_data else ui.data_btn.setText("Start")


# Button function for the camera button
# Starts the camera on the rocket
def camera_btn_clicked():
    serial_reader.start_stop_camera()
    ui.camera_btn.setText("Stop") if serial_reader.camera_recording else ui.camera_btn.setText("Start")


# Button function for the test button
# Used to test serial connection
def test_btn_clicked():
    serial_reader.start_serial()


# Grabs serial data from rocket, saves the data, then updates the text on the GUI
def update_text():
    if serial_reader.reading_data:
        try:
            serial_reader.get_data(rocket_data)
            rocket_data.save_data()

            ui.alt_label.setText(f'{int(rocket_data.alt)}')
            ui.spd_label.setText(f'{int(rocket_data.spd)}')
            ui.gforce_label.setText(f'{rocket_data.gforce}')
            ui.pressure_label.setText(f'{rocket_data.pressure}')
            ui.bat_temp_label.setText(f'{rocket_data.bat_temp}')
            ui.cubesat_temp_label.setText(f'{int(rocket_data.cube_temp)}°F')
            ui.motor_temp_label.setText(f'{int(rocket_data.motor_temp)}°F')
            ui.bat_temp_label.setText(f'{int(rocket_data.bat_temp)}°F')
            ui.gps_label.setText(f'{rocket_data.gps_lat}, {rocket_data.gps_long}')
        except Exception:
            serial_reader.msg = 'Unknown error occurred while trying to retrieve data'


# Everything in this function will be executed once per 200 milliseconds
def main_loop():
    update_text()
    ui.term_label.setText(serial_reader.msg)


if __name__ == "__main__":
    # Get graphics from graphics_main.py, graphics were created in Qt Designer
    # In order to change the GUI you have to edit the ground_station.ui in
    # the user-interfaces folder, you have to edit in Qt Designer
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serial_reader = SerialReader()
    rocket_data = RocketData()

    ui.data_btn.clicked.connect(data_btn_clicked)
    ui.camera_btn.clicked.connect(camera_btn_clicked)
    ui.test_btn.clicked.connect(serial_reader.start_serial)

    # Creates a loop, calls it every 200 milliseconds
    timer = QtCore.QTimer()
    timer.start(200)
    timer.timeout.connect(main_loop)

    MainWindow.showFullScreen()
    sys.exit(app.exec_())
