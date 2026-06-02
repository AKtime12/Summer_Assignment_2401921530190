class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using prefix sum
        prefix = 0
        MinPrefix = 0
        result = float('-inf')
        for num in nums:
            prefix += num
            result = max(result, prefix - MinPrefix)
            MinPrefix = min(MinPrefix, prefix)

        return result
        