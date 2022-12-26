# run time: O(n)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        dict_ = {}
        for j in jewels:
            dict_[j] = 0

        for s in stones:
            if s in dict_:
                dict_[s] += 1

        return sum(dict_.values())
