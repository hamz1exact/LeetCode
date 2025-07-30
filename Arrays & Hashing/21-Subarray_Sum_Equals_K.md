# 21. Subarray Sum Equals K

Difficulty: Medium
Status: Practicing
Priority: High
Category: Array, Hashing
Link: https://neetcode.io/problems/subarray-sum-equals-k?list=neetcode250

$$
Solution
$$

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {
            0:1
        }
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum - k in seen : # means if prefix_sum - k in keys
                count+=seen[prefix_sum - k]
            seen[prefix_sum] = seen.get(prefix_sum, 0)+1
        return count
```

$$
Explaining
$$

```
We Store all prefix sums in a hash map, if we substract the current prefix sum from k and we get a valid value, means we can find that value in the hashmap, for example 3 - 3 = 0, 0 found in the hashmap, we add the seen[0] to count means count = 1 now, so on until we find all subarrays.
this is the complement method, where we use that equation to find subarrays
for example if we have this array [1,-1, 1 ,1] and k = 3, at the first iteration we have 1 : 1 in the hashmap, second iteration 1 - 1 = 0 so we increment 0 to be 0:2, 1 - 1 + 1 = 1, 1 already in hashmap so we increment it now, 0:2, 1:2, 1-1+1+1 = 3 and 3 - 3 = 0 so total now is added to seen[0] which is 2, means we have only to valid subarrays [1, -1, 1] and [-1, 1, 1]
```
