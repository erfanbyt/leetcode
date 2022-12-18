# This approach exceeds the time limit on the leetcode server

# time complexity: O(n^2) --> doing iteration on each element and calculating sum at each iteration
# space complexity: O(n)



def pivotIndex(self, nums: List[int]) -> int:

    for pointer in range(len(nums)):
        left_sum = 0
        right_sum = 0

        left_sum += sum(nums[:pointer])
        right_sum += sum(nums[pointer+1:])

        if left_sum == right_sum:
            return pointer


    return -1
