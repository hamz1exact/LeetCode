# 6. Group Anagrams

Difficulty: Medium
Status: Mastred
Priority: High
Category: Array, Hashing
Time Complexity: O(n)
Space Complexity: O(n)
Link: https://neetcode.io/problems/anagram-groups?list=neetcode150

$$
Solution --Hashing
$$

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())

```

$$
Idea
$$

input: ["eat","tea","tan","ate","nat","bat"]

output: [["bat"],["nat","tan"],["ate","eat","tea"]]

The Idea is really Simple:

we initilaze a hashmap called groups (groups = {})

we iterate over each word in the strs list (for word in strs)

we initialize a universal key which is a sorted word and we say if the key in the hashmap we append the the unsorted word to it because its from the group, but if the key was not in the group we initialize a new group for it and we store the current word in a new list.

once we complete the last iteration we return the values we stored in the hashMap in form of list to match the expected output