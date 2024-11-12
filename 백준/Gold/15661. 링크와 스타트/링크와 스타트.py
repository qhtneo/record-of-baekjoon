import sys

input = sys.stdin.readline

n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

visited = [0 for _ in range(n)]

def cal_it():
  global ans
  start, link = 0, 0
  for i in range(n):
    for j in range(n):
      if visited[i] and visited[j]:
        start += team[i][j]
      elif not visited[i] and not visited[j]:
        link += team[i][j]
  ans = min(ans, abs(start-link))
  return

def solve(iter):
  if iter == n:
    cal_it()
    return
  visited[iter] = 1
  solve(iter + 1)
  visited[iter] = 0
  solve(iter+1)

solve(0)
print(ans)