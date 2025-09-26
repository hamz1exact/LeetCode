# 1984. Minimum Difference Between Highest and Lowest of K Scores

Difficulty: Easy
Status: Mastred
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)
Created time: August 15, 2025 2:42 AM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        min_diff = float('inf')
        for r in range(len(nums)):
            if r - l + 1 == k:
                min_diff = min(min_diff, nums[r] - nums[l])
                l += 1
            r += 1
        return min_diff
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