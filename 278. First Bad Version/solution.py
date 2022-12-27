# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left_p = 1
        right_p = n

        while left_p <= right_p:
            mid_p = int((left_p + right_p)//2)
            if isBadVersion(mid_p):
                result = mid_p
                right_p = mid_p - 1
            elif isBadVersion(mid_p) == False:
                left_p = mid_p + 1
        
        return result

