class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c=0
        for i in nums:
            x = target - i
            if x in nums:
                if c != nums.index(x):
                    return [c,nums.index(x)]
            c = c + 1
                
        