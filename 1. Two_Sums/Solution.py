def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {} # int : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap: 
            return [hashmap[diff], i]
        else:
            hashmap[n] = i

#Time Complexity: O(N)
print(twoSum([2, 3, 1, 7], 4))