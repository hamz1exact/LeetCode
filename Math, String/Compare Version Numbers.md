# 165. Compare Version Numbers

Difficulty: Medium
Priority: Medium
Topic: Math, String
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = version1.split('.')
        v2 = version2.split('.')
        print(v1, v2)
        
        l, r = 0, 0
        while l < len(v1) or r < len(v2):
            # get current revision or 0 if missing
            rev1 = int(v1[l]) if l < len(v1) else 0
            rev2 = int(v2[r]) if r < len(v2) else 0
            
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
            
            l += 1
            r += 1
        
        return 0

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