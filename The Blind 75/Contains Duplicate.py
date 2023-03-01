class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {}
        for i in nums:
            if i in table:
                return True
            table[i] = True
        return False
