class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return False
        lookup = {}
        
        for num in nums:
            lookup[num] = lookup.get(num, 0) +1
            if lookup[num] > 1 :
                return True
        return False
