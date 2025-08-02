# 14. Encode and Decode Strings

Difficulty: Medium
Status: Mastred
Priority: Low
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode250

$$
Solution
$$

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for string in strs:
            ans += str(len(string)) + "$" + string
        return ans
    def decode(self, s: str) -> List[str]:
        out = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "$":
                right+=1
            length = int(s[left:right])
            out.append(s[right+1:right+1+length])
            left = right + 1 + length
        return out
```

$$
Explaining
$$

```
step1: we loop over each string in strs list, and we convert it based on the following 
				process:
				- at the first of each work we add the length of that word followed by "$"
					this help use to determin from where the string will start and to where will it 
					end
step2: we set 2 pointers ( left and right ) and we will continue looping as long as left is less than the len of the coded string, the only work of right pointer is to track where the "$" begins. once we arrive at the symbol "$" means the next char is the first char of that X word, which tells us start recording this word X number of chars. and we can get that X no of chars based on the "$" sign because the number that was before "$" is repreneting the number of chars, and that number is where left reside, that's why the length is length = int(s[left:right]). 
```

$$
Stuck-Point-if -any!
$$

```
Null
```