# run time: O(nlogn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_p = 0
        right_p = len(nums) - 1

        while left_p <= right_p:
            mid_p = int((left_p + right_p) // 2)
            
            if nums[mid_p] == target:
                return mid_p
            elif nums[mid_p] < target:
                left_p = mid_p + 1
            elif nums[mid_p] > target:
                right_p = mid_p - 1

        return -1
