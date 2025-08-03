# 14. 3Sum Closest

Difficulty: Medium

[Problem Link](https://leetcode.com/problems/3sum-closest/description/)

$$
Solution
$$

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # Check how close this sum is to the target
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    # Exact match
                    return target
        return closest_sum
```

$$
Explaining
$$

```
* Step1: We Sort The Array to get known how we should move our Pointers
* Step2: Set Initial Variable called closest_sum to start with
* Step3: Check Which one is close
* Step4: increment the PTRs based on the followed conditions.

```

$$
Stuck-Point
$$

```
* at the first loop we do not have anything to compare with, the trick was
  compare with the abs(infinit - target)
```