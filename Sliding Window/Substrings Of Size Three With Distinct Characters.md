# 1876. Substrings of Size Three with Distinct Characters

Difficulty: Easy
Status: Mastred
Priority: High
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 28, 2025 10:03 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        counter = {}
        cnt = l = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            if r - l + 1 == k:
                if len(counter) == 3:
                    cnt += 1
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
        return cnt

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