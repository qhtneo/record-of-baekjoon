T = int(input())

for i in range(T):
  n = int(input())
  num_list = []

  for _ in range(n):
    num_list.append(int(input()))
  # lis 길이의 총합을 저장할 변수
  total_length = 0
  # 모든 연속 부분 수열을 생성
  for start in range(n):
    lis = []
    for end in range(start, n):
      num = num_list[end]
      
      left, right = 0, len(lis)
      while left < right:
        mid = (left + right) // 2
        if lis[mid] < num:
          left = mid + 1
        else:
          right = mid
      pos = left
  
      # 위치가 리스트의 길이와 같으면 새로운 원소 추가
      if pos == len(lis):
        lis.append(num)
      else:
        # 기존 원소를 현재 원소로 교체
        lis[pos] = num
      total_length += len(lis)
  # 최장 증가 부분 수열의 길이 반환
  print(f"Case #{i + 1}: {total_length}")
  