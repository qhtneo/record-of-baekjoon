# 한시간 별
# 피로도 쌓이는 양 A
# 피로도 비례해 할수 있는 양 B
# 휴식시에 줄어드는 피로도 양 C
# 피로도 최대치 M
A, B, C, M = map(int, input().split())

# A = 5, B = 3, C = 2, D = 10 이라 했을 때
# 한시간 일을 했다면 다음 시간에는 무조건 휴식을 취해야 최대치에 닿지 않음
# 5 - 3 - 8 - 6 - 4 - 9 - 
# 7 - 5 - 3 - 8 - 6 - 4 - 
# 9 - 7 - 5 - 3 - 8 - 6 - 
# 4 - 9 - 7 - 5 - 3 - 8 - 

# 하루(24시간)동안 증가한 횟수 = 8 
# 시간별 작업량 3에 의해 8 * 3 = 24

# 조건으로 걸 것인가
# 반복된 패턴을 찾을 것인가

# 그리디란 무엇인가?

time = 24
work = 0
fatigue = 0
max_fatigue = M

while(time > 0):
  time -= 1
  
  # 일 했는데 맥시멈 피로도를 넘을 경우
  if fatigue + A > max_fatigue:
    # 일 안하고 휴식 조져야함
    fatigue -= C
    if fatigue < 0:
      fatigue = 0
  else:
    work += B
    fatigue += A
  
print(work)