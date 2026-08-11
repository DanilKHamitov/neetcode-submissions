class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
         
        while len(heap) >=2:
            x = heap[0]
            heapq.heappop(heap)
            y = heap[0]
            heapq.heappop(heap)
            if x == y:
                continue
            x = x - y                # 1 5 4 2 3  - > -5 -1 -4 -2 -3 - 
            heapq.heappush(heap,x)
        if len(heap)  ==0:
            return 0
        return abs(heap[0])

            
        