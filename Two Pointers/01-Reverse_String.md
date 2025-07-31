# 1. Reverse String

Difficulty: Easy
Status: Mastred
Priority: Medium
Link: https://neetcode.io/problems/reverse-string?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
```

$$
Explaining
$$

```python
Null
```