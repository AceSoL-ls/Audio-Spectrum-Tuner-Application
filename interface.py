import pyqtgraph as pg
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

win = pg.plot(title="Sympan Tuner")
win.show()

app.exec_()