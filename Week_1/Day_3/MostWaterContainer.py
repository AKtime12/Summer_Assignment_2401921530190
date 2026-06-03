class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start,end = 0,len(height) - 1
        Max = 0
        while start < end :
            Area = min(height[start], height[end])*(end - start)
            Max = max(Max,Area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return Max
'''Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''
''' DRY RUN
start=0, end=8, Max=0
Area = min(1, 7) * (8 - 0) = 1 * 8 = 8, Max = 8
start=0, end=7, Max=8
Area = min(1, 3) * (7 - 0) = 1 * 7 = 7, Max = 8
start=0, end=6, Max=8
Area = min(1, 8) * (6 - 0) = 1 * 6 = 6, Max = 8
start=0, end=5, Max=8
Area = min(1, 4) * (5 - 0) = 1 * 5 = 5, Max = 8
start=0, end=4, Max=8
Area = min(1, 5) * (4 - 0) = 1 * 4 = 4, Max = 8
start=0, end=3, Max=8
Area = min(1, 2) * (3 - 0) = 1 * 3 = 3, Max = 8
start=0, end=2, Max=8
Area = min(1, 6) * (2 - 0) = 1 * 2 = 2, Max = 8
start=0, end=1, Max=8
Area = min(1, 8) * (1 - 0) = 1 * 1 = 1, Max = 8
start=1, end=1, Max=8
'''

''' TIME COMPLEXITY: O(n) 
    SPACE COMPLEXITY: O(1) 
    '''