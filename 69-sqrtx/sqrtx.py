class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        l,r = 1,x
        ans=1
        while l<=r:
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            else:
                ans=mid
                l=mid+1

        return ans        