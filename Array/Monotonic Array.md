# 896. Monotonic Array

Difficulty: Easy
Status: Mastred
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 10, 2025 2:30 AM

$$
Solution
$$

```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if decreasing:
                    return False
                increasing = True
            elif nums[i] < nums[i+1]:
                if increasing:
                    return False
                decreasing = True
            else:
                continue
        return True

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