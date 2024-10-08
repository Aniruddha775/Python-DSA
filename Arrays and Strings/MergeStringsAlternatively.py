
# https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        A,B=len(word1),len(word2)
        a,b=0,0 #index of the word

        s=[]
        word=1 # switch between word 1 and word 2
        while a<A and b<B:
            if word==1:
                s.append(word1[a])
                a+=1
                word=2
            else:
                s.append(word2[b])
                b+=1
                word=1
        while a<A: # if word 2 gets exhausted
            s.append(word1[a])
            a+=1
        while b<B: # if word 1 gets exhausted
            s.append(word2[b])
            b+=1

        return ''.join(s)

n=Solution()
print(n.mergeAlternately("abc","pqr")) # "apbqcr"   