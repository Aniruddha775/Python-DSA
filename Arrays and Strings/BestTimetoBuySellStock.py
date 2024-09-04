from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice=float('inf')
        maxProfit=0
        for price in prices:
            if price<minPrice:
                minPrice=price

            profit=price-minPrice

            if profit>maxProfit:
                maxProfit=profit    

        return maxProfit

n=Solution()
print(n.maxProfit([7,1,5,3,6,4])) #5