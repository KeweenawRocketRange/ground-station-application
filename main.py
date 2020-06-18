from serial_reader import SerialReader
from rocket_data import RocketData
from graphics_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# Main python file to connect all parts of the ground station.
#
# Authors: Ethan Visscher


def setup_btns():
    ui.data_btn.clicked.connect(data_btn_clicked)
    ui.camera_btn.clicked.connect(camera_btn_clicked)


def data_btn_clicked():
    serial_reader.start_stop_reading()
    ui.data_btn.setText("Stop") if serial_reader.reading_data else ui.data_btn.setText("Start")
    update_text()


def camera_btn_clicked():
    serial_reader.start_stop_camera()
    ui.camera_btn.setText("Stop") if serial_reader.camera_recording else ui.camera_btn.setText("Start")


def update_text():
    serial_reader.get_data(rocket_data)
    rocket_data.save_data()

    ui.alt_label.setText(f'{rocket_data.alt}')
    ui.spd_label.setText(f'{rocket_data.spd}')
    ui.gforce_label.setText(f'{rocket_data.gforce}')
    ui.pressure_label.setText(f'{rocket_data.pressure}')
    ui.bat_temp_label.setText(f'{rocket_data.bat_temp}')
    ui.cubesat_temp_label.setText(f'{rocket_data.cube_temp}')
    ui.motor_temp_label.setText(f'{rocket_data.motor_temp}')
    ui.bat_temp_label.setText(f'{rocket_data.bat_temp}')
    ui.gps_label.setText(f'{rocket_data.gps_lat}, {rocket_data.gps_long}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    serial_reader = SerialReader()
    rocket_data = RocketData()
    setup_btns()
    update_text()

    MainWindow.show()
    sys.exit(app.exec_())
