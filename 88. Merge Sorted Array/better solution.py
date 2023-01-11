# this solution is checking less conditons for solving the problem and is faster.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        pointer_n1 = m-1
        pointer_n2 = n-1
        insert_pointer = m+n-1

        while pointer_n1 >=0 and pointer_n2 >=0:

            if nums1[pointer_n1] >= nums2[pointer_n2]:
                nums1[insert_pointer] = nums1[pointer_n1]
                pointer_n1 -= 1
                insert_pointer -= 1

            else:
                nums1[insert_pointer] = nums2[pointer_n2]
                pointer_n2 -= 1
                insert_pointer -= 1

        if pointer_n2 >= 0:
            nums1[:insert_pointer+1] = nums2[:pointer_n2+1]

        return nums1




