# Solution for this problem can be done with dynamic programming

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        num1 = 1
        num2 = 1
        c = 1

        while c < n:
            temp = num2
            num2 = num1 + num2
            num1 = temp
            c += 1
        return num2
