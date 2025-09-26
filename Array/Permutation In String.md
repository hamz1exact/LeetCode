# 567. Permutation in String

Link: https://leetcode.com/problems/permutation-in-string/description/
Difficulty: Medium
Status: Mastred
Patterns: Sliding Window
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: None
Created time: July 6, 2025 4:33 PM

```python
Solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            s1_length = len(s1)
            s2_length = len(s2)
            s1 = sorted(s1)
            for _ in range(s2_length):
                if sorted(s2[:s1_length]) == sorted(s1):
                    return True
                s2 = s2[1:]
            return False
```