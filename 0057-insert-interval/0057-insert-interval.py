class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        ans = []

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1,len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:#merge
                end1 = max(end1,end2)
                
            
            else:#no merge
                ans.append([start1,end1])
                start1 = start2
                end1 = end2
            
        # Add the last merged interval
        ans.append([start1,end1])

        return ans