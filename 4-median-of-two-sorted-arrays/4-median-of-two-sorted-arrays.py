class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        my_array = nums1
        for num in nums2:
            my_array.append(num)
        
        my_array.sort()
        
        
        if len(my_array) % 2 == 0:
            mid1 = len(my_array) // 2
            mid2 = mid1 -1
            
            summation = float(my_array[mid1] + my_array[mid2])
            return summation / 2
        else:
            md = len(my_array) // 2
            return my_array[md]
            