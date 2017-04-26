# -*- coding: utf-8 -*-

"""
    File Description:
        The .py file aims to assist morphingUI.py with more advanced function,
        e.g. add events, interact with morphing algorithm
"""

from Morphing import Interface
import numpy as np

class Valid():
    """
    Class Description:
        The goal of this class is to check whether the data is enough to run morphing algorithm.
        The condition of valid state is all bool type attributes are True. 
    """
    def __init__(self):
        self.loadSourceImg=False
        self.loadTargetImg=False

    def checkDataType(self,interface):
        """
        Function Description;
            Check whether the data type in interface is correct
        """
        valid=True
        if(type(interface.sourceImg) is not np.ndarray):
            print('Error: The format of source image is not numpy.ndarray')
            valid=False
        if(type(interface.targetImg) is not np.ndarray):
            print('Error: The format of target image is not numpy.ndarray')
            valid=False

        if(type(interface.a) is not int):
            print('Error: The format of a is not int')
            valid=False
        if(type(interface.b) is not float):
            print('Error: The format of b is not float')
            valid=False
        if(type(interface.p) is not float):
            print('Error: The format of p is not int')
            valid=False
        if(type(interface.framePerSecond) is not int):
            print('Error: The format of frame per second is not int')
            valid=False
        if(type(interface.timeDur) is not int):
            print('Error: The format of time duration is not int')
            valid=False

        return valid

    def checkDataValue(self,interface):
        """
        Function Description;
            Check whether the data value or size in interface is correct
        """
        valid=True
        if not self.loadSourceImg:
            print('Error: Have not loaded source image')
            valid=False
        if not self.loadTargetImg:
            print('Error: Have not loaded source image')
            valid=False

        if interface.startPos.shape[1]!=4:
            print('Error: The number of column of source image is not equal to 4')
            valid=False
        if interface.terminatePos.shape[1]!=4:
            print('Error: The number of column of target image is not equal to 4')
            valid=False

        if interface.startPos.shape[0]!=interface.terminatePos.shape[0]:
            print('Error: The number of lines in source and target image is different')
            valid=False

        if interface.a<0:
            print('Error: a is less than 0')
            valid=False
        if interface.b<0:
            print('Error: b is less than 0')
            valid=False
        if interface.p<0:
            print('Error: p is less than 0')
            valid=False
        if interface.framePerSecond<=0:
            print('Error: frame per second is less than 0')
            valid=False
        if interface.timeDur<0:
            print('Error: time duration is less than 0')
            valid=False

        return valid

    def isValid(self,interface):
        valid=self.checkDataType(interface)
        valid=valid and self.checkDataValue(interface)
        return valid
        