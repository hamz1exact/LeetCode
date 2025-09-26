# 155. Min Stack

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Design, Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 16, 2025 3:39 AM
Solved by my own: True

$$
Solution
$$

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)	
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)
        return
    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None
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