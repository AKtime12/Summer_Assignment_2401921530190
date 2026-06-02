class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # using sliding window
        WindowSum = sum(nums[:k])
        MaxSum = WindowSum

        for i in range(k, len(nums)):
            WindowSum += nums[i] - nums[i - k]
            MaxSum = max(MaxSum, WindowSum)

        return MaxSum /float(k) 

        