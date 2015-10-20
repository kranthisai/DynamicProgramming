'''
Created on Oct 17, 2015

@author: FRONT-DESK-STAFF
'''
import sys
def CoinWeights(L,S):
    Min=[]
    for i in range(0,S+1):
        Min.append(sys.maxint)
    Min[0]=0
    for i in range(1,S+1):
        for j in L:
            if j<=i and Min[i-j]+1<Min[i]:
                Min[i]=Min[i-j]+1
    if Min[S]!=sys.maxint:    
        print Min[S]
    else: 
        print "no number of coins"  
def method2(L,S):
    Min=[]
    for i in range(0,S+1):
        Min.append(sys.maxint)
    Min[0]=0
    for i in range(0,len(L)):
        for j in range(1,S+1):
            if L[i]<=j and Min[j-L[i]]+1<Min[j]:
                Min[j]=Min[j-L[i]]+1
        #for k in range(1,S+1):
            #print L[i],k,Min[k]
            
    if Min[S]!=sys.maxint:    
        print Min[S]
    else: 
        print "no number of coins"
        
    
     
CoinWeights([2,3,4], 11)
method2([2,3,4], 11)
        
    