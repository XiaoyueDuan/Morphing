# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 9:50:22 2017

@author: Xiaoyue Duan 
"""
from scipy.misc import imsave
import numpy as np

class ImageSaver:
    """
    Class Description:
        An object which can save images
    """
    def __init__(self,path):
        """
        Function Description:
            function of construtor
        Input:
            path- string, the path of file
        """
        self.__path=path

    def save(self, image, name,type='.jpg'):
        """
        Function Description:
            Save image according to its name and type
        Input:
            image- (rows, cols, 3) int narray, the image to be saved
            name- string, saving name of the image
            type- string, suffix of image, preferring '.jpg' or '.png'
        """
        fullname=self.__path+name+type
        imsave(fullname, image)

class BatchImageSaving:
    """
    Class Description:
        Save a series of images with same start name and number. e.g image1.jpg, image2.jpg...
    """

    def __init__(self,path,start_name):
        """
        Function Description:
            Save image according to its name and type
        Input:
            image- (rows, cols, 3) int narray, the image to be saved
            n- int, the order of batch iamges sequence
        """
        self.__imgSaver=ImageSaver(path)
        self.__startname=start_name

    def save(self,image,n):
        """
        Function Description:
            Save image according to its name and order
        Input:
            image- (rows, cols, 3) int narray, the image to be saved
            n- int, the order of batch iamges sequence
        """
        self.__imgSaver.save(image,self.__startname+str(n))

