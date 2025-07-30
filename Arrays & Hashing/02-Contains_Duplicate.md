# 2. Contains Duplicate

Difficulty: Easy
Status: Mastred
Priority: Low
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/duplicate-integer?list=neetcode150

$$
Solution1--O(n)
$$

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = []
        for num in nums:
            if num not in r:
                r.append(num)
            else:
                    return True
        return False
            
```

$$
Solution2 -O(1)
$$

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        left = 0
        for right in range(1,len(nums)):
            if nums[left] == nums[right]:
                return True
            left+=1
        return False
```

Memory Complexity: O(1)
Time Complexity: O(N log N)