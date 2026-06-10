class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        dic = Counter(nums)
        d = []
        for v,f in dic.items():
            heapq.heappush(d,(f,v))

            if len(d)>k:
                heapq.heappop(d)
        return [v for f,v in d]    
