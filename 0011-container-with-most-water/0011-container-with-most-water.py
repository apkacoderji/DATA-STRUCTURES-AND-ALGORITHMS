class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_water = 0

        def calculateWater(i,j):
            length = min(height[i],height[j])
            width = j-i

            return length*width
        
        i = 0
        j = len(height) - 1
        while i < j:
            
            
            max_water = max(max_water,calculateWater(i,j))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
         

        
        return max_water

                
        