class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p2] != nums[p1]:
                p1 += 1
                nums[p1] = nums[p2]
        return p1 + 1