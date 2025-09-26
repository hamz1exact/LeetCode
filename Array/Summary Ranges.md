# 228. Summary Ranges

Link: https://leetcode.com/problems/summary-ranges/submissions/1709752564/
Difficulty: Easy
Status: Need to be reviewed
Patterns: Iteration
Priority: Medium
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)
Created time: July 24, 2025 2:40 PM

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
i Undertand it
```

$$
Stuck-Point
$$

```
i get stuck at th point where we should app end the number alone without any pointers, and where we should append it with its pointer,
the idea was if start wasn't point to the number that was pointing to it earlier so we had some changes, otherways nothing change and
we simple append the number by it self.
```