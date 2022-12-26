# run time: O(n)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        res = 0
        J = set(jewels)
        for s in stones:
            if s in J:
                res += 1
        return res
