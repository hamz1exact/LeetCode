# 150. Evaluate Reverse Polish Notation

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
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        Evaltokens = ('*', "+", "-", "/")
        for token in tokens:
            if token not in Evaltokens:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(num2 + num1)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return int(stack[-1])
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