import sys
n = int(sys.stdin.readline())

prev = 1
now = 2
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(n - 2):
        temp = prev
        prev = now
        now = (temp + now) % 15746
    print(now)

# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n + 1):
#     dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
# print(dp)
# print(now)