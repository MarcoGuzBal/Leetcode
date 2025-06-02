# Last updated: 6/2/2025, 1:54:36 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        p1 = 0
        p2 = 0

        res = ""

        while p1 < len(word1) or p2 < len(word2):

            if p1 < len(word1):
                res = res + word1[p1]
                p1 += 1
            if p2 < len(word2):
                res = res + word2[p2]
                p2 += 1

        return res


#   l = 0 
#   r = 0

#   result = ""

#   while (l < len(word1) and r < len(word2)):
#     result += word1[l]
#     result += word2[r]
#     l += 1
#     r += 1
  
#   if (l < len(word1)):
#     result += word1[l:]
#   else:
#     result += word2[r:]

#   return result
            