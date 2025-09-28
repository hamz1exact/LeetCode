# 1920. Build Array from Permutation

Difficulty: Easy
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[nums[i]]
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