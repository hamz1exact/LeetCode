# 13. Top K Frequent Elements

Difficulty: Medium
Status: Mastred
Priority: High
Category: Array, Hashing
Time Complexity: O(n Log n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

$$
Python
$$

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```

$$
Explaining
$$

```
This Algorithms Runs in O(n log n).
step1: count the frequency of each number in the array
step1: append new arrays in form of [key, value] to new array (O(n) Space).
step3: sort the array in asc order 
step4: add K numbers of pops which represent the most frequent elements
```