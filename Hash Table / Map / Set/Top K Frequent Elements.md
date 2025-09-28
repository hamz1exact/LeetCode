# 347. Top K Frequent Elements

Link: https://leetcode.com/problems/top-k-frequent-elements/description/
Difficulty: Medium
Patterns: Hashing, Sorting
Priority: High
Topic: Hash Table / Map / Set
Time Complexity: O(n Log n)
Space Complexity: O(n)

$$
My Solution:
$$

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        hashMap = {}
        arr = []
        for num in nums:
            if num in hashMap:
                hashMap[num] +=1
            else:
                hashMap[num] = 1
        for _ in range(k):
            max_key= max(hashMap, key = hashMap.get)
            arr.append(max_key)
            hashMap.pop(max_key)
        return arr
```

> The Problem with my solution that it runs in O(n²) Time Complexity
> 

$$
Fixed-Clean-Version
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

1st Loop: We Count Frequencies

2ed Loop: we append keys and values into an array, then sort it.

→ we sort the arr at the end

3rd loop: we pop the element that has [1] index from the arr and put it into new array.

`Time Complexity (n log n)`