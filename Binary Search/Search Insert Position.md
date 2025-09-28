# 35. Search Insert Position

Difficulty: Easy
Priority: Low
Topic: Binary Search
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        min_index = float('inf')
        min_diff = float('inf')
        min_num = float('inf')
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

            if abs(abs(target) - nums[right]) < min_diff:
                mind_diff = abs(abs(target) - nums[right])
                min_num = nums[right]
                min_index = right
            elif abs(abs(target) - nums[left]) < min_diff:
                mind_diff = abs(abs(target) - nums[left])
                min_num = nums[left]
                min_index = left
            else:
                mind_diff = abs(abs(target) - nums[left])
                min_num = min(nums[left], nums[right])
                min_index = min(left, right)

        mid = min_index if min_index >= 0 else 0
        
        if mid == 0 and target > nums[mid]:
            return mid + 1
        elif mid == 0 and target < nums[mid]:
            return 0

        elif target > nums[mid]:
            return mid + 1
        else:
            return mid - 1

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