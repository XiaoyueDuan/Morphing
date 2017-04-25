# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morphingUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        ############## SourceImg_layout and its widgets START ##############
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.SourceImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.SourceImg_layout.setContentsMargins(0, 0, 0, 0)
        self.SourceImg_layout.setSpacing(10)
        self.SourceImg_layout.setObjectName("SourceImg_layout")

        self.sourceImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.sourceImg_groupbox.setObjectName("sourceImg_groupbox")

        self.sourceImgPos_label = QtWidgets.QLabel(self.sourceImg_groupbox)
        self.sourceImgPos_label.setGeometry(QtCore.QRect(10, 10, 310, 190))
        self.sourceImgPos_label.setTextFormat(QtCore.Qt.AutoText)
        self.sourceImgPos_label.setScaledContents(False)
        self.sourceImgPos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceImgPos_label.setObjectName("sourceImgPos_label")

        self.SourceImg_layout.addWidget(self.sourceImg_groupbox)
        ############## SourceImg_layout and its widgets END ##############


        ############## SourceImgButtons_layout and its widgets START ##############
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.SourceImgButtons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.SourceImgButtons_layout.setContentsMargins(0, 0, 0, 0)
        self.SourceImgButtons_layout.setObjectName("SourceImgButtons_layout")

        self.source_load_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.source_load_button.setObjectName("source_load_button")
        self.SourceImgButtons_layout.addWidget(self.source_load_button)

        self.source_draw_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.source_draw_button.setObjectName("source_draw_button")
        self.SourceImgButtons_layout.addWidget(self.source_draw_button)

        self.source_finish_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.source_finish_button.setObjectName("source_finish_button")
        self.SourceImgButtons_layout.addWidget(self.source_finish_button)
        ############## SourceImgButtons_layout and its widgets END ##############


        ############## TargetImg_layout and its widgets START ##############
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 510, 331, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.TargetImgButtons_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TargetImgButtons_layout.setContentsMargins(0, 0, 0, 0)
        self.TargetImgButtons_layout.setObjectName("TargetImgButtons_layout")

        self.target_load_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.target_load_button.setObjectName("target_load_button")
        self.TargetImgButtons_layout.addWidget(self.target_load_button)

        self.target_draw_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.target_draw_button.setObjectName("target_draw_button")
        self.TargetImgButtons_layout.addWidget(self.target_draw_button)

        self.target_finish_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.target_finish_button.setObjectName("target_finish_button")
        self.TargetImgButtons_layout.addWidget(self.target_finish_button)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 290, 331, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.TargetImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.TargetImg_layout.setContentsMargins(0, 0, 0, 0)
        self.TargetImg_layout.setSpacing(10)
        self.TargetImg_layout.setObjectName("TargetImg_layout")

        self.targetImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.targetImg_groupbox.setObjectName("targetImg_groupbox")

        self.targetImgPos_label = QtWidgets.QLabel(self.targetImg_groupbox)
        self.targetImgPos_label.setGeometry(QtCore.QRect(10, 10, 310, 190))
        self.targetImgPos_label.setTextFormat(QtCore.Qt.AutoText)
        self.targetImgPos_label.setScaledContents(False)
        self.targetImgPos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.targetImgPos_label.setObjectName("targetImgPos_label")

        self.TargetImg_layout.addWidget(self.targetImg_groupbox)
        ############## TargetImg_layout and its widgets END ##############


        ############## ResultImg_layout and its widgets START ##############
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 20, 441, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.ResultImg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ResultImg_layout.setContentsMargins(0, 0, 0, 0)
        self.ResultImg_layout.setObjectName("ResultImg_layout")

        self.resultImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.resultImg_groupbox.setObjectName("resultImg_groupbox")

        self.resultImgPos_label = QtWidgets.QLabel(self.resultImg_groupbox)
        self.resultImgPos_label.setGeometry(QtCore.QRect(10, 10, 420, 290))
        self.resultImgPos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.resultImgPos_label.setObjectName("resultImgPos_label")

        self.ResultImg_layout.addWidget(self.resultImg_groupbox)
        ############## ResultImg_layout and its widgets START ##############


        ############## Parameters_layout and its widgets START ##############
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(380, 350, 441, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.Parameters_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Parameters_layout.setContentsMargins(0, 0, 0, 0)
        self.Parameters_layout.setObjectName("Parameters_layout")


        ############## time_input_layout and its widgets START ##############
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
        ############## time_input_layout and its widgets END ##############


        ############## a_input_layout and its widgets START ##############
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
        ############## a_input_layout and its widgets END ##############


        ############## speed_input_layout and its widgets START ##############
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
        ############## speed_input_layout and its widgets END ##############


        ############## b_layout and its widgets START ##############
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
        ############## b_layout and its widgets END ##############

        ############## p_layout and its widgets START ##############
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
        ############## p_layout and its widgets END ##############

        ############## p_layout and its widgets START ##############
        self.Save_Play_buttons_input_layout = QtWidgets.QHBoxLayout()
        self.Save_Play_buttons_input_layout.setObjectName("Save_Play_buttons_input_layout")

        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.Save_Play_buttons_input_layout.addWidget(self.save_button)

        self.play_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.play_button.setObjectName("play_button")
        self.Save_Play_buttons_input_layout.addWidget(self.play_button)

        self.Parameters_layout.addLayout(self.Save_Play_buttons_input_layout, 2, 1, 1, 1)
        ############## p_layout and its widgets START ##############
        ############## Parameters_layout and its widgets END ##############

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
        self.source_draw_button.setText(_translate("MainWindow", "Draw"))
        self.source_finish_button.setText(_translate("MainWindow", "Finish"))
        self.target_load_button.setText(_translate("MainWindow", "Load"))
        self.target_draw_button.setText(_translate("MainWindow", "Draw"))
        self.target_finish_button.setText(_translate("MainWindow", "Finish"))
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
        self.ui.source_load_button.clicked.connect(lambda: self.__getImage(self.ui.sourceImgPos_label))
        self.ui.target_load_button.clicked.connect(lambda: self.__getImage(self.ui.targetImgPos_label))

    def __getImage(self,Pos_label):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        imgName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image',
                                                           "..\\Image",
                                                           "Image Files (*.png *.jpg *.bmp)",
                                                           options=options)
        
        pixmap=QtGui.QPixmap(imgName)
        scaled_pixmap=pixmap.scaled(Pos_label.width(),Pos_label.height(), 1)
        Pos_label.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_AddEvent()
    window.show()
    sys.exit(app.exec_())

#if __name__ == "__main__":    
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())

