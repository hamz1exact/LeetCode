# 7. Remove Element

Difficulty: Easy
Status: Mastred
Priority: Medium
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/remove-element?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
```

$$
Idea
$$

`Input: nums = [1,1,2,3,4], val = 1`

`Output: [2,3,4]` 

the idea is we initialize a variable K to track the unique elements, we increment this K only if the current number from the nums list is not equal to val which means its unique, for example we have the following input [1, 1, 2, 3, 4] and we want to remove all ones, so becuase at the first 2 iterations nums[i] is equal to val we would not incremene K so K stays at 0, once we arrive at the index 2 which is number 2,

we set nums[k] which is [0] to be nums [i] which is 2 → nums[0] = nums[2] so the edited array now is [2, 1, 2 ,3, 4,], we keep doing the same approach until we we get this results [2, 3, 4, 3, 4] but we need the first K elements which is the first 3 elements [2, 3, 4] and we return K value (3).