n = int(input())

pattern = []

for _ in range(n):
  text = list(input().strip())
  
  if len(pattern) == 0:
    pattern += text
    
  else:
    for i in range(len(pattern)):
      if text[i] != pattern[i]:
        pattern[i] = "?"

for char in pattern:
  print(char, end= "")