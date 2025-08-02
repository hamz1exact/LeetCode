# 6, Remove Duplicates From Sorted Array

Difficulty: Easy
Status: Not Started
Priority: Medium
Link: https://neetcode.io/problems/remove-duplicates-from-sorted-array?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
        return slow+1
```

$$
Explaining
$$

```
we increment slow if slow != fast, we increment before swapping the values, actually not swapping but set slow to be fast in nums
```