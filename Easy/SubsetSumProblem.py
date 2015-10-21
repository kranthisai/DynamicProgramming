'''
Created on Oct 20, 2015

@author: system
'''

def Subset(L,n,S):
    if S==0:
        return True 
    elif L[n-1]==S:
        return True
    elif n==0 and S!=0:
        return False 
    elif L[n-1]>S:
        return Subset(L,n-1,S) 
    else:
        t=Subset(L, n-1, S)
        t1=Subset(L, n-1, S-L[n-1])
        return t or t1

if __name__ == '__main__':
    print Subset([2,3,5,6,7,8], 6, 20)
    pass
