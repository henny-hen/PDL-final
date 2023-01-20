# calclex.py

from sly import Lexer
import sys

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { NUM, ID, WHILE, IF, ELSE, PRINT,
               MAS, MASI, ASSIGN,
               EQQ, DIF, RETURN, STRING, FUNCTION,
               VAR, INT, BOOLEAN, LET, FOR, DO, 
               CAD, COM, PYC, PARI, PARF, CORI, 
               CORF, TRUE, FALSE }


    literals = { '(', ')', '{', '}', ';', ',' }

    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'//.*'
    # Regular expression rules for tokens
    MASI    = r'\+='
    MAS    = r'\+'
    EQQ      = r'=='
    ASSIGN  = r'='
    DIF      = r'!'
    COM   = r','
    PYC   = r';'
    PARI   = r'\('
    PARF   = r'\)'
    CORI   = r'\{'
    CORF   = r'\}'




    @_(r'[0-9][0-9]*[a-zA-Z_][a-zA-Z_]*[a-zA-Z0-9_]*')
    def numErroneo(self, t):
        print ('Error en linea %d: identificador o numero incorrecto (%r)' % (self.lineno, t.value))
        fd2 = open("errores.txt", "a")
        fd2.write('Error en linea %d: identificador o numero incorrecto (%r)' % (self.lineno, t.value))
        fd2.write('\n')
    
    @_(r'\+=')
    def MASI(self,t):
        t.value = ''
        return t
    @_(r'\+')
    def MAS(self,t):
        t.value = ''
        return t
    @_(r',')
    def COM(self,t):
        t.value = ''
        return t
    @_(r';')
    def PYC(self,t):
        t.value = ''
        return t
    @_(r'\(')
    def PARI(self,t):
        t.value = ''
        return t
    @_(r'\)')
    def PARF(self,t):
        t.value = ''
        return t

    @_(r'\}')
    def CORF(self,t):
        t.value = ''
        return t

    @_(r'\{')
    def CORI(self,t):
        t.value = ''
        return t

    @_(r'\*')
    def MUL(self,t):
        t.value = ''
        return t
    @_(r'=')
    def ASSIGN(self,t):
        t.value = ''
        return t
    @_(r'==')
    def EQQ(self,t):
        t.value = ''
        return t
    @_(r'!')
    def DIF(self,t):
        t.value = ''
        return t

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        if t.value > 32768:
                    print ('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
                    fd2 = open("errores.txt", "a")
                    fd2.write('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
                    fd2.write('\n')
        elif t.value < -32768:
                    print ('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
                    fd2 = open("errores.txt", "a")
                    fd2.write('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
                    fd2.write('\n')

        else:
            return t

   
    
    @_(r'[\'][a-zA-Z0-9_\s,%.():;<>?!]*[\']')
    def CAD(self, t):
        try:
            t.value = str(t.value)
        except ValueError:
            t.value = 0
        return t


    # Identifiers and keywords
    CAD = r'[\'][a-zA-Z0-9_\s,%.():;<>?!]*[\']'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT
    ID['for'] = FOR
    ID['var'] = VAR
    ID['function'] = FUNCTION
    ID['return'] = RETURN
    ID['do'] = DO
    ID['int'] = INT
    ID['string'] = STRING
    ID['boolean'] = BOOLEAN
    ID['true'] = TRUE
    ID['false'] = FALSE
    ID['let'] = LET
    



    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


    def error(self, t):
        print('Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
        fd2 = open("errores.txt", "a") 
        fd2.write('Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
        fd2.write('\n')
        self.index += 1




if __name__ == '__main__':

numTS = 1
posTS = 1
TS = {}

fd = open(sys.argv[1], 'r')
txt = fd.read()

fd2 = open("errores.txt", "w") 
fd3 = open("tokens.txt", "w")
fd4 = open("TS.txt", "w")
fd4.write("TABLA # %d : \n \n" % numTS)

lexer = CalcLexer()
for tok in lexer.tokenize(txt):
    fd3 = open("tokens.txt", "a") 
    if((tok.type == 'ID')):
        if(TS.get(tok.value, -1) == -1):
            fd4 = open("TS.txt", "a")
            print("lexema")
            TS[tok.value] = posTS
            TS[tok.value + '.type'] = '-'
            fd4.write("* LEXEMA: %r \n" % tok.value)
            fd4.write("\t Atributos: \n")
            fd4.write("\t + tipo = - \n")
            fd4.write("\t + despl = %d \n" % posTS)
            fd4.write("-----------  ------------ \n") 
            posTS += 1
        print("< %r , %d >" % (tok.value, TS.get(tok.value)))
        fd3.write("< %r , %d > \n" % (tok.value, TS.get(tok.value)))
    else:
        print("< %r , %s >" % (tok.type, tok.value))
        fd3.write("< %r , %s >" % (tok.type, tok.value))
        fd3.write('\n')


print(TS)

        

fd.close()
fd2.close()
fd3.close()
fd4.close()

