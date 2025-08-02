## 2. Best Time to Buy And Sell Stock

Difficulty: Easy

Link: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150

$$
The Problem
$$

**You are given an integer array** `prices` **where** `prices[i]` **is the price of NeetCoin on the** `ith` **day.**

**You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.**

**Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be `0`.**

$$
Example
$$

```markdown
Input: prices = [10,1,5,6,7,1]

Output: 6
```

$$
Solution
$$

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1: return 0
        left = 0
        profit = 0
        for right in range(len(prices)):
            if prices[left] >  prices[right]:
                left = right
            elif prices[left] < prices[right]:
                profit = max(profit, prices[right] -  prices[left])
        return profit
```

$$
Explaining
$$

```markdown
# Buy Every Rally, Return The Max Rally
```

$$
Stuck-Point
$$

```markdown
Null
```