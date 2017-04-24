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

from PyQt5 import QtWidgets,QtCore,QtGui

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 560)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(30, 20, 500, 210))
        self.centralwidget.setObjectName("centralwidget")

        self.view= View(self)
        self.button=QtWidgets.QPushButton('Clear View',QtWidgets.QWidget(MainWindow))
        self.button.clicked.connect(self.handleClearView)
        
        layout=QtWidgets.QVBoxLayout(self.centralwidget)
        
        layout.addWidget(self.button)
        layout.addWidget(self.view)

    def handleClearView(self):
        self.view.scene().clear()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)

         #self.ui.dirButton.clicked.connect(self.browse)

class View(QtWidgets.QGraphicsView):
    def __init__(self,parent):
        QtWidgets.QGraphicsView.__init__(self)
        self.setScene(QtWidgets.QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))

    def mousePressEvent(self, event):
        self._start = event.pos()

    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        self.scene().addItem(
            QtWidgets.QGraphicsLineItem(QtCore.QLineF(start, end)))
        for point in (start, end):
            text = self.scene().addSimpleText(
                '(%d, %d)' % (point.x(), point.y()))
            text.setBrush(QtCore.Qt.red)
            text.setPos(point)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    #window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())