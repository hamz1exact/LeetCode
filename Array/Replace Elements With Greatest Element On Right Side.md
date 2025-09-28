# 1299. Replace Elements with Greatest Element on Right Side

Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
Difficulty: Easy
Patterns: Iteration
Priority: Low
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        if len(arr) == 1:
            return [-1]
        elif len(arr) == 2:
            return [arr[-1], -1]
        prev = arr[-1]
        arr[-1] = -1
        currentMax = 0
        for i in range(len(arr)-2, -1, -1):
            currentMax = max(currentMax, prev)
            prev = arr[i]
            arr[i] = currentMax
        return arr
```

$$
Explaining
$$

```
# Keep Track of the prev Max Val
```

$$
Stuck-Point
$$

```

```