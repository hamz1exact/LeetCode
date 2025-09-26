# 136. Single Number

Link: https://leetcode.com/problems/single-number/description/
Difficulty: Easy
Status: Mastred
Patterns: Sorting, Two Pointers
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: None
Created time: July 29, 2025 8:02 PM

$$
Solution
$$

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = 1
        nums.sort()
        while right < len(nums):
            if nums[left] != nums[right]:
                return nums[left]
            left +=2
            right+=2
        return nums[left]
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