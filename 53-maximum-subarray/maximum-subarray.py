class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        ans=nums[0]
        curr_sum=0

        for i in nums:
            curr_sum+=i
            if curr_sum>ans:
                ans=curr_sum
            if curr_sum<0:
                curr_sum=0

        return ans
        