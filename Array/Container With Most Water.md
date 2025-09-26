# 11. Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water/description/
Difficulty: Medium
Status: Mastred
Patterns: Two Pointers
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)
Created time: July 20, 2025 3:07 PM

$$
Python
$$

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        results = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            results = max(results, area)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return results

```

$$
Idea
$$

Increment the left ptr if it’s smaller than the rught ptr and vice versa