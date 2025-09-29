# 33. Search in Rotated Sorted Array

Difficulty: Medium
Status: Mastred
Priority: High
Topic: Binary Search
Time Complexity: O(n)
Space Complexity: O(1)
Created time: September 29, 2025 1:34 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)- 1
        min_value = float('inf')
        while l <= r:
            mid = (r +l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if nums[l] < nums[mid] > nums[r]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            elif nums[l] > nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            if l < len(nums) and nums[l] == target:
                return l
            if l < len(nums) and nums[r] == target:
                return r
        return -1

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