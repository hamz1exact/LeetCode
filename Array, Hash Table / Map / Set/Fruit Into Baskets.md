# 904. Fruit Into Baskets

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Array, Hash Table / Map / Set
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 10, 2025 2:30 AM

$$
Solution
$$

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        
        mp = defaultdict(int)
        left = 0
        maxFruits = 0
        for right in range(len(fruits)):
            mp[fruits[right]] += 1
            while len(mp) > 2:
                mp[fruits[left]] -= 1
                if mp[fruits[left]] == 0:
                    del mp[fruits[left]]
                left += 1

            maxFruits = max(maxFruits, right - left + 1)

        return maxFruits
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