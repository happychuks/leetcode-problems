""" Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters. """

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest_palindrome = ""
        for i in range(len(s)):
            palindrome1 = expand_around_center(s, i, i)
            palindrome2 = expand_around_center(s, i, i + 1)
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
        
        return longest_palindrome
    
""" 
- Use a helper function to expand the palindromic substring centered around a given position, which simplifies the main function.

- Iterate over the string and find the longest palindromic substring centered around each position, considering both odd-length and even-length palindromes.

- Use the max function to find the longest palindromic substring among the options, which ensures that the longest palindrome is always chosen.

This solution has a time complexity of O(n^2), where n is the length of the input string, because it iterates over the string and expands the palindromic substring centered around each position. The space complexity is O(1) because it only uses a few extra variables to store the longest palindromic substring.
 """
