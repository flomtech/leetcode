from math import factorial

class Solution(object):

    def calculate_perm(self,my_l):
        permutations=[]
        l=len(my_l)
        for x in xrange(factorial(l)):
            av=list(my_l)
            np=[]
            for radix in xrange(l, 0, -1):
                pv=factorial(radix-1)
                index=x/pv
                np.append(av.pop(index))
                x-=index*pv
            if np not in permutations:
                permutations.append(np)
        return permutations

    def permuteUnique(self, nums):
        return self.calculate_perm(list(nums))