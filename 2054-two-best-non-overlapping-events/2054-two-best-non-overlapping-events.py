class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        max_value = 0  
        max_sum = 0   
        max_values = []  
               
        ends = [0]
        max_values.append(0)
        
        for start, end, value in events:  
            idx = bisect.bisect_right(ends, start - 1) - 1
            max_sum = max(max_sum, value + max_values[idx])         
            max_value = max(max_value, value)          
            ends.append(end)
            max_values.append(max_value)
        
        return max_sum