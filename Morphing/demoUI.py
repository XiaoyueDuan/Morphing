# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morphingUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Morphing import Interface, Morphing
from scipy import misc
from UI_assistant import Valid
import numpy as np
from images2gif import writeGif

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
        self.SourceImg_layout.setContentsMargins(5, 0, 5, 5)
        self.SourceImg_layout.setSpacing(10)
        self.SourceImg_layout.setObjectName("SourceImg_layout")
        self.sourceImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.sourceImg_groupbox.setObjectName("sourceImg_groupbox")        
        self.sourceImg_groupbox.setLayout(self.SourceImg_layout);
        self.sourceImg_groupbox.setGeometry(QtCore.QRect(0, 0, 
                                                         self.verticalLayoutWidget.width(), 
                                                         self.verticalLayoutWidget.height()))        

        self.sourceImg_PictureView=PictureView(self)
        self.sourceImg_PictureView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sourceImg_PictureView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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
        self.TargetImg_layout.setContentsMargins(5, 0, 5, 5)
        self.TargetImg_layout.setSpacing(10)
        self.TargetImg_layout.setObjectName("TargetImg_layout")
        self.targetImg_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.targetImg_groupbox.setObjectName("targetImg_groupbox")
        self.targetImg_groupbox.setLayout(self.TargetImg_layout)
        self.targetImg_groupbox.setGeometry(QtCore.QRect(0, 0, 
                                                         self.verticalLayoutWidget_2.width(), 
                                                         self.verticalLayoutWidget_2.height()))

        self.targetImg_PictureView=PictureView(self)
        self.targetImg_PictureView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.targetImg_PictureView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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

        self.resultImgPos_label = QtWidgets.QLabel(self.resultImg_groupbox)
        self.resultImgPos_label.setGeometry(QtCore.QRect(10, 10, 420, 290))
        self.resultImgPos_label.setAlignment(QtCore.Qt.AlignCenter)
        self.resultImgPos_label.setObjectName("resultImgPos_label")

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
        self.time_SpinBox.setValue(2)
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
        self.a_slider.setValue(5)
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
        self.speed_spinBox.setValue(2)
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
        self.b_Slider.setValue(10)
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
        self.p_Slider.setValue(50)
        self.p_input_layout.addWidget(self.p_Slider)
        self.Parameters_layout.addLayout(self.p_input_layout, 2, 0, 1, 1)

        self.Generate_Play_buttons_input_layout = QtWidgets.QHBoxLayout()
        self.Generate_Play_buttons_input_layout.setObjectName("Generate_Play_buttons_input_layout")
        self.play_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.play_button.setObjectName("play_button")
        self.Generate_Play_buttons_input_layout.addWidget(self.play_button)
        self.generate_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generate_button.setObjectName("generate_button")
        self.Generate_Play_buttons_input_layout.addWidget(self.generate_button)
        self.Parameters_layout.addLayout(self.Generate_Play_buttons_input_layout, 2, 1, 1, 1)
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
        self.resultImgPos_label.setText(_translate("MainWindow", "Results"))
        self.time_label.setText(_translate("MainWindow", "time:"))
        self.second_label.setText(_translate("MainWindow", "s"))
        self.a_label.setText(_translate("MainWindow", "a:"))
        self.speed_label.setText(_translate("MainWindow", "speed:"))
        self.frame_per_second_label.setText(_translate("MainWindow", "f/s"))
        self.b_label.setText(_translate("MainWindow", "b:"))
        self.p_label.setText(_translate("MainWindow", "p:"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.generate_button.setText(_translate("MainWindow", "Generate"))

class Ui_AddEvent(QtWidgets.QMainWindow):
    aValue,bValue,pValue=range(3)
    sourceImg,targetImg,resultImg=range(3,6)
    timeDur,fps=range(6,8)

    def __init__(self):
         QtWidgets.QMainWindow.__init__(self)
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self)

         self.__addEvent()
         self.interface=Interface()
         self.valid=Valid()

    def __addEvent(self):
        # button
        self.ui.source_load_button.clicked.connect(lambda: self.__getImage(self.ui.sourceImg_PictureView,
                                                                           Ui_AddEvent.sourceImg))
        self.ui.target_load_button.clicked.connect(lambda: self.__getImage(self.ui.targetImg_PictureView,
                                                                           Ui_AddEvent.targetImg))

        self.ui.source_clear_button.clicked.connect(lambda: self.__clearView(self.ui.sourceImg_PictureView,
                                                                             Ui_AddEvent.sourceImg))
        self.ui.target_clear_button.clicked.connect(lambda: self.__clearView(self.ui.targetImg_PictureView,
                                                                             Ui_AddEvent.targetImg))
        self.ui.generate_button.clicked.connect(self.__generate_Event)
        self.ui.play_button.clicked.connect(lambda: self.__play_Event(self.ui.resultImgPos_label))

        # parameters
        a_scale=1
        self.ui.a_slider.valueChanged.connect(lambda:self.__getScollBarValue(self.ui.a_slider,self.ui.a_label,
                                                                             a_scale, Ui_AddEvent.aValue))        
        b_scale=10
        self.ui.b_Slider.valueChanged.connect(lambda:self.__getScollBarValue(self.ui.b_Slider,self.ui.b_label,
                                                                             b_scale, Ui_AddEvent.bValue))
        p_scale=self.ui.p_Slider.maximum()
        self.ui.p_Slider.valueChanged.connect(lambda:self.__getScollBarValue(self.ui.p_Slider,self.ui.p_label,
                                                                             p_scale, Ui_AddEvent.pValue))

        self.ui.time_SpinBox.valueChanged.connect(lambda:self.__getSpinBoxValue(self.ui.time_SpinBox,Ui_AddEvent.timeDur))
        self.ui.speed_spinBox.valueChanged.connect(lambda:self.__getSpinBoxValue(self.ui.speed_spinBox,Ui_AddEvent.fps))        

    def __getImage(self,PictureView,imgType):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        imgName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image',
                                                           "..\\Image",
                                                           "Image Files (*.png *.jpg *.bmp)",
                                                           options=options)  
        if imgName!='': # if loaded
            pixmap = QtGui.QPixmap(imgName)
            scaled_pixmap=pixmap.scaled(PictureView.width(),PictureView.height(), 1)
            pixItem = QtWidgets.QGraphicsPixmapItem(scaled_pixmap)        
            self.interface.setScale(pixmap.width()/scaled_pixmap.width())

            PictureView.scene().addItem(pixItem)
        
            # set image to self.interface
            img=misc.imread(imgName)
            if imgType==Ui_AddEvent.sourceImg:
                self.interface.setSourceImg(img)
                self.valid.loadSourceImg=True
            elif imgType==Ui_AddEvent.targetImg:
                self.interface.setTargetImg(img)      
                self.valid.loadTargetImg=True  
    
    def __clearView(self,PictureView,imgType):
        # Clear displaying
        PictureView.scene().clear()
        PictureView.nPoint=1

        # Clear start or terminate positions
        if imgType==Ui_AddEvent.sourceImg:
            self.interface.setStartPos(Empty_signal=True)
            self.valid.loadSourceImg=False
        elif imgType==Ui_AddEvent.sourceImg:
            self.interface.setTargetImg(Empty_signal=True)  
            self.valid.loadTargetImg=False

    def __getScollBarValue(self,ScollBar,ChangeWeidge,scale=1,valueTpye=0):
        value=float(ScollBar.value())/float(scale)
        ChangeWeidge.setText(str(value))

        if valueTpye==Ui_AddEvent.aValue:
            self.interface.setA(value)
        elif valueTpye==Ui_AddEvent.bValue:
            self.interface.setB(value)
        elif valueTpye==Ui_AddEvent.pValue:
            self.interface.setP(value)

    def __getSpinBoxValue(self,SpinBox,spinType):
        value=SpinBox.value()
        if spinType==Ui_AddEvent.timeDur:
            self.interface.setTimeDur(value)
        elif spinType==Ui_AddEvent.fps:
            self.interface.setFramePerSecond(value)

    def __generate_Event(self):
        # 1. pass all value in self.interface
        self.interface.setStartPos(self.ui.sourceImg_PictureView.position)
        self.interface.setTerminatePos(self.ui.targetImg_PictureView.position)

        #self.interface.setStartPos(
        #    np.array([[  -1.,   -1.,   -1.,   -1.],
        #           [  94.,    6.,   71.,   32.],
        #           [  60.,   71.,   66.,   99.],
        #           [ 140.,   14.,  171.,   36.],
        #           [ 171.,   70.,  160.,   92.]]))
        #self.interface.setTerminatePos(
        #    np.array([[  -1.,   -1.,   -1.,   -1.],
        #           [ 126.,   27.,   98.,   44.],
        #           [  83.,   89.,   87.,  107.],
        #           [ 161.,   27.,  178.,   41.],
        #           [ 192.,   76.,  179.,  112.]]))

        # 2. check wether the value is valid
        valid_flag=self.valid.isValid(self.interface)
        
        # 3. generate result 
        if valid_flag:
            runMor=Morphing(self.interface)
            runMor.LinerMorphing()         
            
            #from PIL import Image
            #import os
            #file_names=sorted((fn for fn in os.listdir(self.interface.savePath) if fn.endswith('.jpg')))
            #images=[Image.open(fn) for fn in file_names]

            #resultName=self.interface.resultImgName+'.GIF'
            #writeGif(resultName,images,duration=self.interface.timeDur)

    def __play_Event(self,label,type='.jpg'):
        # 4. display in the result groupbox
        #n=(self.interface.framePerSecond+2)*self.interface.timeDur
        #freq=1/float(self.interface.framePerSecond)
        #for i in range(n):
        #    fullname=self.interface.savePath+self.interface.resultImgName+str(i)+type
        #    pixmap=QtGui.QPixmap(fullname)
        #    scaled_pixmap=pixmap.scaled(label.width(),label.height(), 1)
        #    label.setPixmap(scaled_pixmap)            
        #    sleep(freq)
        
        from PIL import Image
        import os
        file_names=sorted((fn for fn in os.listdir(self.interface.savePath) if fn.endswith('.jpg')))
        images=[Image.open(self.interface.savePath+fn) for fn in file_names]

        resultName=self.interface.resultImgName+".GIF"
        writeGif(resultName,images,duration=0.1)

class PictureView(QtWidgets.QGraphicsView):
    def __init__(self,parent):
        QtWidgets.QGraphicsView.__init__(self)
        self.setScene(QtWidgets.QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))
        self.nPoint=1
        self.position=np.array([[-1,-1,-1,-1]]) 

    def mousePressEvent(self, event):
        self._start = event.pos()

    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
       
        if start!=end:        
            self.scene().addItem(
                QtWidgets.QGraphicsLineItem(QtCore.QLineF(start, end)))        

            self.position=np.concatenate((self.position, 
                                          np.array([[start.x(),start.y(),end.x(),end.y()]])), 
                                          axis=0)
        
            #text=self.scene().addSimpleText('(%d)' % self.nPoint)
            #text.setBrush(QtCore.Qt.red)
            #text.setPos(start)
            self.nPoint+=1
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

