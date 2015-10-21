# cook your code here
import numpy as np
def DpSubset(L,n,S):
    Subset=np.zeros((n+1,S+1))
    for i in range(0,n+1):
        Subset[i][0]=True 
    
    for j in range(1,S+1):
        Subset[0][j]=j
    for i in range(1,n+1):
        for j in range(1,S+1):
            if L[i-1]>Subset[0][j]:
                if i==1:
                    Subset[i][j]=False 
                else:
                    Subset[i][j]=Subset[i-1][j]

            else:
                if i==1:
                    if L[i-1]==Subset[0][j]:
                        Subset[i][j]=True 
                    else:
                        Subset[i][j]=False 
                else:
                    #print i,j,L[i-1]
                    if Subset[i-1][j]==True:
                        Subset[i][j]=True
                    else:
                        Subset[i][j]=Subset[i-1][j-L[i-1]] 
    if Subset[n][S]==True:
        return "Yes" 
    else:
        return "No"
        
t=raw_input()
N=int(t.split(" ")[0])
Q=int(t.split(" ")[1])
l=raw_input().split(" ")
for i in l:
    i=int(i)
while(Q>0):
    q=raw_input().split(" ")
    if int(q[0])==1:
        I=int(q[1])
        W=int(q[2])
        l[I-1]=W 
        #print l 
    if int(q[0])==2:
        L=int(q[1])
        R=int(q[2])
        j=R-1
        for i in range(L-1,R):
            if i<j:
                t=l[i] 
                l[i]=l[j]
                l[j]=t 
                j-=1
        #print l
    if int(q[0])==3:
        L=int(q[1])
        R=int(q[2])
        W=int(q[3])
        A=[]
        for i in range(L-1,R):
            A.append(int(l[i])) 
        B=sorted(A)
        x=DpSubset(B,len(B),W)
        print x 
    Q-=1    
        
        
