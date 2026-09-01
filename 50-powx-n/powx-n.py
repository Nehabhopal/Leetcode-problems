class Solution(object):
    def findPow(self, x, n):
        if n==0:
            return 1
        
        if n==1:
            return x

        a=self.findPow(x,n//2)

        if n%2==1:
            return a*a*x
        else:
            return a*a

    def myPow(self,x,n):
        if n>=0:
            return self.findPow(x,n)
        else:
            return 1/self.findPow(x,-n)
 

