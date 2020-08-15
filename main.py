from serial_reader import SerialReader
from rocket_data import RocketData
from graphics_main_new import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys
import os

# Main python file to connect all parts of the ground station.
#
# To convert UI file to python code use command: pyuic5 -x ground_station.ui -o graphics_main.py
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
        serial_reader.get_data(rocket_data)
        rocket_data.save_data()
        rocket_data.print_data()

        ui.spd_label.setText(f'{int(rocket_data.y)}')
        ui.alt_label.setText(f'{int(rocket_data.alt)}')
        ui.gforce_label.setText(f'{rocket_data.gforce}')
        ui.pressure_label.setText(f'{int(rocket_data.pressure)}')
        ui.temp_label.setText(f'{rocket_data.temp} °C')


# Updates the 3d rendering of the rocket based off the rockets x, y, and z accelerations
def update_render():
    if serial_reader.reading_data:
        rocket_render.rotate(20, 1, 0, 0)


# Everything in this function will be executed once per 200 milliseconds
def main_loop():
    update_text()
    update_render()
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

    # 3D graph
    ui.main_view = gl.GLViewWidget(ui.gridWidget5)
    ui.main_view.setObjectName("main_graph")
    ui.gridLayout_5.addWidget(ui.main_view, 0, 0, 1, 1)
    ui.main_grid.addWidget(ui.gridWidget5, 0, 1, 3, 1)
    ui.horizontalLayout.addLayout(ui.main_grid)
    ui.main_view.show()

    x_grid = gl.GLGridItem()
    y_grid = gl.GLGridItem()
    z_grid = gl.GLGridItem()
    ui.main_view.addItem(x_grid)
    ui.main_view.addItem(y_grid)
    ui.main_view.addItem(z_grid)
    x_grid.rotate(90, 0, 1, 0)
    y_grid.rotate(90, 1, 0, 0)

    verts = np.array([
        [0, 0, 10],
        [2, 0, 0],
        [1, 2, 0],
        [1, 1, 1]
    ])
    faces = np.array([
        [0, 1, 2],
        [0, 1, 3],
        [0, 2, 3],
        [1, 2, 3]
    ])
    colors = np.array([
        [1, 0, 0, 0.3],
        [0, 1, 0, 0.3],
        [0, 0, 1, 0.3],
        [1, 1, 0, 0.3]
    ])
#    rocket_mesh = gl.GLMeshItem(vertexes=verts, faces=faces, faceColors=colors)
    rocket_mesh = gl.MeshData.cylinder(20, 20, 2, 8)
    rocket_render = gl.GLMeshItem(meshdata=rocket_mesh, smooth=True, shader='shaded', glOptions='opaque')
    ui.main_view.addItem(rocket_render)

    # Creates a loop, calls it every 200 milliseconds
    timer = QtCore.QTimer()
    timer.start(50)
    timer.timeout.connect(main_loop)

    MainWindow.show()
    sys.exit(app.exec_())
