# 8. Majority Element

Difficulty: Easy
Status: Mastred
Priority: High
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/majority-element?list=neetcode250

$$
Solution
$$

```python
# Boyer-Moore Voting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentNum, count = 0, 0
        for num in nums:
            if count == 0:
                currentNum = num
            count += (1 if num == currentNum else -1 )
        return currentNum
```

$$
Idea
$$

We used [Boyer-Moore Voting Algorithm](https://www.notion.so/Boyer-Moore-Voting-Algorithm-2394eb3001c080608e1bfef12fa2cf2d?pvs=21) In This Problem

- Keep a **currentNum** and a **count**.
- If the count is 0, choose the current number as the **currentNum**.
- If the number is the same as the **currentNum**, increment the count.
- If it’s different, decrement the count.

at the end if there is any **majority element** count would end up greater than 0 at this time we return the **currentNum**