# 54. Spiral Matrix
'''Given an m x n matrix, return all elements of the matrix in spiral order.
'''
# Intuition:
'''
1. We can use four pointers (left, right, top, bottom) to keep track of the boundaries of the matrix that we need to traverse.
2. We can start by traversing from left to right along the top row, then move down along the right column, 
   then move from right to left along the bottom row, and finally move up along the left column.
3. We need to ensure that we don't visit the same element multiple times.
4. We can continue this process until we have traversed all the elements in the matrix.
5. We can store the elements in a list and return it at the end.
'''

# Approach:
'''
1. Initialize an empty list spiralMat to store the elements in spiral order.
2. Initialize four pointers: left, right, top, and bottom to keep track of the boundaries of the matrix.
3. Use a while loop that continues until the top pointer is less than or equal to the bottom pointer and the left pointer is less than or equal to the right pointer.
    a. Traverse from left to right along the top row and append the elements to spiralMat. Then, increment the top pointer.
    b. Traverse from top to bottom along the right column and append the elements to spiralMat. Then, decrement the right pointer.
    c. If the top pointer is still less than or equal to the bottom pointer, traverse from right to left along the bottom row and append the elements to spiralMat. Then, decrement the bottom pointer.
    d. If the left pointer is still less than or equal to the right pointer, traverse from bottom to top along the left column and append the elements to spiralMat. Then, increment the left pointer.
4. Return the spiralMat list containing the elements in spiral order.
'''

# Complexity Analysis:
'''
1. Time Complexity: O(m*n) - We need to traverse all the elements in the matrix once, where m is the number of rows and n is the number of columns.
2. Space Complexity: O(m*n) - We need to store all the elements in the spiralMat list, which can contain at most m*n elements.
'''

# Code:


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        spiralMat = []
        left=0
        right = len(matrix[0])-1
        top=0
        bottom = len(matrix)-1
        while top<=bottom and left<=right:

            # left-->right
            for j in range(left, right + 1):
                spiralMat.append(matrix[top][j])
            top += 1

            # top-->bottom
            for i in range(top, bottom + 1):
                spiralMat.append(matrix[i][right])
            right -= 1

            if top<=bottom:
                # right -->left
                for j in range(right, left - 1, -1):
                    spiralMat.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # bottom --> top
                for i in range(bottom, top - 1, -1):
                    spiralMat.append(matrix[i][left])
                left += 1

        return spiralMat
    
# Example 1:
'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Explanation: The first row is traversed from left to right, the last column is traversed from top to bottom, the last row is traversed from right to left and the first column is traversed from bottom to top. Then, we continue the spiral traversal again until all the elements are visited.
'''