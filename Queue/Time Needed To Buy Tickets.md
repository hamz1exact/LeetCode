# 1701. Average Waiting Time

Difficulty: Medium
Priority: Low
Topic: intervals
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        calc, total = 0, 0
        for c in customers:
            end  = c[1]
            calc = end + max(c[0], calc)
            # print(calc)
            total += (calc - c[0])
        return total / len(customers)
```

$$
Explaining
$$

```

```

$$
Stuck-Point
$$

```

```