# 22. First Missing Positive

Difficulty: Hard
Status: Not Started
Priority: High
Category: Array, Hashing
Link: https://neetcode.io/problems/first-missing-positive?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
            if not 1 in nums or not nums:
                return 1
            n = len(nums)
            for i in range(n):
                if nums[i] > n or nums[i] < 1:
                    nums[i] = 1
            for j in range(n):
                var = nums[abs(nums[j])-1]
                if var > 0:
                    nums[abs(nums[j]) - 1] *= -1
            for k in range(n):
                if nums[k] > 0:
                    return k + 1
            return n + 1
```

$$
Explaining
$$

```
Step1: we set each number that greater than the length of the array or equal to or smaller than 0, to prevent index error
Step2: we substract one from the current number from the array and we see if its the index in its absolute value is greater than 0, if so we flip it to be negative by multiplying it by -1
Step3: we check if there any positive number left in the array we return its index + 1, if not we return the length of the array + 1 means there is no missing positive number in the arr
       but its outside the array so we return the very first number after the array, and we include the edge case which said if not nums or if 1 in nums return 1 immedialty. 
```