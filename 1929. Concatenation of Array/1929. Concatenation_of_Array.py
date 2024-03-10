# Leetcode Link: https://leetcode.com/problems/concatenation-of-array/description/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        #Copies the List twice and then assigns it to ans
        ans = nums * 2
        return ans

#Time Complexity: O(1)