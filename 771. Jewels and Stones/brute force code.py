# run time: o(n^2)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counter = 0
        for j in jewels:
            for s in stones:
                
                if j == s:
                    counter += 1


        return counter 
