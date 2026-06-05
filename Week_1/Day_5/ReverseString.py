# 344. Reverse String
'''
Write a function that reverses a string. The input string is given as an array of characters s.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left,right = 0,(len(s)-1)

        while left<right :
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return s

'''Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

# Intuition:
'''
1. We can use two pointers (left and right) to compare characters from the beginning and end of the string. 
2. We swap the characters at the left and right pointers and move the pointers towards the center until they meet.
3. This approach allows us to reverse the string in-place with O(1) extra memory.
'''

# Approach:
'''
1. Initialize two pointers, left and right, to the start and end of the array, respectively.
2. Use a while loop that continues until the left pointer is less than the right pointer.
    a. Inside the loop, swap the characters at the left and right pointers.
    b. Move the left pointer to the right and the right pointer to the left.
3. If the loop completes without any mismatches, return True, indicating that the string is a palindrome.
'''

# Complexity Analysis:
'''
1. Time Complexity: O(n)
2. Space Complexity: O(1)
'''

