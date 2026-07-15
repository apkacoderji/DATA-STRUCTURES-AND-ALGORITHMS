class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        new_intervals = []
        insert = True
        
        for i in range(n):

            if intervals[i][0] > newInterval[0] and insert == True:
                new_intervals.append(newInterval)
                insert = False
                
            new_intervals.append(intervals[i])
        
        if insert == True:
            new_intervals.append(newInterval)

        ans = []
        start1 = new_intervals[0][0]
        end1 = new_intervals[0][1]

        for i in range(1,len(new_intervals)):
            start2 = new_intervals[i][0]
            end2 = new_intervals[i][1]

            if end1 >= start2:#merge
                end1 = max(end1,end2)
                
            
            else:#no merge
                ans.append([start1,end1])
                start1 = start2
                end1 = end2
            
        # Add the last merged interval
        ans.append([start1,end1])

        return ans