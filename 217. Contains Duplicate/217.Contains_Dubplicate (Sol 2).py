class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Set returns a list that has no duplicates in it
        nums_set = nums.set()
        # We simply check if the length of the nums_set and nums has changed if it does there is a duplicate if not then there wasnt
        if len(nums_set) != len(nums):
            return True
        else:
            return False

#Time Complexity: O(1)