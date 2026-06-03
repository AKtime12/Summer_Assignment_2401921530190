class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        start,end = 0,n - 1
        SquareNums = [0]*n
        SqPointr = n - 1

        while start<=end:
            startSq =nums[start] * nums[start]
            endSq= nums[end] * nums[end]

            if startSq > endSq:
                SquareNums[SqPointr] =startSq
                start += 1
            else:
                SquareNums[SqPointr] = endSq
                end-= 1
            SqPointr-= 1

        return SquareNums
    
'''Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''
''' DRY RUN
start=0, end=4, SqPointr=4
startSq=16, endSq=100, SquareNums=[0,0,0,0,100], start=1, SqPointr=3
start=1, end=4, SqPointr=3
startSq=1, endSq=100, SquareNums=[0,0,0,100,100], end=3, SqPointr=2
start=1, end=3, SqPointr=2
startSq=1, endSq=9, SquareNums=[0,0,9,100,100], start=2, SqPointr=1
start=2, end=3, SqPointr=1
startSq=0, endSq=9, SquareNums=[0,9,9,100,100], end=2, SqPointr=0
start=2, end=2, SqPointr=0
startSq=0, endSq=0, SquareNums=[0,9,9,100,100], start=3, SqPointr=-1
'''

''' TIME COMPLEXITY: O(n) 
    SPACE COMPLEXITY: O(n) 
    '''