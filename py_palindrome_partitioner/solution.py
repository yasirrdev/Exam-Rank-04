def palindrome_partitioner(s: str) -> int:
    if len(s) <= 1:
        return 0
    dp = [0] * len(s)

    for i in range(len(s)):
        dp[i] = i

        for j in range(i + 1):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                dp[i] = 0 if j == 0 else min(dp[i], dp[j - 1] + 1)

    return dp[-1]
