# run time: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_rep = {}

        for char in s:
            if char in char_rep:
                char_rep[char] += 1
            else:
                char_rep[char] = 1

        sum_ = 0
        condition = False
        for val in char_rep.values():
            if val % 2 == 1:
                sum_ += val-1
                condition = True
            else:
                sum_ += val
            

        if condition:
            return sum_ + 1
        else:
            return sum_
