def evaluate ( expression , scope = gb):
    if(isinstance(expression,str)):
       return scope[expression]
    elif (not isinstance(expression , list )):
          return expression
    elif(expression[0] == 'quote'):
          (_,exp) = expression
          return exp
    elif(x[0] == 'if'):
          _,to_be_tested,first,second = expression
          if(evaluate(to_be_tested,scope)):
              exp = first
          else:
            exp = second
          return evaluate(exp,scope)
    else:
        function = evaluate(expression[0],scope)
        arguments = [evaluate(x,scope) for x in expression[1:]]
        return function(*arguments)

