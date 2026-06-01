class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp_nums = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in comp_nums:
                return [comp_nums[complement], i]
            comp_nums[num] = i