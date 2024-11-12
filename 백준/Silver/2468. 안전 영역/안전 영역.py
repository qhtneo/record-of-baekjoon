from collections import deque

n = int(input())
graph = [list(map(int, input().rsplit())) for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited, x, y):
  queue = deque([(x, y)])
  
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > num:
        queue.append((nx, ny))
        visited[nx][ny] = True

# 임시
# 최대치 비교를 위한 변수
max_safe_zone_length = 1
# 장마의 가정 높이 1~100
for num in range(1, 101):
  # 방문 위치 초기화
  visited = [[False] * n for _ in range(n)]
  # 생존지역 길이 초기화
  count = 0
  # bfs 사용전 전처리(침수 지역 초기화)
  for i in range(n):
    for j in range(n):
      if graph[i][j] <= num:
        visited[i][j] = True

      # bfs 실행문
      if graph[i][j] > num and not visited[i][j]:
        bfs(visited, i, j)
        count += 1

      max_safe_zone_length = max(max_safe_zone_length, count)

print(max_safe_zone_length)
