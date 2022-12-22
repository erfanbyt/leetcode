# run time: O(n)
# space: O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result = []
        max_candies = max(candies)

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result
