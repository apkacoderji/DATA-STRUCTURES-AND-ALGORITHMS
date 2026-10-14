class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        low = 0
        n = len(nums)
        high = n - 1

        while low<=high:

            mid = (low+high)//2

            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[n-1]:
                low = mid + 1
            elif nums[mid] < nums[n-1]:
                high = mid - 1
        
        return nums[0]


        