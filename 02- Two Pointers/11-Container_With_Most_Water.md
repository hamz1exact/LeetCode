# 11. Container With Most Water

Difficulty: Medium

Status: Mastred

Priority: High

Link: https://neetcode.io/problems/max-water-container?list=neetcode250

$$
The Problem
$$

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

$$
Example
$$

![](image/water.png)

```markdown
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

$$
Solution
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
Explaining
$$

```markdown
# At Each Step We calculate the area, and we move the pointer that point to the lower boundary, if left > right we move right
```

$$
Stuck-Point
$$

```markdown
Null
```