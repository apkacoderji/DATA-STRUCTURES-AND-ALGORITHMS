class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        first = float('inf')
        last = float('-inf')
        
        while low <= high:
             
            mid = (low+high)//2

            if nums[mid] == target:
                first = min(first,mid)
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = len(nums)-1

        while low <= high:
             
            mid = (low+high)//2

            if nums[mid] == target:
                last = max(last,mid)
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                  
        return [first,last] if first != float('inf') and last != float('-inf') else [-1,-1]
        