class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        result = 0
        n = len(nums)
        zero = one = 0

        for i in range(n):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            
            diff = zero - one

            if diff == 0:
                result = max(result,i+1)

            else:

                if diff in freq:
                    result = max(result,i - freq[diff])
                else:
                    freq[diff] = i

        return result
            



