class Solution(object):
    def intersect(self, nums1, nums2):
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        c = collections.Counter(nums1)
        res = []
        for i in nums2:
            if c[i] > 0:
                res += i,
                c[i] -= 1
        return res