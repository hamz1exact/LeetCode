# 153. Find Minimum in Rotated Sorted Array

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Binary Search
Time Complexity: O(n)
Space Complexity: O(1)
Created time: September 29, 2025 1:37 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)- 1
        min_value = float('inf')
        while l <= r:
            mid = (r +l) // 2

            if nums[l] < nums[mid] > nums[r]:
                if abs(nums[mid] - nums[l]) < abs(nums[mid] - nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] > nums[mid] < nums[r]:
                if nums[l] > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r  = mid - 1

            min_value = min(min_value, nums[r], nums[l], nums[mid])
        return min_value
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