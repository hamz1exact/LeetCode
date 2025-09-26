# 1475. Final Prices With a Special Discount in a Shop

Difficulty: Easy
Status: Mastred
Priority: Low
Topic: Stack
Time Complexity: O(n²)
Space Complexity: O(n)
Created time: August 21, 2025 12:51 PM
Solved by my own: True

$$
Solution
$$

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = list(prices)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    arr[i] = prices[i] - prices[j]
                    break
        return arr
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