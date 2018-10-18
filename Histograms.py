import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2
#from PIL import Image


##########################################
## Do not forget to delete "return NotImplementedError"
## while implementing a function
########################################
class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
    #    return NotImplementedError

        action= QAction("&Open Input",self)
        action.triggered.connect(self.openInputImage)

        action2 = QAction ("&Open Target",self)
        action2.triggered.connect(self.openTargetImage)

        action3 = QAction ("&Exit",self)
        action3.triggered.connect(self.closeApp)

        mainmenu = self.menuBar()
        fileMenu = mainmenu.addMenu("&file")
        fileMenu.addAction(action2)
        fileMenu.addAction(action3)
        fileMenu.addAction(action)

        self.title = 'Histogram Equalization'
        self.showFullScreen()
        # You can define other things in here
        self.initUI()

    def openInputImage(self):
        # This function is called when the user clicks File->Input Image.
        label = QLabel(self)
        filename = QFileDialog.getOpenFileName()
        imagePath = filename[0]
        img = cv2.imread(imagePath)
        #plt.subplot(4, 1, 1)
        #cv2.imshow('image',img)
        #blue, green, red = cv2.split(img)
        red = img[:,:,2]
        green = img[:,:,1]
        blue = img[:,:,0]
         #cv2.imshow('green',green)
        #cv2.imshow('blue',blue)
        #cv2.imshow('red',red)
        fig = plt.figure()
        width, height = blue.shape
        i =0
        blueArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = blue[w][h]
                blueArray[temp]+=1

        plt.subplot(4, 1, 4)
        plt.bar(range(256), blueArray, color="blue")

        width, height = red.shape
        i =0
        redArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = red[w][h]
                redArray[temp]+=1
        plt.subplot(4, 1, 2)
        plt.bar(range(256), redArray, color="red")

        width, height = green.shape
        i =0
        greenArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = green[w][h]
                greenArray[temp]+=1
        plt.subplot(4, 1, 3)
        plt.bar(range(256), greenArray, color="green")
        plt.show()

        return NotImplementedError


    def openTargetImage(self):
        # This function is called when the user clicks File->Target Image.
        label = QLabel(self)
        filename = QFileDialog.getOpenFileName()
        imagePath = filename[0]
        img2 = cv2.imread(imagePath)
        red = img2[:,:,2]
        green = img2[:,:,1]
        blue = img2[:,:,0]

        fig = plt.figure()
        width, height = blue.shape
        i =0
        blueArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = blue[w][h]
                blueArray[temp]+=1

        plt.subplot(4, 1, 3)
        plt.bar(range(256), blueArray, color="blue")

        width, height = red.shape
        i =0
        redArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = red[w][h]
                redArray[temp]+=1
        plt.subplot(4, 1, 2)
        plt.bar(range(256), redArray, color="red")

        width, height = green.shape
        i =0
        greenArray = [0]* 256
        for w in range(0,width):
            for h in range(0,height):
                temp = green[w][h]
                greenArray[temp]+=1
        plt.subplot(4, 1, 4)
        plt.bar(range(256), greenArray, color="green")
        plt.show()


        return NotImplementedError

    def closeApp(self):

        return NotImplementedError

    def initUI(self):
        #return NotImplementedError
        # Write GUI initialization code

        self.show()

    def histogramButtonClicked(self):
        if not self.inputLoaded and not self.targetLoaded:
            # Error: "First load input and target images" in MessageBox
            return NotImplementedError
        if not self.inputLoaded:
            # Error: "Load input image" in MessageBox
            return NotImplementedError
        elif not self.targetLoaded:
            # Error: "Load target image" in MessageBox
            return NotImplementedError

    def calcHistogram(self, I):
        # Calculate histogram
        return NotImplementedError

    def createEmptyInputGroupBox(self):
        self.inputGroupBox = QGroupBox('Input')
        layout = QVBoxLayout()

        self.inputGroupBox.setLayout(layout)

    def createEmptyTargetGroupBox(self):
        self.targetGroupBox = QGroupBox('Target')
        layout = QVBoxLayout()

        self.targetGroupBox.setLayout(layout)

    def createEmptyResultGroupBox(self):
        self.resultGroupBox = QGroupBox('Input')
        layout = QVBoxLayout()

        self.resultGroupBox.setLayout(layout)


class PlotCanvas(FigureCanvas):
    def __init__(self, hist, parent=None, width=5, height=4, dpi=100):
        return NotImplementedError
        # Init Canvas
        self.plotHistogram(hist)

    def plotHistogram(self, hist):
        return NotImplementedError
        # Plot histogram

        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
