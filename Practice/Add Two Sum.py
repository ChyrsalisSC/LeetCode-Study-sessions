class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_values = {}
        for i in range(len(nums)):
            value = target - nums[i] 
            if value in old_values:
                return [old_values[value], i]
            else:
                old_values[nums[i]] = i
