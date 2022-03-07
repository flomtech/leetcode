class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find length of intervals
        
        lengthOfIntervals  = len(intervals)
        
        # base case
        if lengthOfIntervals == 0:
            return [newInterval]
        
        
        result_stack = []
        
        i = 0
        while i < lengthOfIntervals and intervals[i][1] < newInterval[0]:
            
            result_stack.append(intervals[i])
            i += 1
            
            
        left, right = newInterval
        
        while i < lengthOfIntervals and intervals[i][0] <= newInterval[1]:
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
            i += 1
            
        result_stack.append([left, right])
        result_stack.extend(intervals[i:])
        return result_stack