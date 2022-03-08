class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        nums.sort()
        
        length_of_array = len(nums)
        
        # base case
        if length_of_array < 3:
            if length_of_array == 2:
                if (nums[0] + 1) == nums[1]:
                    return 2
                else:
                    return 1
            else:
                return length_of_array
            
        
    
        currentLongest = 1
        
        currentMax = 2
        for i in range(1,len(nums)):
            previous = nums[i-1]
            current = nums[i]       
            if (previous + 1) != current:
                currentMax = 1       
            if currentMax > currentLongest:
                currentLongest = currentMax

            currentMax = currentMax + 1             
        return currentLongest
    
    
          