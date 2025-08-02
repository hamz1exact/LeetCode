# 1. Concatenation of Array

Difficulty: Easy
Status: Mastred
Priority: Low
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/concatenation-of-array?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums+nums
        return ans
```

$$
Idea
$$

```
Adding the same input Twice
```