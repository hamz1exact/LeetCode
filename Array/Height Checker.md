# 1051. Height Checker

Difficulty: Easy
Priority: Medium
Topic: Array
Time Complexity: O(n Log n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                c += 1
        return c
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