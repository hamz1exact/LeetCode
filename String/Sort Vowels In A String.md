# 80. Remove Duplicates from Sorted Array II

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Difficulty: Medium
Patterns: Fast & Slow Pointer, Two Pointers
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)

Source Code:

```python
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        slow = 2
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
	                slow+=1
	       return slow
```