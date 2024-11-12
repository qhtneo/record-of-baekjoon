# 체스판은 8 * 8 크기 0,0 = 흰색
chessboard = []
for i in range(8):
    if i % 2 == 0 or i == 0:
      chessboard.append([0,1,0,1,0,1,0,1])
    else:
      chessboard.append([1,0,1,0,1,0,1,0])
count = 0
for i in range(8):
  piece = list(input().strip())
  for j in range(len(piece)):
    if chessboard[i][j] == 0 and piece[j] == "F":
      count += 1
print(count)