class Solution(object):
    def maxSubArray(self, nums):
        maximum = [nums[0]]*len(nums)
        for i in range(1,len(nums)):
            maximum[i] = max(maximum[i-1], 0)+ nums[i]
        return max(maximum)