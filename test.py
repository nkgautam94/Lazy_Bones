import math, operator as op
operators=['+','-','*','/']
ops=dict()
ops.update({'+':op.add,
          '-':op.sub,
          '*':op.mul,
          '>':op.gt,
          '<':op.lt,
          '>=':op.ge,
          '<=':op.le,
          '=':op.eq})

def postfix( command ):
    
    stack=[]
    postfix=[]
    for i in command:
        if i in operators:
            stack.append(i)
        elif i==')':
            postfix.append(stack.pop())
        elif i=='(':
            pass
        else:
            postfix.append(i)
    while(len(stack)!=0):
        postfix.append(stack.pop())
    return postfix

def evaluate_postfix( l ):
    stack=[]
    for i in l:
        if i in operators:
            a=stack.pop()
            b=stack.pop()
            #operator=ops[i]
            #result=operator(a,b)
            #stack.append(result)
            stack.append(str(a+i+b))
        else:
            stack.append(i)
    stack[0]=stack[0][::-1]
    print(stack)
    
        
        
while 1:
    command=input()
    l=postfix(command)
    for i in l:
        print(i,end="")
    print()
    evaluate_postfix(l)
