def palindrome_partitioner(s: str) -> int:

    if len(s) <= 1:
        return 0
    n = len(s)
    dp = [0] * n

    for i in range(n):
        dp[i] = i
        for j in range(i + 1):
            if is_palindrome(s[j:i + 1]):
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[n-1]


def is_palindrome(s: str) -> bool:
    p = ""
    for i in s:
        if i.isalnum():
            p += i.lower()
    return p == p[::-1]


if __name__ == "__main__":
    tests = [
        ("aab", 1),
        ("racecar", 0),
        ("abcbm", 2),
        ("a", 0),
        ("", 0),
        ("banana", 1),
        ("abc", 2),
    ]

    for s, expected in tests:
        result = palindrome_partitioner(s)
        print(f'"{s}"')
        print(f"Result:   {result}")
        print(f"Expected: {expected}")
        print("-" * 30)
