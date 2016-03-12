
keywords = ['if','quote','define','lamba']


def execute_keywords( expression ,scope):
    if(expression[0] == 'define'):
        scope[expression[1]]=eval(expression[2],scope)
    elif expression[0] == 'quote':
        return expression[1]
    elif expression[0] == 'if':
        (_, condition, first, second) = expression
        if(eval(condition,scope)):
            return eval(first,scope)
        else:
            return eval(second,scope)    


def eval(expression , scope = gb):
    if(isinstance(expression,str)):
        return scope.find(scope)[scope]
    elif(not isinstance(expression,list)):
         return expression
    if(expression[0] in keywords):
         execute_keywords(expression,scope)
    else:
         proc = ecal(expression[0],scope)
         args = [eval(x,scope) for x in expression[1:]]
         return proc(*args)
    
