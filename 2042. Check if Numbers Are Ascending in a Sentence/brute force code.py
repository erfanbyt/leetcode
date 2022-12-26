class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        res = []
        for item in s.split():
            if item.isdigit():
                res.append(int(item))

        def check_ascending(nums):
            pointer = 1
            while pointer < len(nums):
                if not nums[pointer-1] < nums[pointer]:
                    return False
                
                pointer += 1
            
            return True

        return check_ascending(res)

