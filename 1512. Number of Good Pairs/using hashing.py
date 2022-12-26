# run time: O(n)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        nums_index = {}
        counter = 0

        for i in nums:
            if i in nums_index:
                nums_index[i] += 1
                counter += nums_index[i]

            else:
                nums_index[i] = 0

        return counter
