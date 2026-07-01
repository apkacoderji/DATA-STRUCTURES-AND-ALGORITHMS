class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = minsum = curr_max = curr_min = nums[0]

        for num in nums[1:]:
            curr_max = max(curr_max+num,num)
            curr_min = min(curr_min+num,num)
            maxsum = max(maxsum,curr_max)
            minsum = min(minsum,curr_min)

        return max(maxsum,abs(minsum))