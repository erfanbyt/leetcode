# faster than 100% of codes in leetcode

class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        prev = 0

        for item in s.split():
            if item.isdigit():
                if int(item) <= prev:
                    return False

                prev = int(item)  

        return True

