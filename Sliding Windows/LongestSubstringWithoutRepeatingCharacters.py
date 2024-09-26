class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        longest=0
        n=len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            
            window=(r-l)+1
            longest=max(window,longest)
            sett.add(s[r])

        return longest

n=Solution()
print(n.lengthOfLongestSubstring("abcabcbb")) 