# 74. Search a 2D Matrix

Difficulty: Medium
Status: Mastred
Priority: Medium
Topic: Binary Search
Time Complexity: O(n)
Space Complexity: O(1)
Created time: September 28, 2025 11:58 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for nums in matrix:
            if nums[0] <= target <= nums[len(nums)-1]:
                if self.search(nums, target):
                    return True
        return False

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
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