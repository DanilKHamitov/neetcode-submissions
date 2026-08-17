class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp[i] - how much it s  cost to reach this stair
        dp = [0] * (len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
            print(dp[i])
        return dp[len(cost)]

