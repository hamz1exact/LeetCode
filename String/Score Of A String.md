# 2302. Count Subarrays With Score Less Than K

Difficulty: Hard
Priority: Medium
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        l = 0
        summ = 0
        max_cnt = 0
        cnt = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ*(r-l+1) >= k:
                summ -= nums[l]
                l += 1
            if summ * (r-l+1) < k:
                cnt += (r-l+1)
        return cnt
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