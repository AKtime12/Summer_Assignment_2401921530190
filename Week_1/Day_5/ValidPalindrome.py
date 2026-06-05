# 125. Valid Palindrome
'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right = 0,len(s) - 1

        while left<right:
            while left< right and not s[left].isalnum():
                left += 1
            while left <right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# Example 1:
'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# Intuition:
'''
1. We can use two pointers (left and right) to compare characters from the beginning and end of the string.
2. We can skip non-alphanumeric characters by moving the pointers until we find an alphanumeric character.
3. We can convert the characters to lowercase to ignore cases during comparison.
4. If the characters at the left and right pointers are not equal, we can conclude that the string is not a palindrome.
5. If the pointers cross each other, it means we have compared all characters and found them to be equal, so the string is a palindrome.
'''

# Approach:
'''
1. Initialize two pointers, left and right, to the start and end of the string, respectively.
2. Use a while loop that continues until the left pointer is less than the right pointer.
    a. Inside the loop, move the left pointer to the right until it points to an alphanumeric character or crosses the right pointer.
    b. Move the right pointer to the left until it points to an alphanumeric character or crosses the left pointer.
    c. If the characters at the left and right pointers are not equal (ignoring case), return False.
    d. Move both pointers towards the center (left += 1 and right -= 1).
3. If the loop completes without finding any mismatches, return True, indicating that the string is a palindrome.
'''

# Complexity Analysis:
'''
1. Time Complexity: O(n)
2. Space Complexity: O(1)
'''

