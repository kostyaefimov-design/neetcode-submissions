class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) +1 # если нет возвращает 0+1 = 1, если есть один 1
        freqlist = [[] for _ in range(len(nums)+1)]
        for key, v in count.items():
            freqlist[v].append(key)
        res = []
        for i in range(len(freqlist) - 1, 0, -1):
            for num in freqlist[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return "А такого быть не может"