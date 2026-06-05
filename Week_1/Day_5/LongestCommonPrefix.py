# 14. Longest Common Prefix
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs : 
            return  ""
        commonPrifix = ""
        strs.sort()
        i = 0
        while i < len(strs[0]) and i < len(strs[-1]):
            if strs[0][i] == strs[-1][i]:
                commonPrifix += strs[0][i]
                i += 1
            else : break
        return commonPrifix


# Example 1:
'''
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

# Intuition:
'''
1. We can sort the array of strings and then compare the first and last strings in the sorted array.
2. The longest common prefix will be the common prefix of the first and last strings in the sorted array.
3. We can iterate through the characters of the first and last strings and compare them until we find a mismatch or reach the end of either string.
'''

# Approach:
'''
1. Sort the array of strings.
2. Initialize an empty string commonPrefix to store the longest common prefix.
3. Compare the first and last strings in the sorted array character by character.
4. If the characters match, append the character to commonPrefix and continue comparing the next characters.
5. If the characters do not match or we reach the end of either string, break the loop.
6. Return the commonPrefix string, which contains the longest common prefix among the array of strings.
'''

# Complexity Analysis:
'''
1. Time Complexity: O(n log n) - Sorting the array of strings takes O(n log n) time, where n is the number of strings in the array. Comparing the first and last strings takes O(m) time, where m is the length of the longest common prefix.
2. Space Complexity: O(1) - We are using a constant amount of extra space to store the common prefix string.
'''
