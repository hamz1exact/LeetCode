# 682. Baseball Game

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
    def calPoints(self, operations: List[str]) -> int:
        prev = 0
        stack = []
        for op in operations:
            if op.isdigit() or  (op.startswith('-') and op[1:].isdigit()):
                stack.append(int(op))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                prev = 1 if prev == 0 else prev
                stack.append(2 * stack[-1])
            elif op == '+':
                first_score = stack[-1] if stack[-1] else 0
                second_score = stack[-2] if stack[-2] else 0
                stack.append(first_score + second_score) 
            prev = stack[-1] if stack else None
        return sum(stack)
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