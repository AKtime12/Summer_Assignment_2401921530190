class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start=0
        for i in range(len(nums)):
            if nums[i]!=0 :
                nums[start],nums[i]=nums[i],nums[start]
                start+=1
            
'''
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

''' DRY RUN
i=0: nums[0]=0, start=0, no swap
i=1: nums[1]=1, start=0, swap nums[0] and nums[1], start=1
i=2: nums[2]=0, start=1, no swap
i=3: nums[3]=3, start=1, swap nums[1] and nums[3], start=2
i=4: nums[4]=12, start=2, swap nums[2] and nums[4], start=3
'''

''' TIME COMPLEXITY: O(n) 
    SPACE COMPLEXITY: O(1) 
    '''

