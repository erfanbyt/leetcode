# run time: O(n)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        target = []
        for i, num in zip(index, nums):
            target.insert(i, num)  # first argument is for poistion and the second on is the value

        return target
