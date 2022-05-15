#https://codeforces.com/contest/1245/problem/C?locale=ru
s = input()
dp = [1] * (len(s))
mod = 10**9 + 7
l, r = 0, 0
if s[0] == 'w' or s[0] == 'm':
    print(0)
else:
    for i in range(1, len(s)):
        if s[i] == 'w' or s[i] == 'm':
            print(0)
            break
        if s[i] not in ['n', 'u']:
            dp[i] = dp[i-1]
        else:
            if s[i]==s[i-1]:
                if i==1:
                    dp[i] = 2
                else:
                    dp[i] = (dp[i-1]+dp[i-2])%mod
            else:
                dp[i]=dp[i-1]

    else:
        print(dp[-1])
