class Solution(object):
    def moveZeroes(self, nums):
        start=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[start]=nums[start],nums[i]
                start+=1