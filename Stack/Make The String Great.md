# 921. Minimum Add to Make Parentheses Valid

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 21, 2025 12:47 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for token in s:
            if not stack:
                stack.append(token)
                continue
            if stack and stack[-1] == "(" and  token == ')':
                stack.pop()
            else:
                stack.append(token)
        return len(stack)

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