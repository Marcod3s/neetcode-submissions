from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        if not stones:
            return 0
        MaxHeap = [-x for x in stones]

        heapq.heapify(MaxHeap)

        while len(MaxHeap) > 1:
            x = heapq.heappop(MaxHeap)
            y = heapq.heappop(MaxHeap)

            x = abs(x - y)
            heapq.heappush(MaxHeap, -x)

        return -MaxHeap[0]