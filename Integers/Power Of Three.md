# 326. Power of Three

Link: https://leetcode.com/problems/power-of-three/description/
Difficulty: Easy
Status: Mastred
Patterns: Modulo Arithmetic
Priority: Medium
Topic: Integers
Time Complexity: O(n)
Space Complexity: O(1)
Created time: July 3, 2025 11:55 PM

```python
Solution:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        n = float(n)
        while n.is_integer():
            if n == 1:
                return True
            n = n / 3
        return False
        
```