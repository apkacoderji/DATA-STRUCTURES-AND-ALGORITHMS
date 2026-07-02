class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxprod = nums[0]
        minprod = nums[0]
        result = nums[0]

        for num in nums[1:]:

            candidates = (num,num * minprod,num * maxprod)
            minprod = min(candidates)
            maxprod = max(candidates)

            result = max(maxprod,result)

        return result



        #     v1 = nums[i]
        #     v2 = minprod * v1
        #     v3 = maxprod * v1

        #     minprod = min(v1,min(v2,v3))
        #     maxprod = max(v1,max(v2,v3))

        #     result = max(minprod,maxprod,result)

        # return result

    



