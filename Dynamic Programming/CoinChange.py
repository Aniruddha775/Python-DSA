from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down DP (Memoization)
        # Time: O(Coins * Amount)
        # Space: O(Amount)
        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            
            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + min_coins(diff))
            
            memo[amt] = minn
            return minn

        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1

#Bottom-Up Tabulation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1) #we are considering the amount 0 also

        for i in range(1,amount+1):
            minn=float('inf')

            for coin in coins:
                diff=i-coin #we calucate diff inorder to see how many ways can that value be achieved
                if diff<0: #ignoring the negative results
                    continue
                minn=min(minn,1+dp[diff]) #we addoing 1 as because we are using that particular coin
        
            dp[i]=minn
        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1