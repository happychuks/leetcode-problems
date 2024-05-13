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