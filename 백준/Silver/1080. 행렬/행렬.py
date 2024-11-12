import sys

input = sys.stdin.readline

n ,m = map(int,input().split())

before = [list(map(int,input().rstrip())) for _ in range(n)]
after = [list(map(int,input().rstrip())) for _ in range(n)]

def check(i,j):
  for x in range(i, i+3):
    for y in range(j, j+3):
      if before[x][y] == 0:
        before[x][y] = 1
      else:
        before[x][y] = 0

count = 0

if(n < 3 or m < 3) and before != after:
  count = -1
else:
  for r in range(n-2):
    for c in range(m-2):
      if before[r][c] != after[r][c]:
        count += 1
        check(r, c)

if count != -1 and before != after:
    count = -1
print(count)