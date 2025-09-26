# 16. 3Sum Closest

Link: https://leetcode.com/problems/3sum-closest/
Difficulty: Medium
Status: Need to be reviewed
Patterns: Two Pointers
Priority: High
Topic: Array
Time Complexity: O(n Log n)
Space Complexity: O(1)
Created time: August 9, 2025 5:38 PM

$$
Solution
$$

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step1: Sort
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    return closest

        return closest 
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