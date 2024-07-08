import ply.lex as lex

# List of token names
tokens = (
    'NUMBER', 'ID', 'KEYWORD', 'STRING', 'CHARACTER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'EQUALS', 'PLUS_EQUALS', 'MINUS_EQUALS', 'TIMES_EQUALS', 'DIVIDE_EQUALS',
    'EQ', 'NE', 'LT', 'LE', 'GT', 'GE',
    'AND', 'OR', 'NOT',
    'AMPERSAND', 'PIPE', 'CARET', 'TILDE', 'LSHIFT', 'RSHIFT',
    'INCREMENT', 'DECREMENT',
    'DOT', 'ARROW', 'COLON', 'SEMICOLON', 'COMMA',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'COMMENT', 'MULTILINE_COMMENT',
    'PREPROCESSOR',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_EQUALS = r'='
t_PLUS_EQUALS = r'\+='
t_MINUS_EQUALS = r'-='
t_TIMES_EQUALS = r'\*='
t_DIVIDE_EQUALS = r'/='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_AMPERSAND = r'&'
t_PIPE = r'\|'
t_CARET = r'\^'
t_TILDE = r'~'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_DOT = r'\.'
t_ARROW = r'->'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
        'if', 'else', 'while', 'for', 'int', 'float', 'char', 'void', 'return',
        # Add more keywords as needed
    }
    if t.value in keywords:
        t.type = 'KEYWORD'
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t

def t_CHARACTER(t):
    r"'([^'\\]|\\.)'"
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_MULTILINE_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_PREPROCESSOR(t):
    r'\#(.)*'
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
input_code = """
#include <stdio.h>

int main() {
    // Simple program
    int a = 10;
    printf("Hello, world!\\n");
    return 0;
}
"""

lexer.input(input_code)

for token in lexer:
    print(token)

#lexer and parser

