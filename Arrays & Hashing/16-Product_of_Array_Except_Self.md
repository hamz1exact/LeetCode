# 16. Product of Array Except Self

Difficulty: Medium
Status: Practicing
Priority: Medium
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(1)
Link: https://neetcode.io/problems/range-sum-query-2d-immutable?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

```

$$
Explaining
$$

```python
Example 1:

Input: nums = [1,2,3,4]

Output: [24,12,8,6]
```

```
first we should make a prefix for the array except the last element and we can do that by writing output[1] * len(nums) this will give us [1, 1, 1, 1]

we start to iterate over the actual list of nums and we sit the first val to be 1 because we initialize the prefix to 1 and after that we product it by the number in index i from the arr ( prefix *= nums[i] ), we will end up by having this output

output = [1, 1, 2, 6], so the first step was done so far, the next step is doing the same approach but in reverse from end to start, but in this time we will product the current num from the output arr to the postfix and the postfix will be producted to the current num from nums, we will end up with this output = [24,12,8,6]

loop 1 : 6 * 1 = 6, postfix = 1 * 4
loop 2: 2 * 4 = 8, postfix = 4 * 3 = 12 
loop 3: 1 * 12 = 12, postfix = 2 * 12 = 24
loop 4: 1 * 24 = 24, postfix = 24 * 1
```