#Array of 0 and 1 [0, 0, 1, 0, 1, 1, 0]
#and k - number of elements could be skipped
#Calculate number of possible ways to reach the end
def numberOfSteps(arr, k):
    n = len(arr)
    dp = [1] * (n + 1)
    s, i = 1, 0
    while i < n:
        if arr[i] == 1:
            dp[i+1] = 0
            if i>=k:
                s-=dp[i-k]
            i+=1
            continue
        if i < k:
            dp[i+1] = s
            s += dp[i+1]
        else:
            s -= dp[i - k]
            dp[i+1] = s
            s += dp[i+1]
            print(s)
        i+=1
    print(dp)
    return dp[-1]
#[0, 0, 0, 0, 1, 0] -> [1, 0, 1, 2, 3, 0, 5]
print(numberOfSteps([1,0, 0, 0, 1, 0], 3))
