# 125. Valid Palindrome

Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Patterns: Two Pointers
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)

Source Code:

```python
class Solution(object):
    def isPalindrome(self, s):
        if len(s) <=1:
            return True
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        s = ''.join(s)

        for i in range(len(s)):
            if s[i] != s[-(i+1)]: #Two Pointers.
                return False
        return True
```