# time complexity: O(n^3) --> n^2 because of 2 loops and it times with O(n) because of sum operation over it 


def maxSubArray(self, nums: List[int]) -> int:

    max_sum = float('-inf')
    for i in range(len(nums)+1):
        for j in range(i+1, len(nums)+1):
            # print((i, j))
            # print(nums[i:j])
            temp_nums = nums[i:j]
            sum_ = sum(temp_nums)
            if sum_ >= max_sum:
                max_sum = sum_

    return max_sum
