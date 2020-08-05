class Solution(object):
    def maxSubArray(self, nums):
        maximum_till_there = 0
        maximum_all = 0
        for i in range(len(nums)):
            maximum_till_there += nums[i]
            
            if maximum_till_there < 0:
                maximum_till_there = 0
            if maximum_all <maximum_till_there:
                maximum_all = maximum_till_there
        return maximum_all