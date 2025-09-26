# 2161. Partition Array According to Given Pivot

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 12, 2025 4:11 AM

$$
Solution
$$

```python
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal = []
        greater = []
        index = -1
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return less_than+equal+greater
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