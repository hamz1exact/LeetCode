# 1249. Minimum Remove to Make Valid Parentheses

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
    def minRemoveToMakeValid(self, s: str) -> str:

        valid_string = ""
        stack = []
        unique_case = []
        for i,char in enumerate(s):
            if char == ")" and not stack:
                unique_case.append(i)
            elif char == "(":
                stack.append(i)
            elif char == ")":
                stack.pop()
        stack += unique_case
        stack = set(stack)
        for i, char in enumerate(s):
            if i in stack:
                continue
            else:
                valid_string += char
        return valid_string

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