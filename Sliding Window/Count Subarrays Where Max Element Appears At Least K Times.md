# 2962. Count Subarrays Where Max Element Appears at Least K Times

Difficulty: Medium
Status: Need to be reviewed
Priority: High
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 23, 2025 2:13 PM
Solved by my own: False

$$
Solution
$$

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = cnt = ans = 0
        maxval = max(nums)
        for r in range(len(nums)):
            if nums[r] == maxval:
                cnt += 1
            while cnt == k:
                if nums[l] == maxval:
                    cnt -= 1
                l+=1
            ans += l
        return ans
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