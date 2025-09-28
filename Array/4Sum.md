# 18. 4Sum

Link: https://leetcode.com/problems/4sum/
Difficulty: Medium
Patterns: TreePointers, Two Pointers
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            for j in range(index+1, len(nums)):
                if j > index + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    foursum = num + nums[j] + nums[l] + nums[r]
                    if foursum > target:
                        r -=1
                    elif foursum < target:
                        l += 1 
                    else:
                        arr.append([num, nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l +=1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return arr

```

$$
Explaining
$$

```

```

$$
Stuck-Point
$$

```markdown
# HOW TO PREVENT DUPLICATES

```