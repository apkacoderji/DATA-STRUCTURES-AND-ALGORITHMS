class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # n = len(nums)
        # res = -1

        # #prefix array
        # prefix = [0] * n

        # prefix[0] = nums[0]

        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] + nums[i]

        # #suffix array
        # suffix = [0] * n

        # suffix[n - 1] = nums[n - 1]

        # for i in range(n - 2, -1, -1):
        #     suffix[i] = suffix[i + 1] + nums[i]


        # for i in range(len(prefix)):
        #     if prefix[i] == suffix[i]:
        #         res = i

        # return res


        #without using extra space
        prefix = suffix = 0
        total = sum(nums)
        n = len(nums)

        for i in range(n):
            
            #suffix sum logic -> total = prefix[i] + suffix[i] + nums[i]
            suffix = total - nums[i] - prefix

            #condition to find pivot index
            if prefix == suffix:
                return i
            
            #prefix sum
            prefix += nums[i]

        return -1
            
 
            
        


    

    




    
        
    
        