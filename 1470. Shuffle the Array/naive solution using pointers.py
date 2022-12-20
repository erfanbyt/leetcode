# time complexity: O(n)

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0]*len(nums)
        r = n #rigth pointer
        l = 0 # left pointer
        k = 0 # pointer on res
        while r < 2*n:
            res[k] = nums[l] 
            res[k+1] = nums[r]
            k += 2
            r += 1
            l += 1

        return res

        
