# be careful to consider the edge case when the frist element of n2 is smaller than first element of n1


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        pointer_n1 = m - 1
        pointer_n2 = n - 1 
        insert_pointer = m + n - 1

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            

        while pointer_n1 >= 0 and pointer_n2 >= 0:
            if nums1[pointer_n1] >= nums2[pointer_n2]:
                nums1[insert_pointer] = nums1[pointer_n1]
                pointer_n1 -= 1
                insert_pointer -= 1
            else:
                nums1[insert_pointer] = nums2[pointer_n2]
                pointer_n2 -= 1
                insert_pointer -= 1

        while pointer_n2 >=0 and insert_pointer >= 0:  # this loop is to consider the edge case
            nums1[insert_pointer] = nums2[pointer_n2]
            insert_pointer -= 1
            pointer_n2 -= 1


        return 



