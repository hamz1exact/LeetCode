# 18. Longest Consecutive Sequence

Difficulty: Medium
Status: Practicing
Priority: Medium
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(1)
Link: https://neetcode.io/practice#:~:text=Longest%20Consecutive%20Sequence

$$
Solution
$$

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        c = 0
        max_c = 0
        for num in nums:
            if num - 1 not in nums:
                c = 0
                while c + num in nums:
                    c +=1
            max_c = max(max_c, c)
        return max_c
```

$$
Explaining
$$

```
Input: 
			nums =[100,4,200,1,3,2]
output: 
			4
			
			
* Approach: we convert that array into set, and initialize two variables c (count) and max_c (max_count)
* We iterate over each number in the set, if number - 1 not in that set, means that number is the root in its collection, otherwise there is somenumber before it and we need to find it,
at this example 100, 200 and 1 were the root, but non of them achieve the while loop except 1, so we say if num + count in the set we increment count, which means we are in sequence of numbers, so the first loop we had, 1 + 0 = 1, 1 + 1 = 2, 1 + 2 = 3, 1 + 3 = 4, 1 + 4 = 5 at this point 5 was not in the set so we stop the loop and count now is 4 which is the longest sequence among all others.
```

$$
Stuck-Point
$$

```
NULL
```