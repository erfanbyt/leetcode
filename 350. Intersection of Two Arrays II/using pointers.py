# in this approach, both lists must be sorted
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        intersection_list = []
        nums1.sort()
        nums2.sort()

        pointer_n1 = 0
        pointer_n2 = 0

        while pointer_n2 < len(nums2) and pointer_n1 < len(nums1):
            if nums1[pointer_n1] < nums2[pointer_n2]:
                pointer_n1 += 1
            elif nums1[pointer_n1] > nums2[pointer_n2]:
                pointer_n2 += 1
            elif nums1[pointer_n1] == nums2[pointer_n2]:
                intersection_list.append(nums1[pointer_n1])
                pointer_n1 += 1
                pointer_n2 += 1

        return intersection_list
