class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_str = ''

        for c in s:
            if c.isalnum():
                new_str += c.lower()

        return new_str[::-1] == new_str
        
    
