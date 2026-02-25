class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        heap = []
        for num in arr:
            count = format(num, "b").count("1")
            heapq.heappush(heap, (count, num))

        res = []
        for _ in arr:
            res.append(heapq.heappop(heap)[1])

        return res