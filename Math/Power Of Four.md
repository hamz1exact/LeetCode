# 3254. Find the Power of K-Size Subarrays I

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
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ans = [0] * len(nums)
        for r in range(len(nums)):
            if r-l+1 == k:
                n = nums[l]
                ans[l] = n
                for i in range(l+1, l + k):
                    if nums[i] <= ans[l]:
                        ans[l] = -1
                        break
                    elif nums[i] == ans[l] + 1:
                        ans[l] = nums[i]
                    else:
                        ans[l] = -1
                        break
                l += 1
        return ans[:l]
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