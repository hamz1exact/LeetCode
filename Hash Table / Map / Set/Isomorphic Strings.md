# 205. Isomorphic Strings

Link: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Medium
Status: Mastred
Patterns: Hashing
Priority: Medium
Topic: Hash Table / Map / Set
Time Complexity: O(n)
Space Complexity: O(n)
Created time: July 15, 2025 2:45 PM

$$
python
$$

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        reserved = []
        for i in range(len(s)):
            if not s[i] in chars and not t[i] in reserved:
                chars[s[i]] = t[i]
                reserved.append(t[i])
            if not s[i] in chars and t[i] in reserved:
                return False
            if s[i] in chars and t[i] in reserved:
                if chars[s[i]] != t[i]:
                    return False
            if s[i] in chars and t[i] not in reserved:
                return False
        return True
```