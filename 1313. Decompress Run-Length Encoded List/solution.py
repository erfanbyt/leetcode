# run time: O(n)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        freq_pointer = 0
        val_pointer = 1
        result = []

        while val_pointer < len(nums):
            result += nums[freq_pointer]*[nums[val_pointer]]
            freq_pointer += 2
            val_pointer += 2

        return result
