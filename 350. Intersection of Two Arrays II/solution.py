# time complexity: O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection_list = []

        for n in nums1:
            if n in nums2:
                intersection_list.append(n)
                nums2.remove(n)

        return intersection_list
