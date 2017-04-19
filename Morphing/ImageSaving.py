# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:58:28 2017

@author: Administrator
"""

import Image
im = Image.fromarray(x)
im.save('test.png')

class ImageSaving:
    def __init__(self,path):
        """
        Function Description:
        Input:
            path- string, the file
        """