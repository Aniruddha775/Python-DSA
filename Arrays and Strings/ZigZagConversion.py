class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
    
        d=1 #direction of adding characters "1" for goind down "-1" for going up
        i=0 #rows index
        rows=[[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i+=d
        ans=''
        for i in range(numRows):
            ans+=''.join(rows[i])
        
        return ans
n=Solution()
print(n.convert("PAYPALISHIRING", 3))   