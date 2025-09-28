# 413. Arithmetic Slices

Difficulty: Medium
Priority: Medium
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        max_cnt = cnt = 0
        l = 0
        k = 3
        if len(nums) < 3:
            return 0
        for r in range(len(nums)):
            if r == l:
                continue
            while r < len(nums) and l < r and nums[r] - nums[r-1] != nums[l+1] - nums[l]:
                l += 1
                cnt = 0
            if (r-l+1) == k:
                cnt += 1
                l += 1
                max_cnt += cnt
        return max_cnt

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