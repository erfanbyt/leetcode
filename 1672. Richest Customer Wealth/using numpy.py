# this would be the most efficient solution is numpy was already installed, but on leetcode server it was not fast enough!

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        import numpy 

        return max(numpy.sum(accounts, axis=1))
