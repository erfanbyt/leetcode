# run time: O(n)

class Solution:
    def largestOddNumber(self, num: str) -> str:

        pointer = len(num) - 1

        odd_num = []
        while pointer >= 0:
            if int(num[pointer]) % 2 != 0:
                odd_num = num[:pointer+1]
                break
            
            pointer -= 1

        return "".join(odd_num)
