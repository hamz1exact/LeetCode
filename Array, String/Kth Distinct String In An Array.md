# 2053. Kth Distinct String in an Array

Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
Difficulty: Easy
Patterns: Counting, Hashing, String
Priority: High
Topic: Array, String
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        freq = Counter(arr)
        c = 0
        ans = ''
        for key, v in freq.items():
            if v == 1:
                c += 1
                if c == k:
                    return key
        return ""¸
            
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