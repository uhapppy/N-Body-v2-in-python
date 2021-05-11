from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
from pathlib import Path
from scipy.stats import kde




dataopen="gravity.cvs"
gravity=open(dataopen)
a= np.loadtxt(gravity,delimiter=",")
n=0
plat = 100
nombreplanete , n2 = plat , plat 
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 110, 1920, 1080)
w.show()

pos = a[0:n2]
sp2=gl.GLScatterPlotItem(pos=pos , size=2,color=(0.0, 1.0, 0.0, 0.5))
w.addItem(sp2)

def update():
    global n
    global n2
    global nombreplanete 
    n+=nombreplanete
    n2+=nombreplanete
    #sp2.setData(pos=a[0:n2],size=2,color=(1.0, 0.0, 1.0, 0.5)) # with trace
    sp2.setData(pos=a[n:n2],size=3,color=(1.0, 1.0, 1.0, 1.5)) #no trace
    

    
t = QtCore.QTimer()
t.timeout.connect(update)
t.start(40)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()