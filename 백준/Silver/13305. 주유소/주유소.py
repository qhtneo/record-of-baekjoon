N = int(input())

load_len_list = list(map(int, input().split()))
fuel_price_list = list(map(int, input().split()))

# 기본으로 깔고가는 최소 금액
FIRST_PRICE = fuel_price_list[0] * load_len_list[0]

# 기름 최솟가
MIN_PRICE = min(fuel_price_list[:-1])

# 현재 최소 기름 금액
current_min_price = fuel_price_list[0]

# 첫도시의 기름가격이 제일 최저가라면
result = 0
if fuel_price_list[0] == MIN_PRICE:
    for load_len in load_len_list:
        result += load_len * fuel_price_list[0]
# 첫도시의 기름가격이 최저가가 아니라면----------------------------------------------
else:
    # 첫 도시는 이미 기름 채웠고 도착할 마지막 도시 기름 가격은 필요없음
    for i in range(1, len(fuel_price_list) - 1):
        # 기름 가격이 현재 최소 기름 가격보다 낮다면
        # 이제부턴 기름가격을 변경시켜서 더해야 함
        if fuel_price_list[i] < current_min_price:
            current_min_price = fuel_price_list[i]
        result += load_len_list[i] * current_min_price
    # 첫 값 더해주기
    result += FIRST_PRICE
print(result)