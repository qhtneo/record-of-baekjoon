# 초 -> 분:초 변환 함수
def convert_to_minutes_seconds(total_seconds):
    return f"{total_seconds // 60:02d}:{total_seconds % 60:02d}"


# 입력 처리
N = int(input())
TOTAL_TIME = 48 * 60  # 총 경기 시간(초 단위)

# 각 팀의 점수와 이기던 시간
team1_score = 0
team2_score = 0
team1_time = 0
team2_time = 0

last_time = 0  # 마지막 득점 시간
current_lead = None  # 현재 이기고 있는 팀

for _ in range(N):
    team_str, time_str = input().split()
    team = int(team_str)
    minutes, seconds = map(int, time_str.split(':'))
    current_time = minutes * 60 + seconds

    # 득점 반영
    if team == 1:
        team1_score += 1
    else:
        team2_score += 1

    # 현재 이기고 있는 팀 결정
    if team1_score > team2_score:
        new_lead = 1
    elif team1_score < team2_score:
        new_lead = 2
    else:
        new_lead = None

    # 이기고 있던 시간 계산
    if current_lead is not None:
        lead_time = current_time - last_time
        if current_lead == 1:
            team1_time += lead_time
        elif current_lead == 2:
            team2_time += lead_time

    # 상태 갱신
    last_time = current_time
    current_lead = new_lead

# 경기 종료 후 남은 시간 계산
if current_lead is not None:
    lead_time = TOTAL_TIME - last_time
    if current_lead == 1:
        team1_time += lead_time
    elif current_lead == 2:
        team2_time += lead_time

# 결과 출력
print(convert_to_minutes_seconds(team1_time))
print(convert_to_minutes_seconds(team2_time))
