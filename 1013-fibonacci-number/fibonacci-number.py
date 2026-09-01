class Solution(object):
    def fib(self, n):
        nums=[0,1]
        if n<=1:
            return n
    
        for i in range(2,n+1):
            nums.append(nums[i - 1] + nums[i - 2])

        return nums[n]