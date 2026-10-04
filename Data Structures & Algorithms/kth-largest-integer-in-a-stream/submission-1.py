class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min = nums
        self.k = k
        heapq.heapify(self.min)
        while len(self.min) > self.k:
            heapq.heappop(self.min)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min, val)
        if len(self.min) > self.k:
            heapq.heappop(self.min)
        return self.min[0]
