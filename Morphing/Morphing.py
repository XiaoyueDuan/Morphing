# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:58:28 2017

@author: Xiaoyue Duan
"""

import numpy as np
import ImageSaving as iSaver

class dis_inter_alg:
    """ 
    Class Description:
        Interface between the displaying and the algorithm
    including:
        - source and target images;
        - a, b and p
        - frame per second and time duration
    """
    def __init__(self):
        self.sourceImg=0
        self.targetImg=0
        
        self.startPos=0
        self.terminatePos=0
        
        self.a=0
        self.b=0
        self.p=0
        
        self.framePerSecond=0
        self.timeDur=0
        
    def convertImg(self,rawSourImg,rawTarImg):
        self.sourceImg=rawSourImg
        self.targetImg=rawTarImg

class morphing:
    def __init__(self, dis_inter_alg):
        """
        Function Description:
            
        Attribute:
            a ~ [0, inf]
            b ~ [0.5, 2]
            p ~ [0, 1]
        Input:

        """
        self.sourceImg=dis_inter_alg.sourceImg
        self.targetImg=dis_inter_alg.targetImg
        
        self.startPos=dis_inter_alg.startPos
        self.terminatePos=dis_inter_alg.terminatePos  
        
        self.a=dis_inter_alg.a
        self.b=dis_inter_alg.b
        self.p=dis_inter_alg.p
        
        self.morphSize=dis_inter_alg.framePerSecond*dis_inter_alg.timeDur   
        
        self.__savePath=""
        self.__sourceImgName=""     
        self.__targetImgName=""     
        
    def setImgName(self,path):
        """
        Function Description:
            name- string, the path for image to be saved    
        """
        self.__savePath=path

    def setImgName(self,name,type="source"):
        """
        Function Description:
            name- string, the name to be assigned to source or target image
            type- string, two option:"source" or "target"
        """
        if type=="source":
            self.__sourceImgName=name
        elif type=="target":
            self.__targetImgName=name

    def LinerMorphing(self):
        dissolve_ratio=np.linspace(1.0, 0.0, num=self.morphSize)
        inter=interpolator()

        # Initialize a source image processor
        source_mid_proc=TargetImage(self.startPos,self.terminatePos,self.sourceImg) 
        source_mid_proc.set_a_p_b(self.a,self.b,self.p)
        sImgSaver=iSaver.BatchImageSaving(self.__savePath,self.__sourceImgName)

        # Initialize a target image processor
        target_mid_proc=TargetImage(self.startPos,self.terminatePos,self.targetImg) 
        target_mid_proc.set_a_p_b(self.a,self.b,self.p)
        tImgSaver=iSaver.BatchImageSaving(self.__savePath,self.__targetImgName)

        # Initialize a result image saver
        rImgSaver=iSaver.BatchImageSaving(self.__savePath,'result')
        
        for idx,r in enumerate(dissolve_ratio):
            midPos = inter.interpolate(self.startPos,self.terminatePos,r)
            
            source_mid_proc.set_Calculator(self.startPos,midPos)
            source_mid_img=source_mid_proc.targetImage()

            target_mid_proc.set_Calculator(self.terminatePos,midPos)
            target_mid_img=target_mid_proc.targetImage()

            midImg=np.around(source_mid_img*r+target_mid_img*(1-r))

            # Save images
            sImgSaver.save(source_mid_img,idx)
            tImgSaver.save(target_mid_img,idx)
            rImgSaver.save(midImg,idx)
    
class interpolator:
    """"Interpolation method"""
    def interpolate(self,  sourcePos, targetPos, ratio, method="liner"):
        """
            method: string
            sourcePos: [n*4] numpy array 
            targetPos: [n*4] numpy array 
            ratio: float
        """
        if method=="liner":
            return sourcePos*(1-ratio)+targetPos*ratio
        else:
            return -1 #Need to be completed!
            
