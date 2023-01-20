# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, '../..')

from sly import Lexer, Parser
class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { NUM, ID, IF, ELSE, PRINT,
               MAS, MASI, ASSIGN, INPUT,
               EQQ, DIF, RETURN, STRING, FUNCTION
               , INT, BOOLEAN, LET, FOR, 
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
      #  if t.value > 32768:
       #             print ('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
        #            fd2 = open("errores.txt", "a")
         #           fd2.write('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
          #          fd2.write('\n')
       # elif t.value < -32768:
        #            print ('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
         #           fd2 = open("errores.txt", "a")
          #          fd2.write('Error en linea %d: numero excede el rango (%r)' % (self.lineno, t.value))
           #         fd2.write('\n')

        #else:
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
    ID['print'] = PRINT
    ID['for'] = FOR
    ID['function'] = FUNCTION
    ID['return'] = RETURN
    ID['int'] = INT
    ID['string'] = STRING
    ID['boolean'] = BOOLEAN
    ID['true'] = TRUE
    ID['false'] = FALSE
    ID['let'] = LET
    ID['input'] = INPUT



    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')


    def error(self, t):
     #   print('Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
      #  fd2 = open("errores.txt", "a") 
       # fd2.write('Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
        #fd2.write('\n')
        self.index += 1





class CalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.names = { }

    @_('s')
    def sp(self, p):
        parseFinal.write('1 ')

    @_('sentencias')
    def s(self, p):
        parseFinal.write('2 ')

    @_('func s')
    def s(self, p):
        parseFinal.write('3 ')

    @_('FUNCTION ID tipoo PARI parametro PARF CORI sentencias CORF')
    def func(self, p):
        parseFinal.write('4 ')
    
    @_('tipoo ID parametros')
    def parametro(self, p):
        parseFinal.write('5 ')
    
    @_('')
    def parametro(self, p):
        parseFinal.write('6 ')

    @_('COM tipoo ID parametros')
    def parametros(self, p):
        parseFinal.write('7 ')

    @_('')
    def parametros(self, p):
        parseFinal.write('8 ')

    @_('declaracion PYC s')
    def sentencias(self, p):
        parseFinal.write('9 ')

    @_('asignacion PYC s')
    def sentencias(self, p):
        parseFinal.write('10 ')

    @_('entsal PYC s')
    def sentencias(self, p):
        parseFinal.write('11 ')


    @_('llamadaf PYC s')
    def sentencias(self, p):
        parseFinal.write('12 ')


    @_('senfor PYC s')
    def sentencias(self, p):
        parseFinal.write('13 ')

    @_('senif PYC s')
    def sentencias(self, p):
        parseFinal.write('14 ')

    @_('retorno PYC s')
    def sentencias(self, p):
        parseFinal.write('15 ')


    @_('asignaciona PYC s')
    def sentencias(self, p):
        parseFinal.write('16 ')

    @_('')
    def sentencias(self, p):
        parseFinal.write('17 ')




    @_('LET ID tipoo asignaciondec')
    def declaracion(self, p):
        parseFinal.write('18 ')

    @_('ASSIGN op')
    def asignaciondec(self, p):
        parseFinal.write('19 ')

    @_('')
    def asignaciondec(self, p):
        parseFinal.write('20 ')

    @_('ID ASSIGN op')
    def asignacion(self, p):
        parseFinal.write('21 ') 


    @_('ID MASI var')
    def asignaciona(self, p):
        parseFinal.write('22 ')

    @_('var opp')
    def op(self, p):
        parseFinal.write('23 ')

    @_('CAD')
    def op(self, p):
        parseFinal.write('24 ')

    @_('DIF ID')
    def op(self, p):
        parseFinal.write('25 ')

    @_('logico')
    def op(self, p):
        parseFinal.write('26 ')

    @_('opar var opp')
    def opp(self, p):
        parseFinal.write('27 ')

