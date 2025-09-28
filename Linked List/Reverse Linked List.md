# 2000. Reverse Prefix of Word

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
    def reversePrefix(self, s: str, ch: str) -> str:
        stack = [""]
        final = ""
        ok = False
        for char in s:
            stack[-1] += char
            if char == ch and not ok:
                word = reversed(list(stack[-1]))
                stack[-1] = ""
                ans = "".join(word)
                final += ans
                ok = True
        if stack:
            final += stack.pop()
        return final

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