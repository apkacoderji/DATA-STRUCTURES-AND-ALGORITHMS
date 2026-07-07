class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
    """
        freq = {0:1}
        prefixSum = 0
        res_count = 0

        for num in nums:

            prefixSum += num

            if (prefixSum-k) in freq:
                res_count += freq[prefixSum-k]

            if prefixSum in freq:
                freq[prefixSum] += 1

            else:
                freq[prefixSum] = 1

        
        return res_count

    