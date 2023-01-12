class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1

        slow_p = 0 
        fast_p = 1

        while fast_p < len(nums):
            if nums[slow_p] == nums[fast_p]:
                fast_p += 1
            else:
                slow_p += 1
                nums[slow_p] = nums[fast_p]
                fast_p += 1

        return slow_p + 1
