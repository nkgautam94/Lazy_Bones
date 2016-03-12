def tokenize( program ):
        return program.replace('<',' < ').replace('>',' > ').split()

def make_AST( tokens ):
        if(len(tokens) == 0):
                raise SyntaxError(' EOF while reading ')
        token = tokens.pop(0)
        if(token == '<'):
                l=[]
                while(tokens[0]!='>'):
                        l.append(make_AST(tokens))
                tokens.pop(0)
                return l
        elif(token == '>'):
                raise SyntaxError(' Unexpected > ')
        else:
                        return atomic( token )

def atomic( token ):
        try:
                return int(token)
        except ValueError:
                try:
                        return float(token)
                except ValueError:
                        return str(token)

def parse( program ):
        return make_AST(tokenize(program))

make_scope=dict

def div(a,b):
        return a/b

def intdiv(a,b):
        return a//b

def global_scope():
    import math, operator as op
    
    scope = make_scope()
    scope.update({
        '+':op.add,
        '-':op.sub,
        '*':op.mul,
        '>':op.gt,
        '<':op.lt,
        '>=':op.ge,
        '<=':op.le,
        '=':op.eq,
        '/':div,
        '//':intdiv
    })
    return scope
gb=global_scope()

keywords = ['if','quote','define','lamba','print']


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
    elif(expression[0] == 'print'):
            print(eval(expression[1],scope))


def eval(expression , scope = gb):
    if(isinstance(expression,str)):
            #print("exp: stirng")
            return scope[expression]
    elif(not isinstance(expression,list)):
            #print("returning",expression)
            return expression
    if(expression[0] in keywords):
            #print("keyword called",expression[0])
            execute_keywords(expression,scope)
    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            #print("Else block")
            proc = eval(expression[0],scope)
            args = [eval(x,scope) for x in expression[1:]]
            return proc(*args)

while True:
        command = input("command: ")
        command = parse(command)
        #print("command formated as",command)
        eval(command)

