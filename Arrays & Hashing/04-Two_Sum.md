# 04. Two Sum

Difficulty: Easy
Status: Mastred
Priority: Medium
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: Null
Link: https://neetcode.io/problems/two-integer-sum?list=neetcode150

$$
Solution1--Iteration
$$

```python
def twoSum(nums, target):
  left = 0
  right =  len(nums)-1
  while left < right:
    if nums[left] + nums[right] > target :
      right-=1
    elif nums[left] + nums[right] < target:
      left+=1
    else:
      return [left, right]
  return -1

# In Order This Algorithm to work, the input should be sorted.
```

$$
Idea
$$

We add Left Number to right number, if the sum is greater than the actual target, we decrease the right val by one, but if it smaller we increase the left val by one.

we return -1 if there is no valid sum to the target

$$
Solution2--Hashing
$$

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            calc = target - nums[i]
            if calc in seen:
                return [seen[calc], i]
            seen[nums[i]] = i
```

$$
Idea
$$

in Each Iteration We store the  value that we need to make the sum valid in a hash Map called Seen, for example in the first iteration we store taget - nums[i] where i is equal to 0 , for example if we used this array [3,4,5,6] and target == 7, the first stores value in the hashMap would be 7 - 3 which is 4.

if this 4 found in the hashMap we return its index and the current index, in the first iteration we did not find 4 in the hashMap so we store the current Num in the hashMap seem[3] = 0

in the second iteration we calculate the needed value to sum up to the target which is 7 - 4 = 3, we check if 3 in the hashMap and yes we find it because we stored it in the first iteration, so we return the index of it by writing seen[calc] which is seen[3] and the current index which is 1, so the output [0, 1].

the equation is 3 = 7 - 4 so 7 = 3 + 4 [0, 1]