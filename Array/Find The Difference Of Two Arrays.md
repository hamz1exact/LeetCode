# 2239. Find Closest Number to Zero

Link: https://leetcode.com/problems/find-closest-number-to-zero/description/
Difficulty: Easy
Status: Mastred
Patterns: Iteration
Priority: Low
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)
Created time: July 30, 2025 9:27 PM

$$
Solution
$$

```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums : 
            return abs(closest)
        else : 
            return closest
```

$$
Explaining
$$

```
We assume that the first number is the closest, and we keep iterate over each number in nums, if that number < closest number, we set closest to be num.
at the end of the loop, if the closest num was negative and its absolute value was in the arr for example the closest is -1 and 1 in the array, we return 1 otherwise we return the value even if its negative because its the closest one
```

$$
Stuck-Point
$$

```
Null
```