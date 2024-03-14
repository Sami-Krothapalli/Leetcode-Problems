class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            countS = {}
            countT = {}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True
        else:
            return False

#Time Complexity: O(n) = n = s

#Explanation: 
