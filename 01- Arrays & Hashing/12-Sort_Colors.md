# 12. Sort Colors

Difficulty: Medium
Status: Mastred
Priority: High
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: Null
Link: https://neetcode.io/problems/sort-colors?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, m, r = 0, 0, len(nums) - 1
        while m <= r:
            if nums[m] == 0:
                nums[m] , nums[l] = nums[l], nums[m]
                l+=1
                m +=1
            elif nums[m]== 1:
                m+=1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r-=1
        
```

$$
Idea
$$

```
for this problem, we used dutch flag algorithm that was introduced by djikstra.
```