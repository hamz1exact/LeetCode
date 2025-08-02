# 20. Majority Element Il

Difficulty: Medium
Status: Mastred
Priority: High
Category: Array, Hashing
Link: https://neetcode.io/problems/majority-element-ii?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        hashmap ={}
        arr = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > target:
                arr.append(num)
                hashmap[num] = float('-inf')
        return arr

```

$$
Explaining
$$

```
We Count The Frequency of each number, if the freq sat to be greater than n / 3 we append it and we set the value of that number to be '-infinity'
to make sure that we do not append that value twice. 
NOTE: I used this O(n)Space O(n)Time instead of O(n) to avoid complexity
```