# time complexity: O(n)
# space complexity: O(1)

def pivotIndex(self, nums: List[int]) -> int:
    total_sum = sum(nums) # O(n)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum

        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1
