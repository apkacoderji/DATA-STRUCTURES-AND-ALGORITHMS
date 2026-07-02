class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = minsum = maxsum = currmax = currmin = nums[0]
        
        n = len(nums)

        totalsum = 0
        for num in nums:
            totalsum += num


        for i in range(1,n):
            
            currmax = max(currmax+nums[(i) % n],nums[(i) % n])
            currmin = min(currmin+nums[(i) % n],nums[(i) % n])
            maxsum = max(maxsum,currmax)
            minsum = min(minsum,currmin)
        circularsum = totalsum - minsum
        if circularsum == 0:
            return maxsum
        result  = max(maxsum,circularsum)
            

        return result