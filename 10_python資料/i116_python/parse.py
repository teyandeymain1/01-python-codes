"""
The grammar of Minila programming language:

   P ::= S

   S ::=                                   (empty statement)
         | var ':=' E ';'                  (assign statement)
         | 'if' E 'then' S 'else' S 'fi'   (if statement)
         | 'while' E 'do' S 'od'           (while statement)
         | S S                             (sequential composition)

   E ::=   num
         | '-' num
         | var
         | '-' var
         | '(' E ')'
         | '-' '(' E ')'
         | E '*' E | E '/' E | E '%' E
         | E '+' E | E '-' E
         | E '<' E | E '>' E | E '=' E | E '!=' E
         | E '&&' E | E '||' E

   num ::= [0-9]+
   var ::= [a-zA-Z][0-9a-zA-Z]*

The grammar for expressions is rewritten as follows so that
a recursive descent parser can be used.

    F ::= ['-'] num | ['-'] var | ['-'] '(' E ')'
    E1 ::= F E11
    E11 ::= eps | '*' F E11 | '/' F E11
    E2 ::= E1 E22
    E22 ::= eps | '+' E1 E22 | '-' E1 E22
    E3 ::= E2 E33
    E33 ::= eps | '<' E2 E33 | '>' E2 E33 | '=' E2 E33 | '!=' E2 E33
    E4 ::= E3 E44
    E44 ::= eps | '&&' E3 E44 | '||' E3 E44
    E ::= E4

The precedence of the operators is as follows:

    (unary) '-'            (strongest)
    '*', '/', '%'
    '+', (bynary) '-'
    '<', '>', '=', '!='
    '&&', '||'             (weakest)

Every operator is left-associative, e.g. 3-2-1 is parsed as ((3-2)-1).
"""

from scan import *
from parseTree import *

