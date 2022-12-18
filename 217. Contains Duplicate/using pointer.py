# using 2 pointers on a sorted list
# time complexity: O(nlog n) --> come from the sorting algo.
# space complexity: O(1) --> it is done in-place

def containsDuplicate(self, nums: List[int]) -> bool:

    nums = sorted(nums)

    right_pointer = 1
    left_pointer = 0

    if len(nums) == 1:  # to deal with the edge case of only one element
        return False

    while right_pointer <= len(nums) - 1:
        if nums[left_pointer] == nums[right_pointer]:
            return True

        left_pointer += 1
        right_pointer += 1

    return False
