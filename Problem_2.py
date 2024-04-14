'''
Time Complexity - O(n^2) for DP, O(2^n) for exhaustive
Space Complexity - O(n) for bottom up DP, O(n^2)+O(n) for top-down dp and O(n) for exhaustive
Works on Leetcode.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[1e5 for j in range(len(triangle))] for i in range(len(triangle))]
        # top Down dp
        # self.findPathSum(triangle, 0, 0, dp)
        # return dp[0][0]

        #Bottom UP DP Space Optimized
        prev = [1e5 for j in range(1)]
        prev[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            curr = [1e5 for j in range(0,i+1)]
            for j in range(0, i+1):
                #prev row has 1 less element
                #last element of current row will only have result from diagonally up left
                #similartly 1st element of current row will only have result from directly up hence we set them to max values initially
                down, diagDown = 1e5, 1e5
                if j-1 >=0:
                    diagDown = prev[j-1]
                if j <= i-1:
                    down = prev[j]
                curr[j] = triangle[i][j] + min(down,diagDown)
            prev = curr
        return min(prev)

    def findPathSum(self, triangle, i, j,dp):
        #remove the DP array and just return the sum and we get an exhaustive approach
        #topDownDP
        if i == len(triangle):
            return 0
        if dp[i][j] != 1e5:
            return dp[i][j]
        
        #min of down and diagonalDown
        down = self.findPathSum(triangle, i+1, j,dp)
        diagDown = self.findPathSum(triangle, i+1, j+1, dp)
        dp[i][j] = triangle[i][j] + min(down, diagDown)
        return dp[i][j]