class Calculator:
    """
    Calculate: u, v, Xi'(line_wise) and etc.
    """    
    def __init__(self, sourcePos, targetPos):
        """ 
        input:
            sourcePos: n*4 narray 
            targetPos: n*4 narray 
        """
        self.P=sourcePos[:,0:1]
        self.Q=sourcePos[:,2:3]    
        self.QminsP=self.Q-self.P
        self.QPdist=np.linalg.norm(self.QminsP)
        
        self.tP=targetPos[:,0:1]
        self.tQ=targetPos[:,2:3]
        self.tQminstP=self.tQ-self.tP
        self.tQPdist=np.linalg.norm(self.tQminstP)
        
    def calU(self,X):
        """
        input:
            X=[x,y]
        return:
            u is a n*2 narray
        """
        XminusP=X-self.P
        QminusP=X-self.Q
        QPdist_square=np.square(self.QPdist)
        
        u=np.dot(XminusP,QminusP)/QPdist_square
        return u
        
    def calV(self,X):
        """
        input:
            X=[x,y]
        return:
            v is a n*2 narray
        """
        XminusP=X-self.P
        
        ortho=Perpend()
        OrthoQminusP=ortho.perpendicular(X-self.Q)
        
        v=np.dot(XminusP,OrthoQminusP)/self.QPdist
        return v
    
    def calNewX(self,u,v):
        """ 
        function description:
            calculate X'
        input:
            u- is a n*2 narray
            v- is a n*2 narray
        return:
            newX- a n*2 narray
        """
        ortho=Perpend()
        OrthoQminusP=ortho.perpendicular(self.tQminstP)
        
        newX=self.tP+np.dot(u,self.tQminstP)+np.dot(v,OrthoQminusP)/self.tQPdist
        return newX
    
    def offset(self,newX,X):
        """ 
        function description:
            calculate the offset = X'-X
        input:
            newX- [x2,y2]
            X- [x1,y1]
        return:
            (X'-X)- [x2-x1,y2-y1]
        """
        return newX-X
    
    def X_PQdist(self,X):
        """ 
        function description:
            calculate the distance from X to all PQs(perpendicular distance)
        input:
            X=[x,y]
        return:
            distance- a (n,) narray
        """
        distance=np.abs(np.cross(X,self.QminP))
        return distance
    
    def PQlength(self):
        """ 
        function description:
            calculate the length of PQs
        input:
            
        return:
            |PQs|- a (n,) vector
        """
        return np.linalg.norm(self.QminP)
                    
class Perpend:
    """
    Calculate: Perpendicular(Q-P), which is orthogonal to (Q-P) as well as same length of (Q-P)
    """
    def perpendicular(vectors):
       length=np.linalg.norm(vectors)
       perpend_vectors=np.ones((vectors.shape))
       
       horInd=(vectors[:,1]==0)
       perpend_vectors[horInd,0]=0
       perpend_vectors[horInd,1]=length[horInd]
       
       verInd=(vectors[:,0]==0)
       perpend_vectors[verInd,1]=0
       perpend_vectors[horInd,0]=length[verInd]
       
       valInd=np.logical_not(horInd | verInd)
       # suppose the first columns value = 1
       perpend_vectors[valInd,1]=-perpend_vectors[valInd,0]/perpend_vectors[valInd,1]
                      
       perpend_vectors=perpend_vectors/np.linalg.norm(perpend_vectors)*length
       
       # only valid ones will calculate its perpendicular vector
       return perpend_vectors    
                       
class TargetImage:
    """
    Class description:
        Calculate all position in Target Image 
    
    """    
    def __init__(self, sourcePos, targetPos, sourceImg):
        """
        Function Description:
        Input:
            sourcePos- (n,4) narray
            targetPos- (n,4) narray
            sourceImg- (rows, cols, 3) int narray(if RGB)
        """
        self.__calculator=Calculator(sourcePos, targetPos)
        self.__img=sourceImg

        self.__a=0.5
        self.__p=0
        self.__b=0.5

    def set_a_p_b(self,a,p,b):
        self.__a=a
        self.__b=b
        self.__p=p
    
    def set_Calculator(self, sourcePos, targetPos):
        """
        Function Description:
        Input:
            sourcePos- (n,4) narray
            targetPos- (n,4) narray

        """
        self.__calculator=Calculator(sourcePos, targetPos)

    def set_Img(self, img):
        """
        Input:    
            img- (rows, cols, 3) int narray(if RGB)
        """
        self.__img=img

    def targetImage(self):
        """ 
        Function description:
            Calculate Target Image corresponding to Source Image
        input:
        return:
            targetImage- (row, col, 3), int narray, the target image
        """
        imgSize=self.__img.shape[:-1] # shape of first 2 dimension
        targetImage=np.zeros_like(self.__img)
        for i,j in zip(range(imgSize[0]),range(imgSize[1])):
            X=np.array([i,j])
            newX=self.__position_pixel_wise(X)
            targetImage[i,j,:]=self.__img[newX,:]

        return targetImage

    def __position_pixel_wise(self,X):
        """ 
        Function description:
            Calculate the position in Target Image corresponding to (row, col) which in Source Image
        input:
            X- (row, col), int narray 
        return:
            newX- X', (int, int)
        """
        u=self.__calculator.calU(X)
        v=self.__calculator.calV(X)
        newX_wise=self.__calculator.calNewX(u,v)
        D=self.__calculator.offset(newX_wise,X)

        dist=self.__calculator.X_PQdist(X)
        length=self.__calculator.PQlength()
        weight=self.weight(dist,length)

        weightSum=np.sum(weight)            # float
        Dsum=np.sum(np.multiply(D,weight))  # float (x,y)

        newX =np.around(X + Dsum/weightSum)
        return newX

    def weight(self, dist, length):
        """ 
        Function description:
            Calculate weight = ( (length)^p / (a+dist) )^b
        input:
            dist- the distance from X to PQ, (n,) narray
            length- length of PQ, (n,) narray
        return:
            weight- a (n,) vector
        """
        r1=np.power(length,self.__p)   # (length)^p
        r2=self.__a+dist               # (a+dist)
        r3=r1/r2                       # (length)^p / (a+dist)
        weight=np.power(r3,self.__b)       # ( (length)^p / (a+dist) )^b    

        return weight