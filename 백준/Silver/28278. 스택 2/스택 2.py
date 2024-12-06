import sys
input = sys.stdin.read


numbers = []
results = []

orders = input().splitlines()
n = int(orders[0])

for i in range(1, n + 1):
  order = orders[i]
  if order.startswith('1'):
    od, num = map(int, order.split())
    numbers.append(num)
  elif order == '2':
    if numbers:
      results.append(numbers.pop())
    else:
      results.append(-1)
  elif order == '3':
      results.append(len(numbers))
  elif order == '4':
    results.append(0 if numbers else 1)
  elif order == '5':
    results.append(numbers[-1] if numbers else -1)

sys.stdout.write('\n'.join(map(str, results)) + '\n')