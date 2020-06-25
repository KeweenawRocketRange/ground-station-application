from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os

# 2D array to hold values from instant rocket data text file
#            time    alt    spd    g's    psi    bat    cube   motor
graph_vals = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]


def txt_to_arr():
    with open('saved-data/instant_rocket_data.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            arr = line.split(';')
            arr = [float(i) for i in arr]

            for i in range(0, 8):
                graph_vals[i].append(arr[i])


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    txt_to_arr()
    window.graphWidget.plot(graph_vals[0], graph_vals[1])
    window.graphWidget.plot(graph_vals[0], graph_vals[2])
    window.graphWidget.plot(graph_vals[0], graph_vals[3])
    window.graphWidget.plot(graph_vals[0], graph_vals[4])
    window.graphWidget.plot(graph_vals[0], graph_vals[5])
    window.graphWidget.plot(graph_vals[0], graph_vals[6])
    window.graphWidget.plot(graph_vals[0], graph_vals[7])

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
