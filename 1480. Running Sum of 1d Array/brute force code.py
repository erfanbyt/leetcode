# time complexity: O(n)
# space complexity: o(n)

def runningSum(self, nums: List[int]) -> List[int]:
    res = []
    sum_ = 0

    for number in nums:
        sum_ = sum_ + number
        res.append(sum_)

    return res
