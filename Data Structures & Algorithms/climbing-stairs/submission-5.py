class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dps(n:int):
            
            if n <1:
                return n
            if n ==1:
                return 1
            if n == 2:
                return 2
            if n in dp:
                return dp[n]
            
            dp[n] = dps(n-1) + dps(n-2)
            return dp[n]
        return dps(n)
            
                       
        