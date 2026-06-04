# INTUITION : 
'''
1. We can iterate through the matrix and add the elements of the primary diagonal (mat[i][i]) and
 the secondary diagonal (mat[i][n-i-1]) to the sum.
2. central element (mat[i][n-i-1]) is counted twice when n is odd, so we need to subtract it once from the sum.
'''

# Approach:
'''
1. Initialize a variable Sum to 0 to store the sum of the diagonals.
2. Get the size of the matrix n.
3. Iterate through the matrix using a loop from 0 to n-1:
   a. For each index i, add the element of the primary diagonal (mat[i][i]) and the secondary diagonal (mat[i][n-i-1]) to Sum.
   b. If i is equal to n-i-1 (which means we are at the central element in an odd-sized matrix), subtract that element from Sum to avoid double counting.
4. Return the final value of Sum.
'''

# Complexity Analysis:
'''
1. Time Complexity: O(n) - We iterate through the matrix once, where n is the size of the matrix.
2. Space Complexity: O(1) - We use a constant amount of extra space to store the sum and the size of the matrix.
'''

# Code

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        Sum = 0
        n= len(mat)
        for i in range(n):
            Sum += mat[i][i] + mat[i][n-i-1]
            if i == n-i-1:
                Sum -= mat[i][n-i-1]
        return Sum


# Example 1:
'''
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Note that element mat[1][1] = 5 is counted only once.
'''
