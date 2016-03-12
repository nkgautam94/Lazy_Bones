operators=['=','/','*','-','+','^']

infix = "(a+b)*(c+d)"
postfix=[]

stack=[]

for i in infix:
    if(i in operators):
        stack.append(i)
    elif(i == ')'):
        postfix.append(stack.pop())
    elif(i =='('):
        pass
    else:
        postfix.append(i)
while len(stack)!=0:
    postfix.append(stack.pop())

print(postfix)
