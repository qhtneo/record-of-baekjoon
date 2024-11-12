T = int(input())
for i in range(T):
  day, answer = map(int, input().split())
  num_list = list(map(int, input().split()))

  # lis의 끝 원소들을 저장할 리스트
  lis = []

  for num in num_list:
    # 현재 원소의 위치를 직접 구현한 이진 탐색으로 찾기
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
  print(f"Case #{i + 1}")
  # 최장 증가 부분 수열의 길이 반환
  if len(lis) >= answer:
    print(1)
  else:
    print(0)
