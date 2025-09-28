# 2958. Length of Longest Subarray With at Most K Frequency

Difficulty: Medium
Priority: Medium
Topic: Sliding Window
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        l = max_cnt = 0
        freq = {}
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0)  + 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            max_cnt = max(max_cnt, r-l+1)
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