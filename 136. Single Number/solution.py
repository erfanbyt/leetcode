class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
        for n in nums:
            if n not in res:
                res.append(n)
            else:
                res.remove(n)

        return res[0]
