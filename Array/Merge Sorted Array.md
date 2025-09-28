# 56. Merge Intervals

Link: https://leetcode.com/problems/merge-intervals/submissions/1709690892/
Difficulty: Medium
Patterns: Indexing, Iteration, Sorting
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(n)

$$
Solution
$$

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda interval: interval[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
```

$$
Explaining
$$

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

Explaining:

```
1- First We sort the array based on the start interval which is interval[0]
2- we create a empty merged array
3- we start iterate over each interval in the intervals, if the merged arr empty we immediatly append the current interval, or if the 
	 end of the last merged interval less than the start of the current interval from intervals.
4- otherways we edit the merged array, we edit the start to be the min start interval among 
	 the merged and the normal interval and we edit the end to be the max as among them as well 
	 
```

$$
Stuck-Point
$$

```
i get stuck at the idea of where should i store the current interval? by using left and right pointer you do not know which one u must append at the merged array, but the correct idea was appending the first interval then work with the others, if no nothing should be 
changed, append the current interval
```