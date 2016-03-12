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
