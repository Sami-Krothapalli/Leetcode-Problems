class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Sorts the List First then compares the value with next value in the list if they are the same then it will return true if not then it will return false
        nums.sort() ## Sorting is a function that is O(n Log n)
        for i in range(len(nums) - 1): #Operation of O(n)
            if nums[i] == nums[i+1]:
                return True
        return False

#Time Complexity: O(n log n)
