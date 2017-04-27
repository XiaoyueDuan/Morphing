# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:58:28 2017

@author: Xiaoyue Duan
"""

import numpy as np
import ImageSaving as iSaver

class Interface:
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
        
        self.startPos=np.array([[-1,-1,-1,-1]])
        self.terminatePos=np.array([[-1,-1,-1,-1]])
        
        self.a=5
        self.b=1.0
        self.p=0.5
        
        self.framePerSecond=2
        self.timeDur=2

        self.savePath='../Results/'
        self.sourceImgName="source"     
        self.targetImgName="target"  
        self.resultImgName="result"
        self.scale=1.0

    def convertImg(self,rawSourImg,rawTarImg):
        self.sourceImg=rawSourImg
        self.targetImg=rawTarImg

    def setScale(self,scale):
        self.scale=scale

    def setA(self,a):
        self.a=a

    def setB(self,b):
        self.b=b

    def setP(self,p):
        self.p=p

    def setFramePerSecond(self,fps):
        self.framePerSecond=fps

    def setTimeDur(self,timeDur):
        self.timeDur=timeDur

    def setStartPos(self,Pos=None,Empty_signal=False):
        """
        Function Description;
            Set start position
        """
        if Empty_signal:
            self.startPos=np.array([[-1,-1,-1,-1]]) 
            return
        self.startPos=np.concatenate((self.startPos, Pos), axis=0)
        self.startPos=self.startPos[2:,:]
        self.startPos=(self.startPos*self.scale).astype(int)

    def setTerminatePos(self,Pos=None,Empty_signal=False):
        if Empty_signal:
            self.terminatePos=np.array([[-1,-1,-1,-1]])
            return
        self.terminatePos=np.concatenate((self.terminatePos,Pos),axis=0)
        self.terminatePos=self.terminatePos[2:,:]
        self.terminatePos=(self.terminatePos*self.scale).astype(int)

    def setSourceImg(self,SourceImg):
        self.sourceImg=SourceImg
    
    def setTargetImg(self,TargetImg):
        self.targetImg=TargetImg

class Morphing:
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
        self.fps=dis_inter_alg.framePerSecond
        self.time=dis_inter_alg.timeDur
        
        self.__savePath=dis_inter_alg.savePath
        self.__sourceImgName=dis_inter_alg.sourceImgName
        self.__targetImgName=dis_inter_alg.targetImgName
        
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
        dissolve_ratio=np.linspace(1.0, 0.0, num=self.morphSize+2) # +2 since the first and last are source image and target image respectively
        inter=interpolator()

        # Initialize a source image processor
        source_mid_proc=TargetImage(self.startPos,self.terminatePos,self.sourceImg) 
        source_mid_proc.set_a_p_b(self.a,self.b,self.p)

        # Initialize a target image processor
        target_mid_proc=TargetImage(self.startPos,self.terminatePos,self.targetImg) 
        target_mid_proc.set_a_p_b(self.a,self.b,self.p)

        sImgSaver=iSaver.BatchImageSaving(self.__savePath,self.__sourceImgName)
        tImgSaver=iSaver.BatchImageSaving(self.__savePath,self.__targetImgName)
        # Initialize a result image saver
        rImgSaver=iSaver.BatchImageSaving(self.__savePath,self.__resultImgName)
        
        for idx,r in enumerate(dissolve_ratio):
            midPos = inter.interpolate(self.startPos,self.terminatePos,r)
            
            if idx==0:  
                source_mid_img=self.sourceImg
            else:
                source_mid_proc.set_Calculator(self.startPos,midPos)
                source_mid_img=source_mid_proc.targetImage()

            # if idx==last one
            # target_mid_img==self.targetImg
            target_mid_proc.set_Calculator(self.terminatePos,midPos)
            target_mid_img=target_mid_proc.targetImage()

            midImg=np.around(source_mid_img*r+target_mid_img*(1-r))

            # Save images
            sImgSaver.save(source_mid_img,idx)
            tImgSaver.save(target_mid_img,idx)
            rImgSaver.save(midImg,idx)

        rImgSaver.end()
    
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
            return sourcePos*ratio+targetPos*(1-ratio)
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
        self.P=sourcePos[:,0:2]
        self.Q=sourcePos[:,2:]    
        self.QminsP=self.Q-self.P
        self.QPdist=np.linalg.norm(self.QminsP,axis=1)
        
        self.tP=targetPos[:,0:2]
        self.tQ=targetPos[:,2:]
        self.tQminstP=self.tQ-self.tP
        self.tQPdist=np.linalg.norm(self.tQminstP,axis=1)
        
    def calU(self,X):
        """
        input:
            X=[x,y]
        return:
            u is a n*2 narray
        """
        XminusP=X-self.P
        QminusP=self.QminsP
        QPdist_square=np.square(self.QPdist)
        
        u=np.sum(np.multiply(XminusP,QminusP),axis=1)/QPdist_square
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
        OrthoQminusP=ortho.perpendicular(self.QminsP)
        
        v=np.sum(np.multiply(XminusP,OrthoQminusP),axis=1)/self.QPdist
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
        
        u=u.reshape(-1,1)
        v=v.reshape(-1,1)
        tQPdist=self.tQPdist.reshape(-1,1)
        newX=self.tP+np.multiply(u,self.tQminstP)+np.multiply(v,OrthoQminusP)/tQPdist
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
    
    def X_PQdist(self,X,u,v):
        """ 
        function description:
            calculate the shortest distance from X to all PQs
            when 0<u<1, the pedal on the PQ, distance=|v|(perpendicular distance)
            when u<0,   the pedal at outer of P side, distance=|XP|
            when u>1,   the pedal at outer of Q side, distance=|XQ|
        input:
            X=[x,y]
            u- (n,) float narray
            v- (n,) float narray
        return:
            distance- a (n,) narray
        """
        # distance=|XP x QP| / |QP|
        distance=np.abs(v)
        #distance=np.abs(np.cross(X-self.P,self.QminsP))/self.QPdist

        less0ind=u<0         
        distance[less0ind]=np.linalg.norm(self.P[less0ind,:]-X,axis=1)

        larger1ind=u>1
        distance[larger1ind]=np.linalg.norm(self.Q[larger1ind,:]-X,axis=1)
        
        return distance
    
    def PQlength(self):
        """ 
        function description:
            calculate the length of PQs
        input:
            
        return:
            |PQs|- a (n,) vector
        """
        return self.QPdist
                    
class Perpend:
    """
    Calculate: Perpendicular(Q-P), which is orthogonal to (Q-P) as well as same length of (Q-P)
    """
    def perpendicular(self,vectors):
       perpend_vectors=np.ones((vectors.shape))
       perpend_vectors[:,0]=-vectors[:,1]
       perpend_vectors[:,1]=vectors[:,0]
       
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
        for i in range(imgSize[0]):
            for j in range(imgSize[1]):
                X=np.array([i,j])
                newX=self.__position_pixel_wise(X,imgSize)
                targetImage[i,j,:]=self.__img[newX[0],newX[1],:]

        return targetImage

    def __position_pixel_wise(self,X,imgSize):
        """ 
        Function description:
            Calculate the position in Target Image corresponding to (row, col) which in Source Image
        input:
            X- (row, col), int narray 
        return:
            newX- X', (int, int)
        """
        def setCorrectPos(X):
            if X[0]<0:
                X[0]=0
            elif X[0]>=imgSize[0]:
                X[0]=imgSize[0]-1

            if X[1]<0:
                X[1]=0
            elif X[1]>=imgSize[1]:
                X[1]=imgSize[1]-1
            return X

        u=self.__calculator.calU(X)
        v=self.__calculator.calV(X)
        newX_wise=self.__calculator.calNewX(u,v)

        D=self.__calculator.offset(newX_wise,X)

        dist=self.__calculator.X_PQdist(X,u,v)
        length=self.__calculator.PQlength()
        weight=self.weight(dist,length)

        weightSum=np.sum(weight)            # float
        Dsum=np.sum(np.multiply(D,weight.reshape(-1,1)),axis=0)  # float (x,y)

        newX =np.around(X + Dsum/weightSum).astype(int)
        newX =setCorrectPos(newX)
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