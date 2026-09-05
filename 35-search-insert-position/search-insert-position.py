class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        l,r=0,n-1
        ans=n

        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                ans=min(ans,mid)
                r=mid-1
            else:
                l=mid+1
        return ans
        