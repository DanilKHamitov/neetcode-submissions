class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            lst_end = output[-1][1]
            if start <= lst_end:
                output[-1][1] = max(lst_end,end)
            else:
                output.append([start,end])
        return output
