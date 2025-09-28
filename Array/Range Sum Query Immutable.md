# 303. Range Sum Query - Immutable

Link: https://leetcode.com/problems/range-sum-query-immutable/description/
Difficulty: Easy
Patterns: Prefix Sum
Priority: Medium
Topic: Array
Time Complexity: O(n) O(1)
Space Complexity: O(1)

```python
Problem Solution:
class NumArray:

    def __init__(self, nums: List[int]):
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        left_sum = 0 
        if left > 0:
            left_sum = self.prefix[left-1]
        
        return self.prefix[right] - left_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```