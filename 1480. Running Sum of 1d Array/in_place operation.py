# this code does the operation in-place to save memory
# time_complexity: O(n)
# space_complexity: O(1)

def runningSum(self, nums: List[int]) -> List[int]:

    if len(nums) == 1:  # edge case to deal with inputs with one entry
        return nums

    pointer = 1
    while pointer <= len(nums) - 1:
        nums[pointer] = nums[pointer] + nums[pointer-1]
        pointer += 1

    return nums
