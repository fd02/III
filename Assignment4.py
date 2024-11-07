def knapsack_dp(W, wt, profit, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            dp[i][w] = dp[i - 1][w]
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i][w], profit[i - 1] + dp[i - 1][w - wt[i - 1]])
    return dp[n][W]

if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    profit = [int(input(f"Profit for item {i + 1}: ")) for i in range(n)]
    wt = [int(input(f"Weight for item {i + 1}: ")) for i in range(n)]
    W = int(input("Enter max weight capacity: "))
    print("Maximum profit:", knapsack_dp(W, wt, profit, n))

""" Time Complexity: 
O(n×W), where n is the number of items and W is the knapsack capacity.
Space Complexity: 
O(n×W), for the DP table storing the intermediate results."""