class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp0 = arr[0]
        dp1 = arr[0]
        result = arr[0]

        for i in range(1,len(arr)):

            dp1 = max(dp1+arr[i],dp0)
            dp0 = max(arr[i]+dp0,arr[i])

            result = max(dp0,dp1,result)

        return result
            



        