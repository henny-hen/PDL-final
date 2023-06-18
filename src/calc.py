# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, '../..')

from sly import Lexer, Parser



class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { NUM, ID, PRINT,
               MAS, MASI, ASSIGN, INPUT,
               EQQ, DIF, RETURN, STRING, FUNCTION
               , INT, BOOLEAN, LET, FOR, 
               CAD, COM, PYC, PARI, PARF, CORI, 
               CORF, TRUE, FALSE, LESI, MUL }


    literals = { '(', ')', '{', '}', ';', ',' }

    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'//.*'
    # Regular expression rules for tokens
    MASI    = r'\+='
    LESI   = r'-'
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
    MUL   = r'\*'




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
    @_(r'-')
    def LESI(self,t):
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
    CAD = r'[\'][a-zA-Z0-9_\s,%.():;<>?!\+\-\*\/{}\[\]=]*[\']'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
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
        print('Lexer: Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
        fd2 = open("errores.txt", "a") 
        fd2.write('LEXER: Error en linea %d: caracter incorrecto (%r)' % (self.lineno, t.value[0]))
        fd2.write('\n')
        self.index += 1





class CalcParser(Parser):
    tokens = CalcLexer.tokens
    debugfile = 'parser.out'

    def __init__(self):
        self.names = { }


    @_('Sl')
    def Sp(self, p):
        parseFinal.write('1 ')
    
    @_('S Sl')
    def Sl(self, p):
        parseFinal.write('2 ')

    @_('')
    def Sl(self, p):
        parseFinal.write('3 ')
    
    @_('Vd PYC')
    def S(self, p):
        parseFinal.write('4 ')

    @_('Aas PYC')
    def S(self, p):
        parseFinal.write('5 ')

    @_('Fd')
    def S(self, p):
        parseFinal.write('6 ')
    
    @_('Fl')
    def S(self, p):
        parseFinal.write('7 ')

    @_('Ps PYC')
    def S(self, p):
        parseFinal.write('8 ')

    @_('Iis PYC')
    def S(self, p):
        parseFinal.write('9 ')
    
    @_('Fcs PYC')
    def S(self, p):
        parseFinal.write('10 ')

    @_('LET ID Ty Opi')
    def Vd(self, p):
        parseFinal.write('11 ')




    @_('STRING')
    def Ty(self, p):
        parseFinal.write('12 ')


    @_('INT')
    def Ty(self, p):
        parseFinal.write('13 ')


    @_('BOOLEAN')
    def Ty(self, p):
        parseFinal.write('14 ')


    @_('ASSIGN Ex')
    def Opi(self, p):
        parseFinal.write('15 ')

    @_('')
    def Opi(self, p):
        parseFinal.write('16 ')

    @_('ID ASSIGN Ex')
    def Aas(self, p):
        parseFinal.write('17 ')
       
     
            
    @_('ID MASI Ex')
    def Aas(self, p):
        parseFinal.write('18 ')


    @_('FUNCTION ID Ty PARI Pl PARF CORI Sl Rs CORF ')
    def Fd(self, p):
        parseFinal.write('19 ')

    @_('FUNCTION ID PARI Pl PARF CORI Sl CORF ')
    def Fd(self, p):
        parseFinal.write('20 ')

    @_('P Mp')
    def Pl(self, p):
        parseFinal.write('21 ')

    @_('')
    def Pl(self, p):
        parseFinal.write('22 ')

    @_('Ty ID')
    def P(self, p):
        parseFinal.write('23 ')

    @_('COM P Mp')
    def Mp(self, p):
        parseFinal.write('24 ')

    @_('')
    def Mp(self, p):
        parseFinal.write('25 ')

    @_('FOR PARI Fi PYC Ex PYC Fu PARF CORI Sl CORF')
    def Fl(self, p):
        parseFinal.write('26 ')

    @_('')
    def Fi(self, p):
        parseFinal.write('27 ')

    @_('Aas')
    def Fi(self, p):
        parseFinal.write('28 ')

    @_('Aas')
    def Fu(self, p):
        parseFinal.write('29 ')

    @_('Se Op Ex')
    def Ex(self, p):
        parseFinal.write('30 ')

                    
    @_('DIF Ex')
    def Ex(self, p):
        parseFinal.write('31 ')

       
    @_('Se')
    def Ex(self, p):
        parseFinal.write('32 ')
 

    @_('Fc')
    def Ex(self, p):
        parseFinal.write('33 ')

    @_('ID')
    def Se(self, p):
        parseFinal.write('34 ')



    @_('Li')
    def Se(self, p):
        parseFinal.write('35 ')

    @_('PARI Ex PARF')
    def Se(self, p):
        parseFinal.write('36 ')
        
    @_('MAS')
    def Op(self, p):
        parseFinal.write('37 ')

        
    @_('EQQ')
    def Op(self, p):
        parseFinal.write('38 ')


    @_('LESI')
    def Op(self, p):
        parseFinal.write('39 ')


    @_('MUL')
    def Op(self, p):
        parseFinal.write('40 ')

    @_('NUM')
    def Li(self, p):
        parseFinal.write('41 ')



    @_('CAD')
    def Li(self, p):
        parseFinal.write('42 ')


    @_('Bo')
    def Li(self, p):
        parseFinal.write('43 ')


    @_('TRUE')
    def Bo(self, p):
        parseFinal.write('44 ')


    @_('FALSE')
    def Bo(self, p):
        parseFinal.write('45 ')


    @_('RETURN Ex PYC')
    def Rs(self, p):
        parseFinal.write('46 ')

    @_('PRINT Ex')
    def Ps(self, p):
        parseFinal.write('47 ')

    @_('ID PARI Al PARF')
    def Fc(self, p):
        parseFinal.write('48 ')

    @_('Ex Ma')
    def Al(self, p):
        parseFinal.write('49 ')

    @_('')
    def Al(self, p):
        parseFinal.write('50 ')  

    @_('COM Ex Ma')
    def Ma(self, p):
        parseFinal.write('51 ')

    @_('')
    def Ma(self, p):
        parseFinal.write('52 ')

    @_('INPUT ID')
    def Iis(self, p):
        parseFinal.write('53 ')

    @_('Fc')
    def Fcs(self, p):
        parseFinal.write('54 ')


    def error(self, p):
        print('PARSER: Error en linea %d' % (p.lineno))
        fd2 = open("errores.txt", "a") 
        fd2.write('PARSER: Error en linea %d' % (p.lineno))
        fd2.write('\n')
        print('error in PYC')
        print(p)
        if p == None:
            print('PARSER: Error en EOF')
            
        elif p.type in ('FOR', 'FUNCTION'):
            skip = 'CORF'
        else:
            skip = 'PYC'
        while tok := next(self.tokens, None):
            if tok.type == skip:
                break
        self.restart()



if __name__ == '__main__':

    TS = {}
    numTS = 1
    posTS = 1

    lexer = CalcLexer()
    parser = CalcParser()
    parseFinal = open('parseFinal.txt','w')
    parseFinal.write("Ascendente \t")
    fd = open(sys.argv[1], 'r')

    fd2 = open("errores.txt", "w") 
    fd3 = open("tokens.txt", "w")
    txt = fd.read()

    parser.parse(lexer.tokenize(txt))

    for tok in lexer.tokenize(txt):
        fd3 = open("tokens.txt", "a") 
        if((tok.type == 'ID')):
            if(TS.get(tok.value, -1) == -1):
                # print("lexema")
                TS[tok.value] = posTS
                TS[tok.value + '.type'] = '-'
                posTS += 1
            print("< %r , %d >" % (tok.value, TS.get(tok.value)))
            fd3.write("< %r , %d > \n" % (tok.value, TS.get(tok.value)))
        else:
            print("< %r , %s >" % (tok.type, tok.value))
            fd3.write("< %r , %s >" % (tok.type, tok.value))
            fd3.write('\n')

    parseFinal.close()
    fd2.close()
    fd3.close()


