# 225. Implement Stack using Queues

Difficulty: Easy
Status: Mastred
Priority: High
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 16, 2025 3:39 AM
Solved by my own: True

$$
Solution
$$

```python
class MyStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1
    def pop(self) -> int:
        self.size -= 1
        return (self.stack.pop())

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack
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