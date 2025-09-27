# 812. Largest Triangle Area

Difficulty: Easy
Status: Need to be reviewed
Priority: Low
Topic: Array, Math
Time Complexity: O(n)
Space Complexity: O(n)
Created time: September 27, 2025 11:31 PM
Solved by my own: False

$$
Solution
$$

```python
class Solution:
    def largestTriangleArea(self, a: List[List[int]]) -> float:
        return max(abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
            for x1,y1 in a for x2,y2 in a for x3,y3 in a)
```

$$
Explaining
$$

```

```

$$
Stuck-Point
$$

```

```