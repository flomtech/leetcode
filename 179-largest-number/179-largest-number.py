from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        my_sorted_numbers_ = sorted(map(str, nums), key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
        ans = ''.join(my_sorted_numbers_).lstrip('0')
        return ans or '0'