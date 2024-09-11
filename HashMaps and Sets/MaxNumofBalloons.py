class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter={}
        balloon='balloon'

        for c in text:
            if c in balloon:
                counter[c]=1+counter.get(c,0)
        if any(c not in counter for c in balloon):
            return 0
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
    
n=Solution()
print(n.maxNumberOfBalloons('loonbalxballpoon'))