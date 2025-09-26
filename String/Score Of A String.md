# 3110. Score of a String

Difficulty: Easy
Status: Mastred
Priority: Medium
Topic: String
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 10, 2025 2:32 AM

$$
Solution
$$

```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) < 2:
            return 0
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans
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