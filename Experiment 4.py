def fibonacci_memoization(n, dp):

  
    if n == 0:
        return 0

    if n == 1:
        return 1

    
    if dp[n] != -1:
        return dp[n]

    
    dp[n] = (
        fibonacci_memoization(n - 1, dp)
        + fibonacci_memoization(n - 2, dp)
    )

    return dp[n]


def fibonacci_tabulation(n):

    # Base cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    
    dp = [0] * (n + 1)

   
    dp[0] = 0
    dp[1] = 1

    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n], dp


print("========================================")
print("       FIBONACCI USING DYNAMIC          ")
print("          PROGRAMMING (DP)              ")
print("========================================")


n = int(input("Enter the value of n: "))

memo_dp = [-1] * (n + 1)


memo_result = fibonacci_memoization(n, memo_dp)

print("\n----------------------------------------")
print("        MEMOIZATION RESULT")
print("----------------------------------------")

print("Fibonacci number:", memo_result)
print("DP Array:", memo_dp)


tab_result, tab_dp = fibonacci_tabulation(n)

print("\n----------------------------------------")
print("        TABULATION RESULT")
print("----------------------------------------")

print("Fibonacci number:", tab_result)
print("DP Array:", tab_dp)


print("\n========================================")
print("              COMPARISON")
print("========================================")

print("Memoization Result :", memo_result)
print("Tabulation Result  :", tab_result)

if memo_result == tab_result:
    print("Both methods give the same result.")

print("\nMemoization : Top-Down + Recursion")
print("Tabulation  : Bottom-Up + Iteration")

print("\nTime Complexity:")
print("Memoization : O(n)")
print("Tabulation  : O(n)")

print("\nSpace Complexity:")
print("Memoization : O(n)")
print("Tabulation  : O(n)")
