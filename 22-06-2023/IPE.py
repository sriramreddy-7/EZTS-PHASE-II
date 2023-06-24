postfix_expr=input()

def postfix_eval(postfix_expr):
  stack = []
  for token in postfix_expr.split():
    if token.isdigit():
      stack.append(int(token))
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      stack.append(eval(f"{operand1} {token} {operand2}"))
  return stack.pop()

postfix_eval(postfix_expr)

