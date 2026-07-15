class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
        i = j = 0


        while i < len(firstList) and j < len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            if start1 <= start2:

                if end1 >= start2:
                    res_start = max(start1,start2)
                    res_end = min(end1,end2)
                    result.append([res_start,res_end])

            else: 

                if end2 >= start1:
                    res_start = max(start1,start2)
                    res_end = min(end1,end2)
                    result.append([res_start,res_end])
                
            if end1 >= end2:
                j += 1
            elif end1 <= end2:
                i += 1

        return result
        