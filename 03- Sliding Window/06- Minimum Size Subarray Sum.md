# 6. Minimum Size Subarray Sum

Difficulty: Medium

[Problem Link](https://neetcode.io/problems/minimum-size-subarray-sum?list=neetcode250)

$$
The Problem
$$

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a subarray whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

$$
Example
$$

```markdown
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

$$
Solution
$$

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        curr_sum = 0
        minlen = float('inf')
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                minlen = min(minlen, right - left + 1)
                curr_sum -= nums[left]
                left +=1
            right += 1
        return 0 if minlen == float('inf') else minlen
```

$$
Explaining
$$

```markdown
# Once We Get The Target or Greater we Calc the length and we substract left then shrink by incrementing the left ptr.
```

$$
Stuck-Point
$$

```markdown
Null
```