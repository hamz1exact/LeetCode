# 32. Longest Valid Parentheses

Difficulty: Hard
Status: Need to be reviewed
Priority: High
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 21, 2025 12:53 PM
Solved by my own: False

$$
Solution
$$

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # sentinel base
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    # reset base
                    stack.append(i)
                else:
                    # valid substring length
                    max_len = max(max_len, i - stack[-1])

        return max_len
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