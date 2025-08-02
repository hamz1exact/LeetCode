# 10. Rotate Array

Difficulty: Medium

Status: Mastred

Priority: High

Link: https://neetcode.io/problems/rotate-array?list=neetcode250

$$
The Problem
$$

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

$$
Example
$$

```markdown
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

$$
Solution
$$

```python
class Solution(object):
    def rotate(self, nums, k):
        if not nums or k == 0:
            return
        
        # If k is bigger than array length, we only need k % len(nums) rotations
        k = k % len(nums)
        
        # Simple approach: take last k elements and put them at the front
        nums[:] = nums[-k:] + nums[:-k]
        return nums
```

$$
Explaining
$$

```markdown
# Simple approach: take last k elements and put them at the front
```

$$
Stuck-Point
$$

```markdown
Null
```