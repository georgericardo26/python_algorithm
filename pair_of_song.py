class Solution(object):
   def numPairsDivisibleBy60(self, time):
      ans = 0
      remainder = {}
      for i in time:
         if i % 60 == 0 and 0 in remainder:
            ans += remainder[0]
         elif 60 - (i%60) in remainder:
            ans += remainder[60 - (i%60)]
         if i % 60 in remainder:
            remainder[i%60]+=1
         else:
            remainder[i%60]=1
      return ans
ob1 = Solution()
# print(ob1.numPairsDivisibleBy60([30,20,150,100,40]))
print(ob1.numPairsDivisibleBy60([37, 23, 60]))



"""

Take a map rem to store remainders. Set ans := 0
for all elements i in time −
if i is divisible by 0 and 0 in rem, then ans := ans + rem[0]
o otherwise when 60 – (i mod 60) in rem, then ans := ans + rem[60 – (i mod 60)]
if i mod 60 in rem, then rem[i mod 60] := rem[i mod 60] + 1
otherwise rem[i mod 60] := 1
return the ans

"""