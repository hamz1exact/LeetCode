# 1003. Check If Word Is Valid After Substitutions

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 31, 2025 11:38 PM
Solved by my own: True

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