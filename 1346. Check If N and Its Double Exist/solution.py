# run time: O(n)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in arr:
            if i*2 in arr:
                if i != 0:
                    return True
                if i == 0:
                    arr.remove(0)
                    if 0 in arr:
                        return True

        return False
