# 1207. Unique Number of Occurrences

Link: https://leetcode.com/problems/unique-number-of-occurrences/description/
Difficulty: Easy
Patterns: Hashing
Priority: Low
Topic: Array, Hash Table / Map / Set
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
            hashMap = {}
            c = {}
            for num in arr:
                hashMap[num] = hashMap.get(num, 0) + 1
            for k,v in hashMap.items():
                if v in c:
                    return False
                c[v] = v
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