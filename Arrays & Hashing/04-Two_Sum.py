class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            calc = target - nums[i]
            if calc in seen:
                return [seen[calc], i]
            seen[nums[i]] = i
