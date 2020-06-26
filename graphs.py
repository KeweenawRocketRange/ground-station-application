from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from graphics_graphs import Ui_MainWindow
import pyqtgraph as pg
import sys
import os


# Object to hold arrays for the data for the graphs
class GraphData:
    def __init__(self):
        # 2D array to hold values from instant rocket data text file
        #            time    alt    spd    g's    psi    bat    cube   motor
        self.instant_vals = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]

        # Array to hold values from max rocket data text file
        #                alt  spd  g's  psi  bat cube  motor
        self.max_vals = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # Function to grab rocket data from text files and put it into arrays
    def txt_to_arr(self):
        with open('saved-data/instant_rocket_data.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                arr = line.split(';')
                arr = [float(i) for i in arr]

                for i in range(0, 8):
                    self.instant_vals[i].append(arr[i])

        with open('saved-data/max_rocket_data.txt', 'r') as f:
            self.max_vals = f.readline().split(';')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    graph_data = GraphData()
    graph_data.txt_to_arr()

    ui.max_alt_label.setText(graph_data.max_vals[0])
    alt_graph = pg.PlotWidget(ui.alt_tab)
    alt_graph.setStyleSheet("background-color: black;")
    alt_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
    alt_graph.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.gridLayout.addWidget(alt_graph, 1, 0, 4, 5)
    alt_graph.plot(graph_data.instant_vals[0], graph_data.instant_vals[1], pen=pg.mkPen('y', width=2))

    ui.max_speed_label.setText(graph_data.max_vals[1])
    spd_graph = pg.PlotWidget(ui.speed_tab)
    spd_graph.setStyleSheet("background-color: black;")
    spd_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
    spd_graph.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.gridLayout_2.addWidget(spd_graph, 1, 0, 4, 5)
    spd_graph.plot(graph_data.instant_vals[0], graph_data.instant_vals[2], pen=pg.mkPen('y', width=2))

    ui.max_gforce_label.setText(graph_data.max_vals[2])
    gforce_graph = pg.PlotWidget(ui.gforce_tab)
    gforce_graph.setStyleSheet("background-color: black;")
    gforce_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
    gforce_graph.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.gridLayout_3.addWidget(gforce_graph, 1, 0, 4, 5)
    gforce_graph.plot(graph_data.instant_vals[0], graph_data.instant_vals[3], pen=pg.mkPen('y', width=2))

    ui.max_pressure_label.setText(graph_data.max_vals[3])
    pressure_graph = pg.PlotWidget(ui.pressure_tab)
    pressure_graph.setStyleSheet("background-color: black;")
    pressure_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
    pressure_graph.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.gridLayout_4.addWidget(pressure_graph, 2, 0, 4, 5)
    pressure_graph.plot(graph_data.instant_vals[0], graph_data.instant_vals[4], pen=pg.mkPen('y', width=2))

    ui.max_bat_temp_label.setText(graph_data.max_vals[4])
    ui.max_cube_temp_label.setText(graph_data.max_vals[5])
    ui.max_motor_temp_label.setText(graph_data.max_vals[6])
    temp_graphs = pg.PlotWidget(ui.temp_tab)
    temp_graphs.setStyleSheet("background-color: black;")
    temp_graphs.setFrameShape(QtWidgets.QFrame.StyledPanel)
    temp_graphs.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.gridLayout_5.addWidget(temp_graphs, 3, 0, 4, 6)
    temp_graphs.plot(graph_data.instant_vals[0], graph_data.instant_vals[5], pen=pg.mkPen('y', width=2))
    temp_graphs.plot(graph_data.instant_vals[0], graph_data.instant_vals[6], pen=pg.mkPen('r', width=2))
    temp_graphs.plot(graph_data.instant_vals[0], graph_data.instant_vals[7], pen=pg.mkPen('b', width=2))

    MainWindow.showFullScreen()
    sys.exit(app.exec_())
