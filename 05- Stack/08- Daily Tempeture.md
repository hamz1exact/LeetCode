# 08- Daily Tempeture

Difficulty: Medium

$$
The Problem
$$

**You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the `ith` day.**

**Return an array `result` where `result[i]` is the number of days after the `ith` day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the `ith` day, set `result[i]` to `0` instead.**

$$
Example
$$

```markdown
Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
```

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

```markdown
Null
```

$$
Stuck-Point
$$

```markdown
Null
```