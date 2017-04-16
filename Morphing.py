# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:58:28 2017

@author: Administrator
"""

import numpy as np

class dis_inter_alg:
    """ Interface between the displaying and the algorithm
    including: source and target images;
                a, b and p
                frame per second and time duration
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
        self.sourceImg=dis_inter_alg.sourceImg
        self.targetImg=dis_inter_alg.targetImg
        
        self.startPos=dis_inter_alg.startPos
        self.terminatePos=dis_inter_alg.terminatePos  
        
        self.a=dis_inter_alg.a
        self.b=dis_inter_alg.b
        self.p=dis_inter_alg.p
        
        self.morphSize=dis_inter_alg.framePerSecond*dis_inter_alg.timeDur        
        
    def LinerMorphing(self):
        dissolve_ratio=np.linspace(0.0, 1.0, num=self.morphSize)
        inter=interpolator()
        for r in dissolve_ratio:
            midPos = inter.interpolate(self.startPos,self.terminatePos,r)
        

    
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
    Calculate: u, v, X'
    """    
    def __init__(self,  sourcePos, targetPos):
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
                       
       
        
        
        
        