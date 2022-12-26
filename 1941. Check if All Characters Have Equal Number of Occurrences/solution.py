# run time: O(n)

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        dict_ = {}

        for char in s:
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 0
        

        return len(set(dict_.values())) == 1