    @_('EQQ op')
    def opp(self, p):
        parseFinal.write('28 ')
    @_('')
    def opp(self, p):
        parseFinal.write('29 ')

    @_('RETURN oppp')
    def retorno(self, p):
        parseFinal.write('30 ')

    @_('INPUT oppp')
    def entsal(self, p):
        parseFinal.write('31 ')

    @_('PRINT oppp')
    def entsal(self, p):
        parseFinal.write('32 ')

    @_('PARI op PARF')
    def oppp(self, p):
        parseFinal.write('33 ')

    @_('op')
    def oppp(self, p):
        parseFinal.write('34 ')

    @_('ID PARI argumento PARF')
    def llamadaf(self, p):
        parseFinal.write('35 ')

    @_('llamadaf argumentos')
    def argumento(self, p):
        parseFinal.write('36 ')

    @_('op argumentos')
    def argumento(self, p):
        parseFinal.write('37 ')

    @_('')
    def argumento(self, p):
        parseFinal.write('38 ')

    @_('COM argumentoss argumentos')
    def argumentos(self, p):
        parseFinal.write('39 ')

    @_('')
    def argumentos(self, p):
        parseFinal.write('40 ')

    @_('llamadaf')
    def argumentoss(self, p):
        parseFinal.write('41 ')

    @_('op')
    def argumentoss(self, p):
        parseFinal.write('42 ')

    @_('FOR PARI inic PYC cond PYC PARF CORI sentencias CORF')
    def senfor(self, p):
        parseFinal.write('43 ')

    @_('ID ASSIGN var opp')
    def inic(self, p):
        parseFinal.write('44 ')

    @_('')
    def inic(self, p):
        parseFinal.write('45 ')

    @_('IF PARI cond PARF senif2 senelse')
    def senif(self, p):
        parseFinal.write('46 ')

    @_('CORI sentencias CORF')
    def senif2(self, p):
        parseFinal.write('47 ')

    @_('sentencia')
    def senif2(self, p):
        parseFinal.write('48 ')

    @_('ELSE senif2')
    def senelse(self, p):
        parseFinal.write('49 ')

    @_('')
    def senelse(self, p):
        parseFinal.write('50 ')
    
    @_('var EQQ var opp')
    def cond(self, p):
        parseFinal.write('51 ')

    @_('STRING')
    def tipoo(self, p):
        parseFinal.write('52 ')

    @_('INT')
    def tipoo(self, p):
        parseFinal.write('53 ')

    @_('BOOLEAN')
    def tipoo(self, p):
        parseFinal.write('54 ')

    @_('NUM')
    def var(self, p):
        parseFinal.write('55 ')

    @_('ID')
    def var(self, p):
        parseFinal.write('56 ')

    @_('TRUE')
    def logico(self, p):
        parseFinal.write('57 ')

    @_('FALSE')
    def logico(self, p):
        parseFinal.write('58 ')

    @_('MAS')
    def opar(self, p):
        parseFinal.write('59 ')

    @_('declaracion PYC')
    def sentencia(self, p):
        parseFinal.write('60 ')

    @_('asignacion PYC')
    def sentencia(self, p):
        parseFinal.write('61 ')

    @_('entsal PYC')
    def sentencia(self, p):
        parseFinal.write('62 ')

    @_('llamadaf PYC')
    def sentencia(self, p):
        parseFinal.write('63 ')

    @_('retorno PYC')
    def sentencia(self, p):
        parseFinal.write('64 ')

    @_('asignaciona PYC')
    def sentencia(self, p):
        parseFinal.write('65 ')

    @_('')
    def sentencia(self, p):
        parseFinal.write('66 ')

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    parseFinal = open('parseFinal.txt','w')
    parseFinal.write("Ascendente \t")
    fd = open(sys.argv[1], 'r')
    txt = fd.read()

    parser.parse(lexer.tokenize(txt))


    parseFinal.close()
