# brute force approach for solving the problem.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict_ = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        for i in range(len(s)-1):
            
            if s[i] == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    res = res - dict_[s[i]]
                    continue
                else:
                    res += dict_[s[i]]
                    continue

            if s[i] == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    res = res - dict_[s[i]]
                    continue
                else:
                    res += dict_[s[i]]
                    continue

            if s[i] == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    res = res - dict_[s[i]]
                    continue
                else:
                    res += dict_[s[i]]
                    continue
            
            res += dict_[s[i]]


        return res


            


                
                

















