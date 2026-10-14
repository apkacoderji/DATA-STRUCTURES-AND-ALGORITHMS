class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 0
        high = len(arr) - 1
        res = 0


        while low<=high:

            mid = (low+high)//2

            if arr[mid] > arr[mid+1]:
                high  = mid - 1
                res =  mid
            
            else:
                low = mid + 1

        return res



        