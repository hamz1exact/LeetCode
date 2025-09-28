# 383. Ransom Note

Link: https://leetcode.com/problems/ransom-note/description/
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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = ransomNote
        m = magazine
        Rset = {}
        Mset = {}
        for char in r:
            Rset[char] = Rset.get(char,0) +1
        for char in m:
            Mset[char] = Mset.get(char, 0)+1
        for k,v in Rset.items():   
            if k not in Mset or Rset[k] > Mset[k]:
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