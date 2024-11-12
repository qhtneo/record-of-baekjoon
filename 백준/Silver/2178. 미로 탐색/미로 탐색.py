from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
# 0부터 세기때문에 N-1, M-1이 최대

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  # 큐 생성 및 시작점 추가
  queue = deque([(x, y)])
  # 리스트로 감싸는 이유 : deque는 iterable을 받아들이므로, 큐에 여러 좌표를 한꺼번에 넣기 위해 감쌈
  # 튜플로 좌표를 묶는 이유 : x,y 좌표를 하나의 단위로 묶어서 저장하고 처리하기 위해 사용. (x,y)라는 좌표 한쌍을 표현하기에 튜플이 적합함

  while queue:
    x, y = queue.popleft()

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
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 마지막 위치의 값(최단 경로의 길이)
  return graph[N - 1][M - 1]


# 시작점(0, 0)에서 BFS 수행
print(bfs(0, 0))
