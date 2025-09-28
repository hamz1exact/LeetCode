# 2379. Minimum Recolors to Get K Consecutive Black Blocks

Difficulty: Easy
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k==1 and "B" in blocks: return 0
        l, r = 0, 0
        min_blocks = float('inf')
        mp = {"B": 0, "W": 0}
        for r in range(len(blocks)):
            mp[blocks[r]] = mp.get(blocks[r], 0) + 1
            while r - l + 1 > k:
                mp[blocks[l]] -= 1
                l += 1
            min_blocks = min(min_blocks, k - mp["B"])
            r+=1
        return min_blocks
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