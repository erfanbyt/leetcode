class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = []
        for pointer in range(1, len(num)-1):
            if num[pointer] == num[pointer-1] and num[pointer] == num[pointer+1]:
                nums = num[pointer-1] + num[pointer] + num[pointer+1]
                res.append(nums)


        if len(res) == 0:
            return ""
        else:
            return sorted(res, reverse=True)[0]
        
