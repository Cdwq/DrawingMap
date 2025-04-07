def countBalancedPermutations(num):
    MOD = 10 ** 9 + 7
    n = len(num)

    # Step 1: Count the frequency of each digit
    from collections import Counter
    freq = Counter(num)

    # Step 2: Initialize the DP array
    max_sum = sum(int(char) for char in num) // 2 + 1
    dp = [[[0] * max_sum for _ in range(max_sum)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    print(n)
    # Step 3: Iterate over each character and update the DP array
    for char, count in freq.items():
        digit = int(char)
        new_dp = [[[0] * max_sum for _ in range(max_sum)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(max_sum):
                for k in range(max_sum):
                    if dp[i][j][k] > 0:
                        for l in range(count + 1):
                            new_i = i + l
                            new_j = j + l * (digit if (i + l) % 2 == 1 else 0)
                            new_k = k + l * (digit if (i + l) % 2 == 0 else 0)
                            print(new_i, new_j, new_k)
                            if new_i <= n:
                                new_dp[new_i][new_j][new_k] += dp[i][j][k]
                                new_dp[new_i][new_j][new_k] %= MOD
        dp = new_dp

    # Step 4: Calculate the result
    result = 0
    for j in range(max_sum):
        for k in range(max_sum):
            if j == k:
                result += dp[n][j][k]
                result %= MOD

    return result


# Example usage:
print(countBalancedPermutations("123"))  # Output: 2
print(countBalancedPermutations("112"))  # Output: 1
print(countBalancedPermutations("12345"))  # Output: 0
