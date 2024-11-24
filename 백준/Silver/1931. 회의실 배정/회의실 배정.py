# 회의 의 수 N
N = int(input())
meeting_list = []
for _ in range(N):
  meeting_list.append(tuple(map(int, input().split())))

# 회의를 끝나는 시간으로 정렬
meeting_list.sort(key = lambda x : (x[1], x[0]))

# 그리디 알고리즘을 활용하여 최대 회의 갯수 구하기
count = 0 
end_time = 0

for meeting in meeting_list:
  if meeting[0] >= end_time:
    end_time = meeting[1]
    count += 1
print(count)
