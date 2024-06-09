import re  #importa o uso de expressões regulares
import sys  #importa o sys para utilizar funções específicas
#Analisador Léxico

#funções para verificar os tokens
def numero(i):
    num = re.compile(r'\d+')  #expressão regular para números inteiros
    procura = re.fullmatch(num, i)  #verifica se o token corresponde ao padrão da expressão regular
    if procura:
        return True
    else:
        return False

def numeroDecimal(i):
    decimal = re.compile(r'\b\d+\.\d+\b')  #expressão regular para números decimais
    procura = re.fullmatch(decimal, i)
    if procura:
        return True
    else:
        return False

def identificador(i):
    ident = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')  #expressão regular para os identificadores
    procura = re.fullmatch(ident, i)
    if procura:
        return True
    else:
        return False

def text(i):
    texto = re.compile(r'"[^"]*"')  #expressão regular para caracteres entre aspas
    procura = re.fullmatch(texto, i)
    if procura:
        return True
    else:
        return False

def palavraReservada(i):
    pr = re.compile(r'\b(int|float|char|str|boolean|void|if|else|elif|for|while|scanf|print|main|return|input|def)\b')  #expressão regular para palavras reservadas da linguagem
    procura = re.fullmatch(pr, i)
    if procura:
        return True
    else:
        return False

def comentario(i):
    comment = re.compile(r'#.*')  #expressão regular para comentários
    procura = re.fullmatch(comment, i)
    if procura:
        return True
    else:
        return False

def operadores(i):
    op = re.compile(r'\b(:|\.|-|%|&&|!|>|>=|<|<=|!=|==|\+|\?)\b')  #expressão regular para operadores e operadores de comparação
    procura = re.fullmatch(op, i)
    if procura:
        return True
    else:
        return False

def especiais(i):
    opespeciais = re.compile(r'[()\[\]{};]')  #expressão regular para símbolos especiais
    procura = re.fullmatch(opespeciais, i)
    if procura:
        return True
    else:
        return False
#função para separar os tokens em str
def separarString(i):
    separa = re.findall(r'\b\d+\.\d+|\b\w+\b|".?"|#.$|==|>=|<=|!=|&&|\|\||[=+\-*/%><!(),;{}\[\]]', i, re.MULTILINE)  #identifica os tokens
    return separa
#inserir o código para análise
print("Digite o código-fonte para analisar:")
codigo = sys.stdin.read()
separado = separarString(codigo)
#imprimir os respectivos tokens
print("Código analisado: \n" + str(separado))

for token in separado:
    if numero(token):
        print("(" + token + ") : NUM_INT")
    elif numeroDecimal(token):
        print("(" + token + ") : NUM_DECIMAL")
    elif palavraReservada(token):
        print("(" + token + ") : PALAVRA_RESERVADA")
    elif identificador(token):
        print("(" + token + ") : IDENTIFICADOR")
    elif text(token):
        print("(" + token + ") : TEXTO")
    elif operadores(token):
        print("(" + token + ") : OPERADOR")
    elif comentario(token):
        print("(" + token + ") : COMENTARIO")
    elif especiais(token):
        print("(" + token + ") : ESPECIAL")
    else:
        print("(" + token + ") : DESCONHECIDO")