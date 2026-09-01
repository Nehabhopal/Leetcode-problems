class Solution(object):
    def findMaxAverage(self, nums,k):
        curr_sum=0
        n=len(nums)

        for i in range(k):
            curr_sum+=nums[i]

        ans=curr_sum/float(k)

        for i in range(k,n):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]

            ans=max(ans,curr_sum/float(k))
        
        return ans
        