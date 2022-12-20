# time complexity: O(n) 
# space complexity: O(1)

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_values = {}

        for i, value in enumerate(nums):
            remaining = target - value

            if remaining in seen_values:
                return [i, seen_values[remaining]]

            seen_values[value] = i
