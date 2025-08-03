# 5. Permutation In String

Difficulty: `Medium`

[Problem Link ](https://neetcode.io/problems/permutation-string?list=neetcode150)

$$
The Problem
$$

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

$$
Example
$$

```markdown
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

$$
Solution
$$

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        n1Count = [0] * 26
        n2Count = [0] * 26
        for i in range (n1):
            n1Count[ord(s1[i])-ord('a')] += 1
            n2Count[ord(s2[i])-ord('a')] += 1
        if n1Count == n2Count:
            return True
        for i in range(n1, n2):
            n2Count[ord(s2[i])-ord('a')] +=1
            n2Count[ord(s2[i-n1])-ord('a')] -=1
            if n2Count == n1Count:
                return True
        return False
```

$$
Explaining
$$
```
# To Achieve O(1) Solution We need to go thru these Steps:
>> Step 1: we need create 2 arrays both of length 26, why 26?
		 Because There Are 26 Characters in English.
>> Step 2: We need to fill these Arrays with the First n1 Characters
		That Characters Represented by the ORD of a given Character
		For Example Character "a" woule be presented as 1
		Because ORD('a') - ORd('a') + 1 = 97 - 97 + 1 = 1
		and ORD('b') == 2 so on.
>> Step 3: We Check if the first N1 Characters was in the order by Default

>> Step 4: Start at index (n1) because if they were equal at the first Check we will have returned True,
             Because They Were not we will start at index n1, and add the current char and 
             removing the old char by saying i - n1 which means if 
             n1 was 2 we calculate the first char by i at the 
             first loop is equal to n1 to i - n1 == 2 - 2 == 0,
             means give me  the ORD of the char at index (0)
```


$$
Stuck-Point
$$

```markdown
Null
```