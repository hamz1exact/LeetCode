# 1598. Crawler Log Folder

Difficulty: Easy
Status: Mastred
Priority: Low
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 16, 2025 3:25 AM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../" and stack:
                stack.pop()
            elif log == "../" and not stack:
                continue
            elif log == './':
                continue
            else:
                stack.append(log)
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