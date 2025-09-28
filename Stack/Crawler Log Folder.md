# 1598. Crawler Log Folder

Difficulty: Easy
Priority: Low
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)

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