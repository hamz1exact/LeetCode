# 3090. Maximum Length Substring With Two Occurrences

Difficulty: Easy
Priority: High
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
            counter = {}
            l = max_cnt = 0
            k = 2
            max_val = 0
            for r in range(len(s)):
                counter[s[r]] = counter.get(s[r], 0 ) + 1
                while counter[s[r]] > 2:
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        del counter[s[l]] 
                    l+=1
                max_cnt = max(max_cnt, r-l+1)
            return max_cnt
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