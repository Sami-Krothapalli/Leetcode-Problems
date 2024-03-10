#Leetcode Link: https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #K is the pointer that will iterate through the list only if the numbers arent the value
        k = 0
        for i in range(len(nums)):
            #Checks if Nums[i] isnt the value if it isnt it will move the value to where index k is then it will increase k thus moving the pointer
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
#Time Complexity: O(N)


