T = int(input())
for _ in range(T):
  count = 0
  N, M = map(int, input().split())
  list_a = list(map(int, input().split()))
  list_b = list(map(int, input().split()))
  list_b = sorted(list_b)
  
  for num_a in list_a:
    first = 0
    end = len(list_b) - 1
    while first <= end:
      mid = (first + end)//2
      
      if num_a > list_b[mid]:
        first = mid + 1
      else:
        end = mid - 1
    count += first
  print(count)
