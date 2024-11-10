# 병사의 수 N
N = int(input())

# 병사 리스트(soliders)
soldiers = list(map(int, input().split()))
lds = []

for combat_power in soldiers:
  # 현재 원소의 위치를 직접 구현한 이진 탐색으로 찾기
  first, end = 0, len(lds)
  while first < end:
    mid = (first + end) // 2
    if lds[mid] > combat_power:
      first = mid + 1
    else:
      end = mid
  pos = end

  # 위치가 리스트의 길이와 같으면 새로운 원소 추가
  if pos == len(lds):
    lds.append(combat_power)
  else:
    # 기존 원소를 현재 원소로 교체
    lds[pos] = combat_power

# 최장 감소 부분 수열의 길이 반환
print(N-len(lds))