class Solution(object):
    def moveZeroes(self, nums):
        for each in nums:
            if each == 0:
                nums.remove(each)
                nums.append(0)
            else:
                pass
        return nums