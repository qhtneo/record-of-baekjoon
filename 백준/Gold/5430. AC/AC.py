import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
  func = input()
  list_length = int(input())
  
  if list_length == 0:
    num_list = deque()
    input()
  else: 
    num_list = deque(map(int, input().strip()[1:-1].split(',')))
  
  iserror = False
  reversed_flag = False  # R의 적용 여부를 기록하는 플래그

  for char in func:
      if char == 'R':
          reversed_flag = not reversed_flag  # 뒤집기 플래그 토글
      elif char == 'D':
          if not num_list:
              iserror = True
              break
          else:
              if reversed_flag:
                  num_list.pop()  # 뒤집힌 상태일 때는 끝에서 제거
              else:
                  num_list.popleft()  # 앞에서 제거

  if iserror:
      print("error")
  else:
      if reversed_flag:
          num_list.reverse()  # 최종적으로 뒤집기
      print('[' + ','.join(map(str, num_list)) + ']')
