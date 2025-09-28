# 1052. Grumpy Bookstore Owner

Difficulty: Medium
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        sat = 0
        exsat = 0
        maxS = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sat += customers[i]
        for r in range(len(customers)):
            exsat += (customers[r] if grumpy[r] == 1 else 0)
            if r - l + 1 == minutes:
                maxS = max(maxS, exsat)
                exsat -= (customers[l] if grumpy[l] == 1 else 0)
                l += 1
        return sat+maxS
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