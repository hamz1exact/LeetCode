# 771. Jewels and Stones

Link: https://leetcode.com/problems/jewels-and-stones/description/
Difficulty: Easy
Patterns: Hashing
Priority: Medium
Topic: Hash Table / Map / Set
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = jewels
        s = stones
        count = 0
        sSet = {}
        jSet = {}
        for char in j:
            jSet[char] = jSet.get(char, 0) + 1
        for char in s:
            sSet[char] = sSet.get(char, 0) + 1
        for char, freq in jSet.items():
            if char in sSet:
                count +=sSet[char]
        return count
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