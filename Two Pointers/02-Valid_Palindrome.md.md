# 2. Valid Palindrome

Difficulty: Easy
Status: Mastred
Priority: Medium
Link: https://neetcode.io/practice#:~:text=Solution-,Valid%20Palindrome,-Easy

$$
Solution
$$

```python
class Solution(object):
    def isPalindrome(self, s):
        if len(s) <=1:
            return True
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        s = ''.join(s)

        for i in range(len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True
```

$$
Explaining
$$

```
Null
```

$$
Stuck-Point
$$

```
Null
```