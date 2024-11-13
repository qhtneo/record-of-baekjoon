while True:
  str = input() 
  check = []
  answer = "yes"
  
  # 종료조건
  if str == ".":
    break
    
  for s in str:
    if s == "(" or s == "[":
      check.append(s)
    # 닫는 괄호가 들어올 때
    elif s == ")":
      # 체크리스트가 비어있다면
      if not len(check):
        answer = "no"
        break
      # 닫는 괄호가 들어올때 체크리스트 안에 뭔가 있다면
      else:
        # 그리고 그걸 꺼냈을때 "("이 아니라면 
        if check.pop(-1) != "(":
          answer = "no"
          break
    # 닫는 대괄호가 들어올 때
    elif s == "]":
        # 체크리스트가 비어있다면
        if not len(check):
          answer = "no"
          break
        # 체크리스트 안에 있다면
        else:
          # 근데 꺼낸게 "["가 아니라면
          if check.pop(-1) != "[":
            answer = "no"
            break
    else:
      continue
  if len(check):
    answer = 'no'
  print(answer)