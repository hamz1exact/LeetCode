# 71. Simplify Path

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