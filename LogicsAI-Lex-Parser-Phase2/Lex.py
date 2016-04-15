#  LogicsAI Lexer
#
#  By Angel Perez, Carlos Donato, Gilberto Jimenez, Luis Sala


import ply.lex as lex

#Format: {'reserved_word':'token_name'}
reserved = {'and': 'AND',
            'or': 'OR', 'if': 'IF', 'then': 'THEN', 'is': 'IS', 'are': 'ARE', 'the': 'THE', 'not': 'NOT', 'what': 'WHAT'}


#Tokens List
tokens = ['SUBJECT', 'OBJECT', 'COMPOBJ', 'OP'] + list(reserved.values())


# Ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Regex rules
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_NOT(t):
    r'\bnot\b'
    t.type = reserved.get(t.value,'NOT')
    return t

def t_WHAT(t):
    r'\bwhat\b'
    t.type = reserved.get(t.value,'WHAT')
    return t

def t_AND(t):
    r'\band\b'
    t.type = reserved.get(t.value,'AND')
    return t

def t_OR(t):
    r'\bor\b'
    t.type = reserved.get(t.value,'OR')
    return t

def t_THE(t):
    r'\bthe\b'
    t.type = reserved.get(t.value,'THE')
    return t

def t_IS(t):
    r'\bis\b'
    t.type = reserved.get(t.value,'IS') 
    return t

def t_ARE(t):
    r'\bare\b'
    t.type = reserved.get(t.value,'ARE') 
    return t

def t_IF(t):
    r'\bif\b'
    t.type = reserved.get(t.value,'IF') 
    return t

def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_]*'
    t.type = reserved.get(t.value,'OP') 
    return t

def t_OBJECT(t):
    r'\@[a-zA-Z_]*'
    t.value = t.value[1:]
    return t

def t_COMPOBJ(t):
    r'\!\@[a-zA-Z_]*'
    t.value = t.value[2:]
    return t

def t_SUBJECT(t):
    r'\#[a-zA-Z_]*'
    t.value = t.value[1:]
    return t

def t_COMMENT(t):
    r'\;.*'
    pass
    # Token is not used

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()

##### For testing Lexer
##data = "the #sky is !@blue"
##
### Give the lexer some input
##lexer.input(data)
##
##print(tokens)
##
### Tokenize
##while True:
##    tok = lexer.token()
##    if not tok:
##        break      # No more input
##    print(tok)
