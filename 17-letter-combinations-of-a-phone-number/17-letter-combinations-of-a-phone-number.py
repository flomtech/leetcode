class Solution(object):
   def master(self, d, c, res, cs="",cl = 0):
      if cl == len(d):
         res.append(cs)
         return
      for i in c[int(d[cl])]:
         self.master(d,c,res,cs+i,cl+1)

         
   def letterCombinations(self, d):
      if len(d) == 0:
         return []
      c = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
      an = []
      self.master(d,c,an)
      return an
