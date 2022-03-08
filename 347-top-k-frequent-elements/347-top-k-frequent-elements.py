from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f_k = c.most_common(k)
        answer = [x[0] for x in f_k] 
        return answer
