class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverse(start,end):
            nums[start:end] = nums[start:end][::-1]
        
        k = k % n
        reverse(0,n)
        reverse(0,k)
        reverse(k,n)

        





        