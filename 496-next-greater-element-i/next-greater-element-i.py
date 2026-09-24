class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num

            stack.append(num)

        while stack:
            greater[stack.pop()] = -1

        return [greater[num] for num in nums1]