people, party = map(int, input().split())

# 비밀을 아는사람
known_people = set(list(map(int,input().split()))[1:])

result = 0
parties = []

for _ in range(party):
  # 파티 리스트
  party_list = list(map(int, input().split()))[1:]
  parties.append(party_list)
  
# 비밀을 아는 사람이 존재하는 파티는 전부 비밀을 알게됨
updated = True
while updated:
  updated = False
  for party_list in parties:
    if known_people & set(party_list) and \
       not known_people.issuperset(set(party_list)):
        known_people.update(party_list)
        updated = True
        
for party in parties:
  if not (known_people & set(party)):
    result += 1
print(result)