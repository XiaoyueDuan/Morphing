# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morphingUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        ##########################################################################
        self.SourceImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.SourceImg_layout.setContentsMargins(0, 0, 0, 0)
        self.SourceImg_layout.setSpacing(10)
        self.SourceImg_layout.setObjectName("SourceImg_layout")
        self.sourceImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.sourceImg_groupbox.setObjectName("sourceImg_groupbox")        
        self.SourceImg_layout.addWidget(self.sourceImg_groupbox)

        self.sourceImg_PictureView=PictureView(self)
        self.SourceImg_layout.addWidget(self.sourceImg_PictureView)
        ##########################################################################

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.SourceImgButtons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.SourceImgButtons_layout.setContentsMargins(0, 0, 0, 0)
        self.SourceImgButtons_layout.setObjectName("SourceImgButtons_layout")
        self.source_load_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.source_load_button.setObjectName("source_load_button")
        self.SourceImgButtons_layout.addWidget(self.source_load_button)
        self.source_clear_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.source_clear_button.setObjectName("source_clear_button")
        self.SourceImgButtons_layout.addWidget(self.source_clear_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 510, 331, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.TargetImgButtons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TargetImgButtons_layout.setContentsMargins(0, 0, 0, 0)
        self.TargetImgButtons_layout.setObjectName("TargetImgButtons_layout")
        self.target_load_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.target_load_button.setObjectName("target_load_button")
        self.TargetImgButtons_layout.addWidget(self.target_load_button)
        self.target_clear_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.target_clear_button.setObjectName("target_clear_button")
        self.TargetImgButtons_layout.addWidget(self.target_clear_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 290, 331, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        ##########################################################################
        self.TargetImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.TargetImg_layout.setContentsMargins(0, 0, 0, 0)
        self.TargetImg_layout.setSpacing(10)
        self.TargetImg_layout.setObjectName("TargetImg_layout")
        self.targetImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.targetImg_groupbox.setObjectName("targetImg_groupbox")
        self.TargetImg_layout.addWidget(self.targetImg_groupbox)

        self.targetImg_PictureView=PictureView(self)
        self.TargetImg_layout.addWidget(self.targetImg_PictureView)
        ##########################################################################

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 20, 441, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.ResultImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ResultImg_layout.setContentsMargins(0, 0, 0, 0)
        self.ResultImg_layout.setObjectName("ResultImg_layout")
        self.resultImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.resultImg_groupbox.setObjectName("resultImg_groupbox")
        self.ResultImg_layout.addWidget(self.resultImg_groupbox)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(380, 350, 441, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Parameters_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Parameters_layout.setContentsMargins(0, 0, 0, 0)
        self.Parameters_layout.setObjectName("Parameters_layout")
        self.time_input_layout = QtWidgets.QHBoxLayout()
        self.time_input_layout.setObjectName("time_input_layout")
        self.time_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.time_input_layout.addWidget(self.time_label)
        self.time_SpinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.time_SpinBox.setObjectName("time_SpinBox")
        self.time_input_layout.addWidget(self.time_SpinBox)
        self.second_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.second_label.setObjectName("second_label")
        self.time_input_layout.addWidget(self.second_label)
        self.Parameters_layout.addLayout(self.time_input_layout, 0, 1, 1, 1)
        self.a_input_layout = QtWidgets.QHBoxLayout()
        self.a_input_layout.setObjectName("a_input_layout")
        self.a_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.a_label.setObjectName("a_label")
        self.a_input_layout.addWidget(self.a_label)
        self.a_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.a_slider.setSingleStep(5)
        self.a_slider.setPageStep(20)
        self.a_slider.setOrientation(QtCore.Qt.Horizontal)
        self.a_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.a_slider.setObjectName("a_slider")
        self.a_input_layout.addWidget(self.a_slider)
        self.Parameters_layout.addLayout(self.a_input_layout, 0, 0, 1, 1)
        self.speed_input_layout = QtWidgets.QHBoxLayout()
        self.speed_input_layout.setObjectName("speed_input_layout")
        self.speed_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.speed_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speed_label.setObjectName("speed_label")
        self.speed_input_layout.addWidget(self.speed_label)
        self.speed_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.speed_spinBox.setObjectName("speed_spinBox")
        self.speed_input_layout.addWidget(self.speed_spinBox)
        self.frame_per_second_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.frame_per_second_label.setObjectName("frame_per_second_label")
        self.speed_input_layout.addWidget(self.frame_per_second_label)
        self.Parameters_layout.addLayout(self.speed_input_layout, 1, 1, 1, 1)
        self.b_input_layout = QtWidgets.QHBoxLayout()
        self.b_input_layout.setObjectName("b_input_layout")
        self.b_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b_label.setObjectName("b_label")
        self.b_input_layout.addWidget(self.b_label)
        self.b_Slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.b_Slider.setMinimum(5)
        self.b_Slider.setMaximum(20)
        self.b_Slider.setSingleStep(1)
        self.b_Slider.setPageStep(5)
        self.b_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.b_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.b_Slider.setObjectName("b_Slider")
        self.b_input_layout.addWidget(self.b_Slider)
        self.Parameters_layout.addLayout(self.b_input_layout, 1, 0, 1, 1)
        self.p_input_layout = QtWidgets.QHBoxLayout()
        self.p_input_layout.setObjectName("p_input_layout")
        self.p_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.p_label.setObjectName("p_label")
        self.p_input_layout.addWidget(self.p_label)
        self.p_Slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.p_Slider.setMaximum(100)
        self.p_Slider.setSingleStep(10)
        self.p_Slider.setPageStep(20)
        self.p_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.p_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.p_Slider.setObjectName("p_Slider")
        self.p_input_layout.addWidget(self.p_Slider)
        self.Parameters_layout.addLayout(self.p_input_layout, 2, 0, 1, 1)
        self.Save_Play_buttons_input_layout = QtWidgets.QHBoxLayout()
        self.Save_Play_buttons_input_layout.setObjectName("Save_Play_buttons_input_layout")
        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.Save_Play_buttons_input_layout.addWidget(self.save_button)
        self.play_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.play_button.setObjectName("play_button")
        self.Save_Play_buttons_input_layout.addWidget(self.play_button)
        self.Parameters_layout.addLayout(self.Save_Play_buttons_input_layout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Morphing Program"))
        self.sourceImg_groupbox.setTitle(_translate("MainWindow", "Source Image"))
        self.source_load_button.setText(_translate("MainWindow", "Load"))
        self.source_clear_button.setText(_translate("MainWindow", "Clear"))
        self.target_load_button.setText(_translate("MainWindow", "Load"))
        self.target_clear_button.setText(_translate("MainWindow", "Clear"))
        self.targetImg_groupbox.setTitle(_translate("MainWindow", "Target Image"))
        self.resultImg_groupbox.setTitle(_translate("MainWindow", "Result Image"))
        self.time_label.setText(_translate("MainWindow", "time:"))
        self.second_label.setText(_translate("MainWindow", "s"))
        self.a_label.setText(_translate("MainWindow", "a:"))
        self.speed_label.setText(_translate("MainWindow", "speed:"))
        self.frame_per_second_label.setText(_translate("MainWindow", "f/s"))
        self.b_label.setText(_translate("MainWindow", "b:"))
        self.p_label.setText(_translate("MainWindow", "p:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.play_button.setText(_translate("MainWindow", "Play"))

class Ui_AddEvent(QtWidgets.QMainWindow):
    def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)

         self.__addEvent()

    def __addEvent(self):
        self.ui.source_load_button.clicked.connect(lambda: self.__getImage(self.ui.sourceImg_PictureView))
        self.ui.target_load_button.clicked.connect(lambda: self.__getImage(self.ui.targetImg_PictureView))

        self.ui.source_clear_button.clicked.connect(lambda: self.__clearView(self.ui.sourceImg_PictureView))
        self.ui.target_clear_button.clicked.connect(lambda: self.__clearView(self.ui.targetImg_PictureView))

    def __getImage(self,PictureView):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        imgName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image',
                                                           "..\\Image",
                                                           "Image Files (*.png *.jpg *.bmp)",
                                                           options=options)   
        pixmap = QtGui.QPixmap(imgName)
        pixItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        PictureView.scene().addItem(pixItem)
    
    def __clearView(self,PictureView):
        PictureView.scene().clear()

class PictureView(QtWidgets.QGraphicsView):
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_AddEvent()
    window.show()
    sys.exit(app.exec_())