class TokenList(object):
    tokenList = []
    idx = 0

    def __init__(self, tl):
        self.tokenList = tl
        self.idx = 0

    def parse(self):
        assert self.idx >= 0 and self.idx < len(self.tokenList), "idx: " + str(self.idx) + " is out of scope of tokenList: " + l2s(self.tokenList)
        return self.S(0)

    def F(self):
        t1 = Token(TName.UNDEF,'')
        t2 = Token(TName.UNDEF,'')
        t3 = Token(TName.UNDEF,'')
        e = ExpParseTree()
        n = ExpParseTree()
        v  = StmParseTree()
        if self.idx == len(self.tokenList):
            raise SyntaxError('a number or a variable or - or (', ' but nothing')
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.NUM:
            return NumParseTree(t1.num)
        elif t1.tname == TName.VAR:
            return VarParseTree(t1.name)
        elif t1.tname == TName.LPAR:
            e = self.E();
            if self.idx == len(self.tokenList):
                raise SyntaxError(')', ' but nothing')
            t2 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t2.tname != TName.RPAR:
                raise SyntaxError('), but ' + str(t2))
            return e
        elif t1.tname == TName.MINUS:
            if self.idx == len(self.tokenList):
                raise SyntaxError('a number or a variable or (, but nothing')
            t2 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t2.tname != TName.NUM:
                return NumParseTree(-1 * t2.num)
            elif t2.tname != TName.VAR:
                return UmiParseTree(VarParseTree(t2.name))
            elif t2.tname != TName.LPAR:
                e = self.E()
                if self.idx == len(self.tokenList):
                    raise SyntaxError(')', ' but nothing')
                t3 = self.tokenList[self.idx]
                self.idx = self.idx + 1
                if t3.tname != TName.RPAR:
                    raise SyntaxError('), but ' + str(t3))
                return UmiParseTree(e)
            else:
                raise SyntaxError('a number or a variable or (, but ' + str(t2))
        else:
            raise SyntaxError('a number or a variable or - or (, but ' + str(t1))

    def E1(self):
        e = self.F()
        return self.E11(e)

    def E11(self,e):
        t1 = Token(TName.UNDEF,'')
        e1 = ExpParseTree()
        e1 = ExpParseTree()
        if self.idx == len(self.tokenList):
            return e
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.MUL:
            e1 = self.F()
            e2 = MulParseTree(e,e1)
            return self.E11(e2)
        elif t1.tname == TName.QUO:
            e1 = self.F()
            e2 = QuoParseTree(e,e1)
            return self.E11(e2)
        elif t1.tname == TName.REM:
            e1 = self.F()
            e2 = RemParseTree(e,e1)
            return self.E11(e2)
        else:
            self.idx = self.idx - 1
            return e;

    def E2(self):
        e = self.E1()
        return self.E22(e)

    def E22(self,e):
        t1 = Token(TName.UNDEF,'')
        e1 = ExpParseTree()
        e1 = ExpParseTree()
        if self.idx == len(self.tokenList):
            return e
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.PLUS:
            e1 = self.E1()
            e2 = AddParseTree(e,e1)
            return self.E22(e2)
        elif t1.tname == TName.MINUS:
            e1 = self.E1()
            e2 = SubParseTree(e,e1)
            return self.E22(e2)
        else:
            self.idx = self.idx - 1
            return e;

    def E3(self):
        e = self.E2()
        return self.E33(e)

    def E33(self,e):
        t1 = Token(TName.UNDEF,'')
        e1 = ExpParseTree()
        e1 = ExpParseTree()
        if self.idx == len(self.tokenList):
            return e
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.LT:
            e1 = self.E2()
            e2 = LTParseTree(e,e1)
            return self.E33(e2)
        elif t1.tname == TName.GT:
            e1 = self.E2()
            e2 = GTParseTree(e,e1)
            return self.E33(e2)
        elif t1.tname == TName.EQ:
            e1 = self.E2()
            e2 = EQParseTree(e,e1)
            return self.E33(e2)
        elif t1.tname == TName.NEQ:
            e1 = self.E2()
            e2 = NEQParseTree(e,e1)
            return self.E33(e2)
        else:
            self.idx = self.idx - 1
            return e;

    def E4(self):
        e = self.E3()
        return self.E44(e)

    def E44(self,e):
        t1 = Token(TName.UNDEF,'')
        e1 = ExpParseTree()
        e1 = ExpParseTree()
        if self.idx == len(self.tokenList):
            return e
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.AND:
            e1 = self.E3()
            e2 = AndParseTree(e,e1)
            return self.E44(e2)
        elif t1.tname == TName.OR:
            e1 = self.E3()
            e2 = OrParseTree(e,e1)
            return self.E44(e2)
        else:
            self.idx = self.idx - 1
            return e;

    def E(self):
        return self.E4()

    def S(self,level):
        t1 = Token(TName.UNDEF,'')
        t2 = Token(TName.UNDEF,'')
        t3 = Token(TName.UNDEF,'')
        t4 = Token(TName.UNDEF,'')
        e = ExpParseTree()
        e1 = ExpParseTree()
        e2 = ExpParseTree()
        s = StmParseTree()
        s1 = StmParseTree()
        s2 = StmParseTree()
        as2 = StmParseTree()
        is2 = StmParseTree()
        ws = StmParseTree()
        v  = StmParseTree()
        if self.idx == len(self.tokenList):
            return EmptyParseTree()
        t1 = self.tokenList[self.idx]
        self.idx = self.idx + 1
        if t1.tname == TName.VAR:
            if self.idx == len(self.tokenList):
                raise SyntaxError(':=', ' but nothing')
            t2 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t2.tname != TName.ASSIGN:
                raise SyntaxError(':=, but ' + str(t2))
            e = self.E()
            if self.idx == len(self.tokenList):
                raise SyntaxError(':=, but nothing')
            t3 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t3.tname != TName.SEMC:
                raise SyntaxError(';, but ' + str(t3))
            as2 = AssignParseTree(t1, e)
            s = self.S(level)
            if isinstance(s, EmptyParseTree):
                return as2
            else:
                return SCompParseTree(as2,s)
        elif t1.tname == TName.IF:
            e = self.E()
            if self.idx == len(self.tokenList):
                raise SyntaxError('then, but nothing')
            t2 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t2.tname != TName.THEN:
                raise SyntaxError('then, but ' + str(t2))
            s1 = self.S(level + 1)
            if self.idx == len(self.tokenList):
                raise SyntaxError('else, but nothing')
            t3 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t3.tname != TName.ELSE:
                raise SyntaxError('else, but ' + str(t3))
            s2 = self.S(level + 1)
            if self.idx == len(self.tokenList):
                raise SyntaxError('fi, but nothing')
            t4 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t4.tname != TName.FI:
                raise SyntaxError('fi, but ' + str(t4))
            is2 = IfParseTree(e,s1,s2)
            s = self.S(level)
            if isinstance(s, EmptyParseTree):
                return is2
            else:
                return SCompParseTree(is2,s)
        elif t1.tname == TName.WHILE:
            e = self.E()
            if self.idx == len(self.tokenList):
                raise SyntaxError('do, but nothing')
            t2 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t2.tname != TName.DO:
                raise SyntaxError('do, but ' + str(t2))
            s1 = self.S(level + 1)
            if self.idx == len(self.tokenList):
                raise SyntaxError('od, but nothing')
            t3 = self.tokenList[self.idx]
            self.idx = self.idx + 1
            if t3.tname != TName.OD:
                raise SyntaxError('od, but ' + str(t3))
            ws = WhileParseTree(e,s1)
            s = self.S(level)
            if isinstance(s, EmptyParseTree):
                return ws
            else:
                return SCompParseTree(ws,s)
        else:
            if level == 0:
                raise SyntaxError('nothing, but ' + str(t1))
            else:
                self.idx = self.idx - 1;
            return EmptyParseTree()
    
"""
assert 1 < 0 or False, "error message"
"""

