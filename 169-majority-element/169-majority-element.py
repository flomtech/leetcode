class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        u=[]
        for i in nums:
            if i not in u:
                u.append(i)
        for i in u:
            if nums.count(i) > n:
                return i