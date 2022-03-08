class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        tested = []
        for i in nums:
            if i in tested:
                c = c + 1
                continue
            if nums.count(nums[c]) == 2:
                tested.append(nums[c])
                c = c + 1
                continue
            return nums[c]