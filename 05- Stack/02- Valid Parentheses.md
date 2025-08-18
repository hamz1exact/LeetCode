# 02- Valid Parentheses

Difficulty: Easy

$$
The Problem
$$

**You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.**

**The input string `s` is valid if and only if:**

**Every open bracket is closed by the same type of close bracket.Open brackets are closed in the correct order.Every close bracket has a corresponding open bracket of the same type.**

- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

**Return `true` if `s` is a valid string, and `false` otherwise.**

$$
Example
$$

```markdown
Input: s = "[]"

Output: true

Input: s = "([{}])"

Output: true

Input: s = "[(])"

Output: false
```

$$
Solution
$$

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in open_to_close:
                # Push the expected closing bracket onto the stack
                stack.append(open_to_close[char])
            elif not stack or stack.pop() != char:
                return False
        
        return not stack
```

$$
Explaining
$$

```markdown
Null
```

$$
Stuck-Point
$$

```markdown
Null
```