class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # using hash set
        used=set()
        for i in nums:
            if i in used:
                return True
            used.add(i)
        return False
        