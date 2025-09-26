# 2264. Largest 3-Same-Digit Number in String

Difficulty: Easy
Status: Mastred
Priority: High
Topic: String
Time Complexity: O(n)
Space Complexity: O(1)
Created time: August 10, 2025 2:32 AM

$$
Solution
$$

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxNum = float('-inf')
        if len(num) == 3:
            if num[0] == num[1] == num[2]:
                return str(num[0:]) 
        maxStr = ""
        strs = num
        k = 3
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if int(num[i:k]) > maxNum:
                    maxStr = str(num[i:k]) 
                    maxNum = int(num[i:k])
            k+=1
        return maxStr
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