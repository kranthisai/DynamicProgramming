'''
Created on Oct 19, 2015

@author: Kranthi
'''
def Function(L):
    A=[]
    for i in range(len(L)):
        A.append(0)
    A[0]=1
    for i in range(1,len(L)):
        max=0
        for j in range(0,i+1):
            if L[j]<L[i]:
                if A[j]>max:
                    max=A[j] 
        if max==0:
            A[i]=1
        else:
            A[i]=1+max    
            
    max=0
    for i in A:
        if A[j]>max:
            max=A[j] 
    print max    
    
Function([1,2,3,5,3,2,4,6,7,8,9])
Function([10, 22, 9, 33, 21, 50, 41, 60, 80 ])
