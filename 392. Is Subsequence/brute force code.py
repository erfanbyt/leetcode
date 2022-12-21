# run time: O(n)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointer_s = 0
        pointer_t = 0

        if len(s) == 0:  # this is an extra condition, if remove it, run time on leetcode will be much faster
            return True

        while pointer_t < len(t) and pointer_s < len(s):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1
                pointer_t += 1
            else:
                pointer_t += 1

        if pointer_s == len(s):
            return True
        

        return False

        
