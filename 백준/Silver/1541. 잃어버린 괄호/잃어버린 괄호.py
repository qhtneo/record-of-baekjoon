expression = input()

# '-'를 기준으로 식을 분리
parts = expression.split('-')

# 각 부분을 분리하여 합을 구한 뒤, 첫 번째 부분을 기준으로 빼줌
result = sum(map(int, parts[0].split('+'))) # 앞부분 합

for part in parts[1:]:
    result -= sum(map(int, part.split('+'))) # 뒷부분 합을 앞부분 결과값에서 뺌
print(result)