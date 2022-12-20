class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        import numpy 

        return max(numpy.sum(accounts, axis=1))
