from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 0부터 세기때문에 N-1, M-1이 최대

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 내 계획 : 모든 수를 다들려 근데 수가 0이면 안세 그리고 1이면 큐에 넣어
total_sum = 0
for lists in graph:
  for num in lists:
    total_sum += num
    
if total_sum > 0:
  total_count = 0
  lengths = []
  
  def bfs(x, y):
    queue = deque([(x, y)])
    length = 0
    
    while queue:
      x, y = queue.popleft()
      if graph[x][y] == 1:
        length += 1
        graph[x][y] = 0
      # 현재 위치에서 4방향으로의 위치 확인
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
  
        # 범위를 벗어나면 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
          continue
        # 벽이거나 이미 방문한 경우 무시 여기서 벽은 0을 의미
        if graph[nx][ny] == 0:
          continue
  
        # 처음 방문하는 노드라면 거리 갱신 후 큐에 추가
        if graph[nx][ny] == 1:  # 방문하지 않은 노드인 경우
          queue.append((nx, ny))
          graph[nx][ny] = 0
          length += 1
    # 마지막 위치의 값(최단 경로의 길이)
    return lengths.append(length)
  
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        bfs(i,j)
        total_count += 1
        
  print(total_count)
  print(max(lengths))
else:
  print(0)
  print(0)