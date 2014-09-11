from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



class PressureFigure(QtGui.QWidget):

    redrawCounter = 0

    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.X = np.arange(1,5,1)
        self.Y = np.arange(1,6,1)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.Z = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.figure.set_facecolor('white')
        self.ax.grid(True)
        self.ax.set_zlim(0, 500)
        self.ax.set_xlim(0,6)
        self.ax.set_ylim(0,6)
        self.surf = self.ax.plot_surface(self.X,self.Y,self.Z)
        plt.tight_layout()
        self.canvas = FigureCanvas(self.figure)
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.canvas.draw()



    def update_data(self, data):

        self.redrawCounter += 1
        for key in data:
            #print(key)
            if key>=1 and key<=20:
                x,y = self.map_id_to_xy(key)
                #print((key,x,y))
                self.Z[x-1][y-1] = data[key]


        if self.redrawCounter > 32:
            self.redrawCounter = 0
            #print('redraw')
            self.surf.remove()
            self.surf = self.ax.plot_surface(self.X,self.Y,self.Z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
            self.canvas.draw()



    def map_id_to_xy(self,key):
        x = key/4
        if key%4 != 0:
            x += 1
        y = key - (x-1)*4
        return x,y

