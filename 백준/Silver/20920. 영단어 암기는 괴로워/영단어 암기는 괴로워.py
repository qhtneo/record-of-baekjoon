words = dict()
n, w_len = map(int, input().split())

for i in range(n):
  word = input()
  if len(word) >= w_len:
    if word not in words:
      words[word] = 1
    else:
      words[word] += 1
words_tueple = sorted(words.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))

for str, count in words_tueple:
  print(str)
