class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        buckets = [[] for _ in range(len(nums))]
        for num, f in freq.items():
            buckets[f - 1].append(num)

        res = []

        for bucket in buckets[::-1]:
            if len(res) == k:
                break
            if not bucket:
                continue
            else:
                res.extend(bucket)
        return res

        
        