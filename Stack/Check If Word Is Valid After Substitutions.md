# 1003. Check If Word Is Valid After Substitutions

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
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "c":
                if len(stack) >=2:
                    b = stack.pop()
                    a = stack.pop()
                    if b != 'b' or a != 'a':
                        return False
                    continue
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True

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