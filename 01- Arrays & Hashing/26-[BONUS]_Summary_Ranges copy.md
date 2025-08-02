# 29. Merge Strings Alternately
Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Status: Mastred
Patterns: Indexing
Priority: Low
Topic: Array 
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i+=1
            
            if start != nums[i]:

                ans.append(f'{start}->{nums[i]}')
            
            else:
                ans.append(f'{nums[i]}')
            
            i+=1
        return ans
```

$$
Explaining
$$

```
We always start with set start variable to nums[i], if there is a sequence the while loop will executed and start will no longer be equal to nums[i] so we will append in this way [start -> end], but if the loop doesn't executed means there was no sequence and we append the number alone
```

$$
Stuck-Point
$$

```
Null
```