# 03. Valid Anagram

Difficulty: Easy
Status: Mastred
Priority: Low
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: Null
Link: https://neetcode.io/problems/is-anagram?list=neetcode150

$$
Python
$$

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

$$
Explaining
$$

```
We sort Both Words and  compare them, True of they are Equal, False Otherways
```