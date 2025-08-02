# 1. Contains Duplicate Il

Difficulty: Easy

Status: Mastred

Priority: Medium

Link: https://neetcode.io/problems/contains-duplicate-ii?list=neetcode250

$$
The Problem
$$

`Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k`

$$
Example
$$

`nums = [1,2,3,1], k = 3` 
`Output: true`

$$
Solution
$$

```python
# Solution No 1
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2  or k == 0: return False
        i, j = 0, 0
        s = set()
        while j < len(nums):
            if abs(i - j) <= k:
                if nums[j] in s:
                    return True
                s.add(nums[j])
                j += 1
            else:
                s.remove(nums[i])
                i+=1
        return False
        
# Solution No 2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False
```

$$
Explaining
$$

```markdown
# Solution 1:
We Keep Adding Values As long as we did not contain K values
If The Duplicate number is in the arr, it would be found in that range
abs(i - j) <= k 
# Solution 2 (better): 
storing the value in a hashmap coupled with its value.
if the value found in the hashmap and the current index - its index 

```

$$
Stuck-Point
$$

```markdown
Null
```