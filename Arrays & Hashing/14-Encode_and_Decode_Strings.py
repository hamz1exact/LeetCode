class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for string in strs:
            ans += str(len(string)) + $ + string
        return ans
    def decode(self, s: str) -> List[str]:
        out = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != $:
                right+=1
            length = int(s[left:right])
            out.append(s[right+1:right+1+length])
            left = right + 1 + length
        return out
