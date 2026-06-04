# 566. Reshape the Matrix
'''In MATLAB, there is a very useful function called 'reshape',
   which can reshape a matrix into a new one with different size but keep its original data.
You are given a 2D array 'mat' and two integers 'r' and 'c' representing the number of rows and the number of columns of the wanted reshaped matrix, respectively.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''

# Intuition:
'''1. We can first check if the total number of elements in the original matrix (m*n) is equal to the total number of elements in the reshaped matrix (r*c). If they are not equal, we cannot reshape the matrix and should return the original matrix.
2. If they are equal, we can create a new matrix with r rows and c columns and fill it with the elements from the original matrix in row-traversing order.
3. We can use two pointers (m and n) to keep track of our position in the original matrix while filling the reshaped matrix.
4. We can iterate through the reshaped matrix and fill it with the elements from the original matrix using the pointers, updating the pointers accordingly.
'''

# Complexity Analysis:
'''1. Time Complexity: O(m*n) - We need to iterate through all the elements of the original matrix to fill the reshaped matrix.
2. Space Complexity: O(r*c) - We need to create a new matrix of size r*c to store the reshaped matrix.
'''

# Code: 

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(mat)*len(mat[0]):
            return mat
        m,n=0,0
        reshapedMat = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                reshapedMat[i][j] = mat[m][n]
                n+=1
                if n == (len(mat[0])):
                    n =0
                    m += 1
        return reshapedMat

# Example 1:
'''Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Explanation: The row-traversing of mat is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
'''


# Second Approach: 
"""
class Solution(object):
    def matrixReshape(self, mat, r, c):
        
        #:type mat: List[List[int]]
        #:type r: int
        #:type c: int
        #:rtype: List[List[int]]
        

        m,n = len(mat),len(mat[0])
        if m * n != r * c: return mat

        reshapedMat = [[0] * c for _ in range(r)]
        for i in range(m * n):
            reshapedMat[i // c][i % c] = mat[i // n][i % n]

        return reshapedMat
"""