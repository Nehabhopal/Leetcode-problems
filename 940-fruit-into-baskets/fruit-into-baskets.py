class Solution(object):
    def totalFruit(self, nums):
        max_length=0
        left=0
        right=0
        n=len(nums)
        my_dicit={}
        while right<n:
            my_dicit[nums[right]]=my_dicit.get(nums[right],0)+1
            while len(my_dicit)>2:
                my_dicit[nums[left]]-=1
                if my_dicit[nums[left]]==0:
                    del my_dicit[nums[left]]
                left+=1
            if len(my_dicit)<=2:
                max_length=max(max_length,right-left+1)
            right+=1
        return max_length
        