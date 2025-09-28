# 412. Fizz Buzz

Difficulty: Easy
Priority: Low
Topic: Math
Time Complexity: O(n)
Space Complexity: O(1)

$$
Solution
$$

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        k = 1
        while k <= n:
            if k % 3 == 0 and k % 5 ==0:
                ans.append('FizzBuzz')
            elif k % 3 == 0:
                ans.append('Fizz')
            elif k % 5  == 0:
                ans.append('Buzz')
            else:
                ans.append(str(k))
            k += 1
        return ans
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