# 71. Simplify Path

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 19, 2025 2:14 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("/", " ")
        path = path.split()
        stack = []
        for token in path:
            if token == "..":
                if not stack:
                    continue
                stack.pop()
            elif token == ".":
                continue
            else:
                stack.append(token)
        s = '/'
        s += '/'.join(stack)
        return s
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