class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        HeapMax = [-x for  x in nums]
        heapq.heapify(HeapMax)
        while k > 1:
            heapq.heappop(HeapMax)
            k-=1
        return -HeapMax[0]
