    # this solution is using hashset method. 
    # time complexity: O(n)
    # space complexity: O(n)
    
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)


        return False
