#https://codeforces.com/problemset/problem/189/A?f0a28=1
n, a, b, c = list(map(int, input().split()))
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for l in [a, b, c]:
        if i - l >= 0 and dp[i-l] != -1:
            dp[i] = max(dp[i], dp[i-l] + 1)
print(dp[-1])