#Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        return self.fib(n-2) + self.fib(n-1)

#Top Down Memoization
class Solution:
    def fib(self, n: int) -> int:
        memo={0:0,1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x]=f(x-2)+f(x-1)
                return memo[x]
        
        return f(n)


#Bottom Up Tabulation

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]

#Bottom-up Constant Space
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        cur = 1

        for i in range(2, n+1):
            prev, cur = cur, prev+cur
        
        return cur

        

n=Solution()
print(n.fib(10))