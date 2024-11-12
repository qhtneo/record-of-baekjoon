import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
  coins.append(int(input()))

# 동전 수 세기 위한 변수
count = 0

if n == 1:
  print(k//coins[0])
else:
  for _ in range(n):
    max_val = coins.pop(-1)
    if max_val > k:
      pass
    count += k//max_val
    k %= max_val
  
  print(count)
