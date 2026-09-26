class Solution(object):
    def maxScore(self, nums, k):
        n=len(nums)
        if n==k:
            return sum(nums)
        left_sum,right_sum=0,0
        for i in range(0,k):
            left_sum+=nums[i]
        maxi=left_sum
        right_ind=n-1
        for i in range(k-1,-1,-1):
            left_sum-=nums[i]
            right_sum+=nums[right_ind]
            maxi=max(maxi,left_sum+right_sum)
            right_ind-=1
        return maxi
