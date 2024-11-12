from collections import deque
from re import T

N, K = map(int, input().split())
LIMIT = 100000

def bfs(start):
  queue = deque([(start, 0)])
  visited = [False] * (LIMIT+1)
  visited[start] = True
  
  while queue:
    x, time = queue.popleft()

    # 동생의 위치에 도달한 경우
    if x == K:
        return time
      
    for next_pos in (x - 1, x + 1):
      if 0 <= next_pos <= LIMIT and not visited[next_pos]:
        visited[next_pos] = True
        queue.append((next_pos, time + 1))

    next_pos = x * 2
    if next_pos <= LIMIT and not visited[next_pos]:
      visited[next_pos] = True
      queue.append((next_pos, time + 1))
    
        
print(bfs(N))
# 큐에 (N, 0) 삽입.
# 큐에서 위치를 꺼내고, 이동 가능한 위치를 큐에 추가.
# 동생의 위치 K에 도달하면 시간을 출력하고 종료.