# 122. Best Time to Buy and Sell Stock II

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Difficulty: Medium
Status: Mastred
Patterns: Fast & Slow Pointer, Sliding Window
Priority: High
Topic: Array
Time Complexity: O(n)
Space Complexity: O(1)
Created time: July 5, 2025 11:39 PM

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        left = 0
        profit = 0
        prev = 0
        sell = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
                sell = profit
                prev = 0
            elif prices[left] < prices[right] and  prices[right] > prev:
                profit =  prices[right] - prices[left] + sell
                prev = prices[right]
            else:
                left = right
                sell = profit
                prev = 0
        return profit
```