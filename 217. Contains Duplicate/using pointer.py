def containsDuplicate(self, nums: List[int]) -> bool:

    nums = sorted(nums)

    right_pointer = 1
    left_pointer = 0

    if len(nums) == 1:
        return False

    while right_pointer <= len(nums) - 1:
        if nums[left_pointer] == nums[right_pointer]:
            return True

        left_pointer += 1
        right_pointer += 1

    return False
