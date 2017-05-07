# the comment is the correct example for open a file windows

#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog, QPushButton
#from PyQt5.QtWidgets import QMainWindow

#class Ui_MainWindow(object):
#    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")

#        self.dirButton = QPushButton(QWidget(MainWindow))
#        #self.dirButton.setGeometry(QtCore.QRect(0, 0, 91, 61))
#        self.dirButton.setObjectName("dirButton")

#class Main(QMainWindow):
#    def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui=Ui_MainWindow()
#         self.ui.setupUi(self)

#         self.ui.dirButton.clicked.connect(self.browse)

#    def browse(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", 
#                                                  "","All Files (*);;Python Files (*.py)", options=options)

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    window = Main()
#    window.show()
#    sys.exit(app.exec_())


#########################################################################################
#from PyQt5 import QtWidgets,QtCore,QtGui

#class Ui_MainWindow(object):
#    def setupUi(self,MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(850, 560)

#        self.centralwidget = QtWidgets.QWidget(MainWindow)
#        self.centralwidget.setGeometry(QtCore.QRect(30, 20, 500, 300))
#        self.centralwidget.setObjectName("centralwidget")

#        self.view= View(self)
#        self.button=QtWidgets.QPushButton('Clear View',QtWidgets.QWidget(MainWindow))
#        self.button.clicked.connect(self.handleClearView)
        
#        layout=QtWidgets.QVBoxLayout(self.centralwidget)
        
#        layout.addWidget(self.button)
#        layout.addWidget(self.view)

#    def handleClearView(self):
#        self.view.scene().clear()

#class Main(QtWidgets.QMainWindow):
#    def __init__(self):
#         QtWidgets.QMainWindow.__init__(self)
#         self.ui=Ui_MainWindow()
#         self.ui.setupUi(self)

#class View(QtWidgets.QGraphicsView):
#    def __init__(self,parent):
#        QtWidgets.QGraphicsView.__init__(self)
#        self.setScene(QtWidgets.QGraphicsScene(self))
#        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))

#        pixmap = QtGui.QPixmap("..\Image\source.jpg")
#        pixItem = QtWidgets.QGraphicsPixmapItem(pixmap)
#        self.scene().addItem(pixItem)

#    def mousePressEvent(self, event):
#        self._start = event.pos()

#    def mouseReleaseEvent(self, event):
#        start = QtCore.QPointF(self.mapToScene(self._start))
#        end = QtCore.QPointF(self.mapToScene(event.pos()))
        
#        self.scene().addItem(
#            QtWidgets.QGraphicsLineItem(QtCore.QLineF(start, end)))        
        
#        for point in (start, end):
#            text = self.scene().addSimpleText(
#                '(%d, %d)' % (point.x(), point.y()))
#            text.setBrush(QtCore.Qt.red)
#            text.setPos(point)

#if __name__ == '__main__':
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    window = Main()
#    #window.resize(640, 480)
#    window.show()
#    sys.exit(app.exec_())

# Save images by matplotlib and imagemagick, though Failed
import matplotlib.pyplot as plt 
from matplotlib import animation
import cv2
import os

def load_all_images(dir):
    imgs = []
    for file_name in os.listdir(dir):
        if os.path.splitext(file_name)[-1] == '.jpg':
            # Remember that I had to flip the iPhone image, also the image was in BGR colorspace so I had to convert to RGB
            img = cv2.cvtColor(cv2.imread(os.path.join(dir, file_name)), cv2.COLOR_BGR2RGB)[::-1, ::-1, :]
            imgs.append(img)
    return imgs

def build_gif(imgs, show_gif=True, save_gif=True, title=''):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()

    def animate(i):
        ax.imshow(imgs[i])

    anim = animation.FuncAnimation(fig, animate, frames=len(imgs), interval=200, blit=True)
     
    #ims = map(lambda x: (ax.imshow(x), ax.set_title(title)), imgs)
    #im_ani = animation.ArtistAnimation(fig, ims, interval=800, repeat_delay=0, blit=False)

    if save_gif:
        anim.save('animation.gif', writer='imagemagick')

    if show_gif:
        plt.show()

    return

images=load_all_images('../Results/')
build_gif(images)


from PIL import Image
import os
file_names=sorted((fn for fn in os.listdir(self.interface.savePath) if fn.endswith('.jpg')))
images=[Image.open(self.interface.savePath+fn) for fn in file_names]

resultName=self.interface.resultImgName+".gif"
writeGif(resultName,images,duration=1)