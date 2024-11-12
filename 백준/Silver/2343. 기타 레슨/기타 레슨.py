# 강의의 수 N M
N, M = map(int,input().split())
record_list = list(map(int,input().split()))
# 최소를 본래 1로 하려고 했으나 
# 레코드 시간중 가장 큰 단일값이 들어가야 하기 때문에 최소값을 가장큰 단일값으로 변경
first = max(record_list)
end = sum(record_list)

while first <= end:
  mid = (first + end) // 2
  # 레코드의 갯수(M)을 넘어서지 않는지 체크
  # 한 레코드의 길이(Mid)값을 넘지 않는지 체크
  record = 0 # 레코드의 시간을 계산할 변수
  record_count = 0 # 레코드 판의 갯수를 세기 위한 변수
  
  for time in record_list:
    # 레코드에 시간을 더함 
    record += time
    # 이 시간이 mid 값보다 크다면 레코드판 +=1, 새로운 판에 넣으려던 시간 넣어야함
    if record > mid:
      record = 0
      record_count += 1
      record += time
  # 만약 레코드 카운트가 M을 넘는다면 최소값을 올려야함
  if record_count >= M:
    first = mid + 1
  else:
    end = mid -1
print(first)