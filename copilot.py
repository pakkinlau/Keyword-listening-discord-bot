class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num == 0:
            return 0
        
        bitmask = 1
        steps = 0
        
        while bitmask <= num:
            if bitmask & num == 0:
                steps += 1
            else:
                steps += 2
            bitmask = bitmask << 1
        return steps - 1 
        
    
s = Solution()
A = s.numberOfSteps(14)
print(A)
