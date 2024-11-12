import sys
from collections import deque

input = sys.stdin.readline

# 세로크기 n, 가로크기 m
n , m = map(int,input().split())
# 입력 그래프
graph = [list(map(int,input().split())) for _ in range(n)]
# 방문 체크
visited = [[-1] * m for _ in range(n)]

def bfs(i,j):
  queue = deque()
  queue.append((i,j))

  visited[i][j] = 0

  while queue:
    x, y = queue.popleft()

    for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
      nx, ny = dx + x, dy + y

      # 방문하지 않은경우
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
        # 이동할 수 없는 경우 방문만 기록하고 계속 진행
        if graph[nx][ny] == 0:
          visited[nx][ny] = 0
        # 이동할 수 있는 경우 이전 위치에서의 거리 + 1을 기록하고 큐에 추가
        elif graph[nx][ny] == 1:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
  
for i in range(n):
  for j in range(m):
    if visited[i][j] == -1 and graph[i][j] == 2:
      bfs(i,j)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(0, end = ' ')
    else:
      print(visited[i][j], end = ' ')
  print()