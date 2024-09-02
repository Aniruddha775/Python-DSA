# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S: int=len(s)
        T: int=len(t)

        if s=='': return True
        if S>T: return False

        j: int=0

        for i in range(T):
            if t[i]==s[j]:
                if j==S-1:
                    return True
                j+=1
            
        return False
    
n=Solution()
print(n.isSubsequence("abc","ahbgdc")) # True