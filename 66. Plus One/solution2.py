class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str_num = [str(i) for i in digits]
        num = str(int("".join(str_num)) + 1)
        list_num = [int(s) for s in num]
        # print(list_num)

        return list_num
 
