# 739. Daily Temperatures

Difficulty: Medium
Priority: Medium
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        popIndex = 0
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] < curr:
                popIndex = stack.pop()
                calc = i - popIndex
                ans[popIndex] = calc
            stack.append(i)
        return ans
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