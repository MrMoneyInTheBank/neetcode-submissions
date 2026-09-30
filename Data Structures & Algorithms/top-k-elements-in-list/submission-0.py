from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = {v: [] for v in freq.values()}

        for num, f in freq.items():
            buckets[f].append(num)

        res = []

        for f in range(len(nums), 0, -1):
            if len(res) == k:
                break
            if f not in buckets:
                continue
            else:
                while buckets[f] != [] and k - len(res) > 0:
                    res.append(buckets[f].pop())
            
        return res

        