# Function to solve the Knapsack problem using Top-Down DP
def knapsack_top_down(weights, profits, capacity):

    n = len(weights)

    # Create a memo table
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    def solve(i, w):

        # Base case
        if i == 0 or w == 0:
            return 0

        # If already calculated
        if memo[i][w] != -1:
            return memo[i][w]

        # If current item fits
        if weights[i - 1] <= w:

            include = profits[i - 1] + solve(i - 1, w - weights[i - 1])
            exclude = solve(i - 1, w)

            memo[i][w] = max(include, exclude)

        else:
            memo[i][w] = solve(i - 1, w)

        return memo[i][w]

    return solve(n, capacity)


# Function to solve the Knapsack problem using Bottom-Up DP
def knapsack_bottom_up(weights, profits, capacity):

    # Find the number of items
    n = len(weights)

    # Create a DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Go through each item one by one
    for i in range(1, n + 1):

        # Check every possible capacity
        for w in range(1, capacity + 1):

            # Check if current item's weight fits
            if weights[i - 1] <= w:

                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main program

weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
capacity = 5

# Find maximum profit using Bottom-Up DP
bottom_up_result = knapsack_bottom_up(weights, profits, capacity)

# Find maximum profit using Top-Down DP
top_down_result = knapsack_top_down(weights, profits, capacity)

print("Maximum Profit using Bottom-Up:", bottom_up_result)
print("Maximum Profit using Top-Down:", top_down_result)
