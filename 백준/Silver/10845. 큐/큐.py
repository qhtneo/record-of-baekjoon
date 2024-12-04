n = int(input())

queueList = []

def queue(order, queueList):
  if order[:4] == "push":
    z, num = order.split()
    queueList.append(int(num))
  elif order == "pop":
    if len(queueList) > 0:
      print(queueList.pop(0))
    else:
      print(-1)
  elif order == "size":
    print(len(queueList))
  elif order == "empty":
    if len(queueList) == 0:
      print(1)
    else:
      print(0)
  elif order == "front":
    if len(queueList) > 0:
      print(queueList[0])
    else:
      print(-1)
  elif order == "back":
    if len(queueList) > 0:
      print(queueList[-1])
    else:
      print(-1)
      
for _ in range(n):
  queue(input(), queueList)
  