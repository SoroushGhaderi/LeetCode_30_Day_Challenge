from collections import Counter

class Solution:
    def singleNumber(self, nums):
        return [key for key,value in Counter(nums).items() if value == 1].pop()

example_list_1 = [2,2,1]
example_test_1 = Solution()
print("Single Number of Example list is: ", example_test_1.singleNumber(example_list_1))

example_list_2 = [4,1,2,1,2]
example_test_2 = Solution()
print("Single Number of Example list is: ", example_test_2.singleNumber(example_list_2))
