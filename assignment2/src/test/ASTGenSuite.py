import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test_simple_program(self):
        input = """
        procedure main(); 
        begin 
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_simple_function(self):
        input = """
        function foo ():integer; begin
            putIntLn(4);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], [], [CallStmt(Id("putIntLn"), [IntLiteral(4)])], IntType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_call_without_parameter(self):
        input = """
        procedure main ();
        begin
            getIntLn();
        end
        function foo ():integer; 
        begin
            putIntLn(4);
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [], [CallStmt(Id("getIntLn"), [])], VoidType(
        )), FuncDecl(Id("foo"), [], [], [CallStmt(Id("putIntLn"), [IntLiteral(4)])], IntType())]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_var_type1(self):
        input = """
        var i,j:integer;
        """
        expect = str(
            Program([VarDecl(Id("i"), IntType()), VarDecl(Id("j"), IntType())]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_var_type2(self):
        input = """
        var i,j:integer;
            k,n:real;
        """
        expect = str(Program([VarDecl(Id("i"), IntType()), VarDecl(
            Id("j"), IntType()), VarDecl(Id("k"), FloatType()), VarDecl(Id("n"), FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_var_int(self):
        input = """
        var i:integer;
        """
        expect = str(Program([VarDecl(Id("i"), IntType())]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_var_float(self):
        input = """
        var i:real;
        """
        expect = str(Program([VarDecl(Id("i"), FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_var_bool(self):
        input = """
        var i:boolean;
        """
        expect = str(Program([VarDecl(Id("i"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_var_string(self):
        input = """
        var i:string;
        """
        expect = str(Program([VarDecl(Id("i"), StringType())]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_var_array(self):
        input = """
        var i:array [1 .. 2] of integer;
        """
        expect = str(Program([VarDecl(Id("i"), ArrayType(1, 2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_multiple_var(self):
        input = """
        var i:integer;
            j,k: boolean;
        """
        expect = str(Program([VarDecl(Id("i"), IntType()), VarDecl(
            Id("j"), BoolType()), VarDecl(Id("k"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_multiple_var(self):
        input = """
        var i:integer;
            j,k: boolean;
        """
        expect = str(Program([VarDecl(Id("i"), IntType()), VarDecl(
            Id("j"), BoolType()), VarDecl(Id("k"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_var_array1(self):
        input = """
        var i:array [-1 .. -2] of integer;
        """
        expect = str(Program([VarDecl(Id("i"), ArrayType(-1, -2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_var_array2(self):
        input = """
        var i:array [-1 .. 2] of integer;
        """
        expect = str(Program([VarDecl(Id("i"), ArrayType(-1, 2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_var_array3(self):
        input = """
        var i:array [1 .. -2] of integer;
        """
        expect = str(Program([VarDecl(Id("i"), ArrayType(1, -2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_void_type(self):
        input = """
        procedure foo();
        begin
            if x > 1 then
                print("x lon hon 1");
            else
                print("x nho hon hoac bang 1");
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], [], 
        [If(BinaryOp(">", Id("x"), IntLiteral(1)), 
        [CallStmt(Id("print"), [StringLiteral("x lon hon 1")])], 
        [CallStmt(Id("print"), [StringLiteral("x nho hon hoac bang 1")])])], VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_void_type1(self):
        input = """
        procedure foo();
        var i,j: array [1 .. 2] of integer;
        begin
            
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], 
        [VarDecl(Id("i"), ArrayType(1, 2, IntType())), 
        VarDecl(Id("j"), ArrayType(1, 2, IntType()))], [], VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_function_decl(self):
        input = """
        function foo(a,b:integer;c:real):array [1 .. 2] of integer;
        var x,y: real;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), 
        VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType())], [], 
        ArrayType(1, 2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_procedure_decl(self):
        input = """
        procedure foo(a,b:integer;c:real);
        var x,y: real;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), 
        VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), 
        FloatType())], [], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_all(self):
        input = """
        function foo(n:integer;x:array[1 .. 10] of integer):array [1 .. 10] of integer;
        var b:array[1 .. 10] of integer;
        begin
            with i:integer; do 
                if n > 0 then
                    for i := n downto a[n] do 
                    begin
                        b[i] := a[i] + x[i];
                        if i = a[x[i]] then
                            return x;
                        else
                            continue;
                    end
                else
                    for i := 1 to n mod a[n] do 
                    begin
                        b[i] := a[i] and then x[i] or else b[i];
                        if a[x[i]] then
                            return x;
                        else
                            break;
                    end
            return foo(foo(x),a[x[n]]);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("n"), IntType()), VarDecl(Id("x"), ArrayType(1, 10, IntType()))], 
        [VarDecl(Id("b"), ArrayType(1, 10, IntType()))], 
        [With([VarDecl(Id("i"), IntType())], [If(BinaryOp(">", Id("n"), IntLiteral(0)), 
        [For(Id("i"), Id("n"), ArrayCell(Id("a"), Id("n")), False, 
        [Assign(ArrayCell(Id("b"), Id("i")), BinaryOp("+", ArrayCell(Id("a"), Id("i")), ArrayCell(Id("x"), Id("i")))), 
        If(BinaryOp("=", Id("i"), ArrayCell(Id("a"), ArrayCell(Id("x"), Id("i")))), 
        [Return(Id("x"))], [Continue()])])], 
        [For(Id("i"), IntLiteral(1), BinaryOp("mod", Id("n"), ArrayCell(Id("a"), Id("n"))), True, 
        [Assign(ArrayCell(Id("b"), Id("i")), BinaryOp("orelse", BinaryOp("andthen", ArrayCell(Id("a"), Id("i")),
        ArrayCell(Id("x"), Id("i"))), ArrayCell(Id("b"), Id("i")))), 
        If(ArrayCell(Id("a"), ArrayCell(Id("x"), Id("i"))), 
        [Return(Id("x"))], [Break()])])])]), 
        Return(CallExpr(Id("foo"), [CallExpr(Id("foo"), [Id("x")]), ArrayCell(Id("a"), ArrayCell(Id("x"), Id("n")))]))], 
        ArrayType(1, 10, 
        IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_all1(self):
        input = """
        procedure main(); 
        var i:integer;
        begin
            i := getIntLn();
            foo(a,i);
            with i:integer; do
                for i := 1 to 10 do
                    putIntLn(a[i]);
        end
        var a:array[1 .. 10] of integer;
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
        [VarDecl(Id("i"), IntType())], [Assign(Id("i"), CallExpr(Id("getIntLn"), [])), 
        CallStmt(Id("foo"), [Id("a"), Id("i")]), With([VarDecl(Id("i"), IntType())], 
        [For(Id("i"), IntLiteral(1), IntLiteral(10), True, 
        [CallStmt(Id("putIntLn"), [ArrayCell(Id("a"), Id("i"))])])])],
        VoidType()), 
        VarDecl(Id("a"), ArrayType(1, 10, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    # ahihiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
    def test_simple_program1(self):
        input = """
        procedure foo (b : real) ;
        begin
            1[1] := 1;
            (1>=0)[2] := 2+a[1]+c+("abc"< 0);
            ahihi(1)[m+1] := 3;
            (1+a[1]+(1<0))[10] := 4;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("b"), FloatType())], [], 
        [Assign(ArrayCell(IntLiteral(1), IntLiteral(1)), IntLiteral(1)), 
        Assign(ArrayCell(BinaryOp(">=", IntLiteral(1), IntLiteral(0)), IntLiteral(2)), 
        BinaryOp("+", BinaryOp("+", BinaryOp("+", IntLiteral(2), ArrayCell(Id("a"), IntLiteral(1))), Id("c")), 
        BinaryOp("<", StringLiteral("abc"), IntLiteral(0)))), 
        Assign(ArrayCell(CallExpr(Id("ahihi"), [IntLiteral(1)]), 
        BinaryOp("+", Id("m"), IntLiteral(1))), IntLiteral(3)), 
        Assign(ArrayCell(BinaryOp("+", BinaryOp("+", IntLiteral(1), 
        ArrayCell(Id("a"), IntLiteral(1))), 
        BinaryOp("<", IntLiteral(1), IntLiteral(0))), IntLiteral(10)), IntLiteral(4))], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_more_complex_program(self):
        input = """
        procedure main () ;
        begin
            putIntLn(4);
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [], [
        CallStmt(Id("putIntLn"), [IntLiteral(4)])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_variable_declaration(self):
        input = """
        procedure main() ;
        var a, b, c : integer ;
            d: array [1 .. 5] of integer ;
            e , f : real ;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
        [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType()), 
        VarDecl(Id("d"), ArrayType(1, 5, IntType())), VarDecl(Id("e"), FloatType()), 
        VarDecl(Id("f"), FloatType())], [], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_function_declaration(self):
        input = """
        function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
        var x,y: real ;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), 
        FloatType())], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType())], [], 
        ArrayType(1, 2, IntType()))]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_procedure_declaration(self):
        input = """
        procedure foo(a, b: integer ; c: real) ;
        var x,y: real ;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), 
        VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType())], [], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_assign_statement1(self):
        input = """
        procedure foo(a, b: integer ; c: real) ;
        var x,y: real ;
        begin
            a := 1;
            b := a[12] ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), 
        VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType())], 
        [Assign(Id("a"), IntLiteral(1)), 
        Assign(Id("b"), ArrayCell(Id("a"), IntLiteral(12)))], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_assign_statement2(self):
        input = """
        procedure foo() ;
        var x,y: real ;
        begin
            a := "conga";
            b := func(1,a+1) ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], 
        [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), FloatType())], 
        [Assign(Id("a"), StringLiteral("conga")), 
        Assign(Id("b"), CallExpr(Id("func"), [IntLiteral(1), BinaryOp("+", Id("a"), IntLiteral(1))]))], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_assign_statement5(self):
        input = """
        function foo(c: real): real ;
        var x: integer ;
        begin
            a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), IntType())], 
        [Assign(ArrayCell(Id("a"), BinaryOp("div", Id("a"), IntLiteral(3))), 
        BinaryOp("andthen", BinaryOp(">", Id("a"), Id("m")), BinaryOp("<", Id("b"), Id("n")))), 
        Assign(ArrayCell(CallExpr(Id("foo"), []), BinaryOp("*", Id("m"), IntLiteral(1))),                                                                                                                                                                                                                                                                 
        ArrayCell(Id("a"), BinaryOp("div", Id("a"), IntLiteral(3)))), 
        Assign(ArrayCell(Id("a"), BinaryOp("+", Id("m"), IntLiteral(1))), 
        ArrayCell(CallExpr(Id("foo"), []), BinaryOp("*", Id("m"), IntLiteral(1)))), 
        Assign(ArrayCell(Id("a"), BinaryOp("+", Id("m"), Id("n"))), 
        ArrayCell(Id("a"), BinaryOp("+", Id("m"), IntLiteral(1))))], 
        FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_if_statement1(self):
        input = """
        function foo(c: real): real ;
        var x:real ;
        begin
            if(a>1) 
            then a:=1 ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [VarDecl(Id("x"), FloatType())], 
        [If(BinaryOp(">", Id("a"), IntLiteral(1)), [Assign(Id("a"), IntLiteral(1))], [])], 
        FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_if_statement2(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            if(a>1) then 
                a:=1 ;
            else if (1<2)<>(2<3) then 
                x:=1 ;
            else foo(a+1,2);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], [If(BinaryOp(">", Id("a"), IntLiteral(1)), 
        [Assign(Id("a"), IntLiteral(1))], [If(BinaryOp("<>", BinaryOp("<", IntLiteral(1), IntLiteral(2)), 
        BinaryOp("<", IntLiteral(2), IntLiteral(3))), 
        [Assign(Id("x"), IntLiteral(1))], 
        [CallStmt(Id("foo"), [BinaryOp("+", Id("a"), IntLiteral(1)), IntLiteral(2)])])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_if_statement3(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            if(a>1) then 
                a:=1 ;
            if (1<2) then 
                begin 
                    x:=1 ; 
                end
            else 
                foo(a+1,2);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], [If(BinaryOp(">", Id("a"), IntLiteral(1)), 
        [Assign(Id("a"), IntLiteral(1))], []), If(BinaryOp("<", IntLiteral(1), IntLiteral(2)), 
        [Assign(Id("x"), IntLiteral(1))], [CallStmt(Id("foo"), 
        [BinaryOp("+", Id("a"), IntLiteral(1)), IntLiteral(2)])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_if_statement4(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            if(a>1) then 
                begin
                    a:=1 ;
                    if(1=1) then 
                        a:= b[1];
                    else 
                        b:=a[1]:= 1;
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], 
        [If(BinaryOp(">", Id("a"), IntLiteral(1)), 
        [Assign(Id("a"), IntLiteral(1)), If(BinaryOp("=", IntLiteral(1), IntLiteral(1)), 
        [Assign(Id("a"), ArrayCell(Id("b"), IntLiteral(1)))], 
        [Assign(ArrayCell(Id("a"), IntLiteral(1)), IntLiteral(1)), 
        Assign(Id("b"), ArrayCell(Id("a"), IntLiteral(1)))])], [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_while_statement1(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            while(a<>1) do 
                begin 
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], 
        [While(BinaryOp("<>", Id("a"), IntLiteral(1)), [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_while_statement2(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            whILe(a<>1) do 
                begin
                    if(a=1) then x:=1;
                    foo();
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], [While(BinaryOp("<>", Id("a"), IntLiteral(1)), 
        [If(BinaryOp("=", Id("a"), IntLiteral(1)), 
        [Assign(Id("x"), IntLiteral(1))], []), CallStmt(Id("foo"), [])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_while_statement3(self):
        input = """
        procedure foo(c: real) ;
        var x:real ;
        begin
            whILe(a<>1) do 
                begin
                    while(1) do x:=1;
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], 
        [VarDecl(Id("x"), FloatType())], [While(BinaryOp("<>", Id("a"), IntLiteral(1)), 
        [While(IntLiteral(1), [Assign(Id("x"), IntLiteral(1))])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_while_statement4(self):
        input = """
        procedure foo(c: real) ;
        begin
            while(a<>1) do 
                begin
                    while(1) do 
                        x:=1;
                    if(a=1) then 
                    begin 
                    end
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [While(BinaryOp("<>", Id("a"), IntLiteral(1)), [While(IntLiteral(1), 
        [Assign(Id("x"), IntLiteral(1))]), If(BinaryOp("=", Id("a"), IntLiteral(1)), [], [])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_with_statement1(self):
        input = """
        procedure foo(c: real) ;
        begin
            with a , b : integer ; c : array [1 .. 2] of real ; do
                d := c [a] + b ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [With([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), ArrayType(1, 2, FloatType()))], 
        [Assign(Id("d"), BinaryOp("+", ArrayCell(Id("c"), Id("a")), Id("b")))])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_with_statement2(self):
        input = """
        procedure foo(c: real) ;
        begin
            with a , b : integer ; c : array [1 .. 2] of real ; do 
                begin
                    d := c [a] + b ;
                    foo();
                    foo1(a,b,c);
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [With([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), 
        VarDecl(Id("c"), ArrayType(1, 2, FloatType()))], 
        [Assign(Id("d"), BinaryOp("+", ArrayCell(Id("c"), Id("a")), Id("b"))), 
        CallStmt(Id("foo"), []), CallStmt(Id("foo1"), [Id("a"), Id("b"), Id("c")])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_with_statement3(self):
        input = """
        procedure foo(c: real) ;
        begin
            with a , b : integer ; c : array [1 .. 2] of real ; do 
                begin
                    d := c [a] + b ;
                    foo();
                    foo1(a,b,c);
                    with a , b : integer ; do 
                    begin
                        foo2(a,b,"anc");
                    end
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [With([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), ArrayType(1, 2, FloatType()))], 
        [Assign(Id("d"), BinaryOp("+", ArrayCell(Id("c"), Id("a")), Id("b"))), 
        CallStmt(Id("foo"), []), CallStmt(Id("foo1"), [Id("a"), Id("b"), Id("c")]), 
        With([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], 
        [CallStmt(Id("foo2"), [Id("a"), Id("b"), StringLiteral("anc")])])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_with_statement4(self):
        input = """
        function foo(c: real): string;
        begin
            with c , d : integer ; c : array [1 .. 2] of real ; do
                with a , b : integer ; do
                    foo2(a,b,"anc");
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [With([VarDecl(Id("c"), IntType()), VarDecl(Id("d"), IntType()), VarDecl(Id("c"), ArrayType( 1, 2, FloatType()))], 
        [With([VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], 
        [CallStmt(Id("foo2"), [Id("a"), Id("b"), StringLiteral("anc")])])])], 
        StringType())]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_for_statement1(self):
        input = """
        function foo(c: real): string;
        begin
            for i := 1 to m + 10 do 
                s := s + 1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], [For(Id("i"), IntLiteral(1), BinaryOp(
            "+", Id("m"), IntLiteral(10)), True, [Assign(Id("s"), BinaryOp("+", Id("s"), IntLiteral(1)))])], StringType())]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_for_statement2(self):
        input = """
        function foo(c: real): string;
        begin
            FOR i:=1 to m+10 do 
                begin
                    s := s + 1;
                    if(a=1) then 
                        s:=s-1;
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [For(Id("i"), IntLiteral(1), BinaryOp("+", Id("m"), IntLiteral(10)), True, 
        [Assign(Id("s"), BinaryOp("+", Id("s"), IntLiteral(1))), 
        If(BinaryOp("=", Id("a"), IntLiteral(1)), 
        [Assign(Id("s"), BinaryOp("-", Id("s"), IntLiteral(1)))], [])])], 
        StringType())]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_for_statement3(self):
        input = """
        function foo(c: real): string;
        begin
            FOR i:=1 to m+10 do 
                begin
                    for j:=m+1 downto 100 do 
                        begin
                            s := s + 1;
                            if(a=1) then 
                                s:=s-1;
                        end
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [For(Id("i"), IntLiteral(1), BinaryOp("+", Id("m"), IntLiteral(10)), True, 
        [For(Id("j"), BinaryOp("+", Id("m"), IntLiteral(1)),IntLiteral(100), False, 
        [Assign(Id("s"), BinaryOp("+", Id("s"), IntLiteral(1))), If(BinaryOp("=", Id("a"), IntLiteral(1)), 
        [Assign(Id("s"), BinaryOp("-", Id("s"), IntLiteral(1)))], [])])])],
        StringType())]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_for_statement4(self):
        input = """
        procedure foo(c: real);
        begin
            FOR i:=1 to m+10 do 
                begin
                    while i>1 do
                            FOR i:=m+1 downto 10 do
                                while j>1 do 
                                    x:=foo(10);
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [For(Id("i"), IntLiteral(1), BinaryOp("+", Id("m"), IntLiteral(10)), True, 
        [While(BinaryOp(">", Id("i"), IntLiteral(1)), 
        [For(Id("i"), BinaryOp("+", Id("m"), IntLiteral(1)), IntLiteral(10), False, 
        [While(BinaryOp(">", Id("j"), IntLiteral(1)), 
        [Assign(Id("x"), CallExpr(Id("foo"), [IntLiteral(10)]))])])])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_break_statement(self):
        input = """
        procedure foo(c: real);
        begin
            for i:=1 to m+10 do 
                begin
                    break;
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [For(Id("i"), IntLiteral(1), BinaryOp("+", Id("m"), IntLiteral(10)), True, [Break()])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_continue_statement(self):
        input = """
        procedure foo(c: real);
        begin
            while (1) do 
                continue ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [While(IntLiteral(1), [Continue()])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_return_statement1(self):
        input = """
        procedure foo(c: real);
        begin
            while (1) do 
                return ;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], [
                     While(IntLiteral(1), [Return(None)])], VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_return_statement2(self):
        input = """
        function foo(c: real): integer;
        begin
            while (1) do
                return foo(a+1);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [While(IntLiteral(1), [Return(CallExpr(Id("foo"), [BinaryOp("+", Id("a"), IntLiteral(1))]))])], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_compound_statement(self):
        input = """
        function foo(c: real): integer;
        begin
            while (1=1) do 
                begin 
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [While(BinaryOp("=", IntLiteral(1), IntLiteral(1)), [])], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_call_statement1(self):
        input = """
        function foo(c: real): integer;
        begin
            foo (3,a+1);
            foo1();
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [CallStmt(Id("foo"), [IntLiteral(3), BinaryOp("+", Id("a"), IntLiteral(1))]), 
        CallStmt(Id("foo1"), [])], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_call_statement2(self):
        input = """
        function foo(c: real): integer;
        begin
            foo(3,a+1,a<>1,a[1]);
            return 1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [CallStmt(Id("foo"), [IntLiteral(3), BinaryOp("+", Id("a"), IntLiteral(1)), BinaryOp("<>", Id("a"), IntLiteral(1)), 
        ArrayCell(Id("a"), IntLiteral(1))]), Return(IntLiteral(1))], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_call_statement3(self):
        input = """
        function foo(c: real): integer;
        begin
            foo(3,foo(foo1(foo(2,a+1))));
            return func(a(1,2));
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [CallStmt(Id("foo"), [IntLiteral(3), CallExpr(Id("foo"), [CallExpr(Id("foo1"), 
        [CallExpr(Id("foo"), [IntLiteral(2), BinaryOp("+", Id("a"), IntLiteral(1))])])])]), 
        Return(CallExpr(Id("func"), [CallExpr(Id("a"), [IntLiteral(1), IntLiteral(2)])]))], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_call_statement4(self):
        input = """
        function foo(c: real): integer;
        begin
            textbackground(brown);
            Clrsr();
            return func(a(1,2));
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("c"), FloatType())], [], 
        [CallStmt(Id("textbackground"), [Id("brown")]), CallStmt(Id("Clrsr"), []), 
        Return(CallExpr(Id("func"), [CallExpr(Id("a"), [IntLiteral(1), IntLiteral(2)])]))], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_multiple1(self):
        input = """
        procedure test1() ;
        begin
	        if a=b then
	            begin
		            b := c ;
		            if(e <> f) then 
                        foo(a,c) ;
	            end
        end
        """
        expect = str(Program([FuncDecl(Id("test1"), [], [], [If(BinaryOp("=", Id("a"), Id("b")), 
        [Assign(Id("b"), Id("c")), If(BinaryOp("<>", Id("e"), Id("f")), 
        [CallStmt(Id("foo"), [Id("a"), Id("c")])], [])], [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_multiple2(self):
        input = """
        procedure test2() ;
        begin
	        if a=b then if c=d then 
                while (d=e) do
                    begin
                    end
            else c := 1;
        end
        """
        expect = str(Program([FuncDecl(Id("test2"), [], [], [If(BinaryOp("=", Id("a"), Id("b")), 
        [If(BinaryOp("=", Id("c"), Id("d")), [While(BinaryOp("=", Id("d"), Id("e")), [])], 
        [Assign(Id("c"), IntLiteral(1))])], [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_multiple3(self):
        input = """
        var i: integer ;
        function f(): integer ;
        begin
	        return 200;
        end
        procedure main() ;
        var main: integer ;
        begin
	        main := f() ;
	        putIntLn(main);
	        with i: integer;main: integer; f: integer; do 
                begin
		            main := f := i:= 100;
		            putIntLn (i);
		            putIntLn (main );
		            putIntLn (f);
	            end
	        putIntLn (main);
        end
        var g: real ;        
        """
        expect = str(Program([VarDecl(Id("i"), IntType()), FuncDecl(Id("f"), [], [], 
        [Return(IntLiteral(200))], IntType()), FuncDecl(Id("main"), [], 
        [VarDecl(Id("main"), IntType())], [Assign(Id("main"), CallExpr(Id("f"), [])), 
        CallStmt(Id("putIntLn"), [Id("main")]), With([VarDecl(Id("i"), IntType()),
        VarDecl(Id("main"), IntType()), VarDecl(Id("f"), IntType())], 
        [Assign(Id("i"), IntLiteral(100)), Assign(Id("f"), Id("i")), 
        Assign(Id("main"), Id("f")), CallStmt(Id("putIntLn"), [Id("i")]), 
        CallStmt(Id("putIntLn"), [Id("main")]), CallStmt(Id("putIntLn"), [Id("f")])]), 
        CallStmt(Id("putIntLn"), [Id("main")])], VoidType()), VarDecl(Id("g"), 
        FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_multiple4(self):
        input = """
        procedure Hello(a, b:integer);
        begin
            a := b + c;
            writeln("Hello, world!");
        end
        """
        expect = str(Program([FuncDecl(Id("Hello"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], [], 
        [Assign(Id("a"), BinaryOp("+", Id("b"), Id("c"))), 
        CallStmt(Id("writeln"), [StringLiteral("Hello, world!")])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_multiple5(self):
        input = """
        Var
            Num1, Num2, Sum : integer;
        procedure sum(a, c:Real);
        begin
            Write("nhap so 1:");
            Readln(Num1);
            Writeln("nhap so 2:");
            Readln(Num2);
            Sum := Num1 + Num2;
            Write(Sum);
            Readln();
        end
        """
        expect = str(Program([VarDecl(Id("Num1"), IntType()), VarDecl(Id("Num2"), IntType()), VarDecl(Id("Sum"), IntType()), 
        FuncDecl(Id("sum"), [VarDecl(Id("a"), FloatType()), VarDecl(Id("c"), FloatType())], [], 
        [CallStmt(Id("Write"), [StringLiteral("nhap so 1:")]), 
        CallStmt(Id("Readln"), [Id("Num1")]), 
        CallStmt(Id("Writeln"), [StringLiteral("nhap so 2:")]), 
        CallStmt(Id("Readln"), [Id("Num2")]), 
        Assign(Id("Sum"), BinaryOp("+", Id("Num1"), Id("Num2"))), 
        CallStmt(Id("Write"), [Id("Sum")]), 
        CallStmt(Id("Readln"), [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_multiple6(self):
        input = """
        Var name, surname: String;
        procedure Main();
        begin
	        write("Nhap ten cua ban:");
	        readln(name);
	        write("Nhap ho cua ban:");
	        readln(surname);
	        writeln();
	        writeln();
	        writeln("Ten day du cua ban la : ",name," ",surname);
	            readln();
        end
        """
        expect = str(Program([VarDecl(Id("name"), StringType()), VarDecl(Id("surname"), StringType()), 
        FuncDecl(Id("Main"), [], [], [CallStmt(Id("write"), [StringLiteral("Nhap ten cua ban:")]), 
        CallStmt(Id("readln"), [Id("name")]), CallStmt(Id("write"), [StringLiteral("Nhap ho cua ban:")]), 
        CallStmt(Id("readln"), [Id("surname")]), CallStmt(Id("writeln"), []), CallStmt(Id("writeln"), []), 
        CallStmt(Id("writeln"), [StringLiteral("Ten day du cua ban la : "), Id("name"), StringLiteral(" "), Id("surname")]), 
        CallStmt(Id("readln"), [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_multiple7(self):
        input = """
        Var PD, Dname, Cmodel : String;
        CostPD, TCostPD, Distance : Real;
        procedure main();
        begin
            textbackground(brown);
            Clrsr();
            TextColor(lightgreen);
            TCostPD := 0;
            Clrsr();
            GotoXy(28,3);
            Readln();
        end
        """
        expect = str(Program([VarDecl(Id("PD"), StringType()), VarDecl(Id("Dname"), StringType()), 
        VarDecl(Id("Cmodel"), StringType()), VarDecl(Id("CostPD"), FloatType()), 
        VarDecl(Id("TCostPD"), FloatType()), VarDecl(Id("Distance"), FloatType()), 
        FuncDecl(Id("main"), [], [], [CallStmt(Id("textbackground"), [Id("brown")]), 
        CallStmt(Id("Clrsr"), []), CallStmt(Id("TextColor"), [Id("lightgreen")]), Assign(Id("TCostPD"), IntLiteral(0)),
        CallStmt(Id("Clrsr"), []), CallStmt(Id("GotoXy"), [IntLiteral(28), IntLiteral(3)]), 
        CallStmt(Id("Readln"), [])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_multiple8(self):
        input = """
        procedure main() ;
        begin
            a[b[2]] := 10;
            foo();
            return ;
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [], 
        [Assign(ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(2))), IntLiteral(10)), 
        CallStmt(Id("foo"), []), Return(None)], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_multiple9(self):
        input = """
        procedure main() ;
        begin
            if a=b then 
                if c = d then 
                    e := f;
                else 
                    i := 1;
            else 
                x := 2 ;
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [], 
        [If(BinaryOp("=", Id("a"), Id("b")), [If(BinaryOp("=", Id("c"), Id("d")), 
        [Assign(Id("e"), Id("f"))], [Assign(Id("i"), IntLiteral(1))])], 
        [Assign(Id("x"), IntLiteral(2))])],
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_multiple10(self):
        input = """
        procedure main() ;
        var a: array[0 .. 9] of integer;
            i,j,temp: integer;
        begin
            for i := 0 to n - 2 do
                for j:= i+1 to n-1 do
                    if(a[i]>a[j]) then 
                        begin
                            temp := a[i];
                            a[i] := a[j];
                            a[j] := temp;
                        end
            print(a);
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], [VarDecl(Id("a"), ArrayType(0, 9, IntType())), VarDecl(Id("i"), IntType()), VarDecl(Id("j"), IntType()), VarDecl(Id("temp"), IntType())], [For(Id("i"), IntLiteral(0), BinaryOp("-", Id("n"), IntLiteral(2)), True, [For(Id("j"), BinaryOp("+", Id("i"), IntLiteral(1)), BinaryOp("-", Id(
            "n"), IntLiteral(1)), True, [If(BinaryOp(">", ArrayCell(Id("a"), Id("i")), ArrayCell(Id("a"), Id("j"))), [Assign(Id("temp"), ArrayCell(Id("a"), Id("i"))), Assign(ArrayCell(Id("a"), Id("i")), ArrayCell(Id("a"), Id("j"))), Assign(ArrayCell(Id("a"), Id("j")), Id("temp"))], [])])]), CallStmt(Id("print"), [Id("a")])], VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_multiple13(self):
        input = """
        function mod5(A:array[0 .. 10] of integer ; N:integer):integer;
        Var S,i :integer;
        begin
            S:=0;
            For i:=0 to N do
            If(A[i] mod 5=0) then
                S := S+A[i];
                return S;
        end
        """
        expect = str(Program([FuncDecl(Id("mod5"), [VarDecl(Id("A"), ArrayType(0, 10, IntType())), VarDecl(Id("N"), IntType())], 
        [VarDecl(Id("S"), IntType()), VarDecl(Id("i"), IntType())], 
        [Assign(Id("S"), IntLiteral(0)), For(Id("i"), IntLiteral(0), Id("N"), True, 
        [If(BinaryOp("=", BinaryOp("mod", ArrayCell(Id("A"), Id("i")), IntLiteral(5)), IntLiteral(0)), 
        [Assign(Id("S"), BinaryOp("+", Id("S"), ArrayCell(Id("A"), Id("i"))))], [])]), Return(Id("S"))], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_multiple14(self):
        input = """
        function foo(N:integer) :integer;
        Var i:integer;
        begin
            for i:=2 to N-1 do
                if(N mod i = 0) then
                    return 0;
                else
                    return 1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("N"), IntType())], 
        [VarDecl(Id("i"), IntType())], [For(Id("i"), IntLiteral(2), BinaryOp("-", Id("N"), IntLiteral(1)), True, 
        [If(BinaryOp("=", BinaryOp("mod", Id("N"), Id("i")), IntLiteral(0)), [Return(IntLiteral(0))], 
        [Return(IntLiteral(1))])])], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_multiple15(self):
        input = """
        function foo(A:array[0 .. 10] of integer; N,X : integer) : integer;
        Var i , Count : integer;
        begin
            Count := 0;
            For i:=0 to N do
                If ( A[i] = X ) then
                    Count := Count + 1;
                return Count;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, IntType())), VarDecl(Id("N"), IntType()), 
        VarDecl(Id("X"), IntType())], [VarDecl(Id("i"), IntType()), 
        VarDecl(Id("Count"), IntType())], [Assign(Id("Count"), IntLiteral(0)), 
        For(Id("i"), IntLiteral(0), Id("N"), True, 
        [If(BinaryOp("=", ArrayCell(Id("A"), Id("i")), Id("X")), 
        [Assign(Id("Count"), BinaryOp("+", Id("Count"), IntLiteral(1)))], [])]), 
        Return(Id("Count"))], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_multiple16(self):
        input = """
        procedure foo (A:array[0 .. 10] of integer;N, x,y:integer);
        Var i:integer;
        begin
            For i:=0 to N do
                If(A[i] = x) then
                    A[i] := y;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, IntType())), 
        VarDecl(Id("N"), IntType()), VarDecl(Id("x"), IntType()), VarDecl(Id("y"), IntType())], 
        [VarDecl(Id("i"), IntType())], [For(Id("i"), IntLiteral(0), Id("N"), True, 
        [If(BinaryOp("=", ArrayCell(Id("A"), Id("i")), Id("x")), 
        [Assign(ArrayCell(Id("A"), Id("i")), Id("y"))], [])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_multiple17(self):
        input = """
        procedure foo(A:array[0 .. 10] of integer; N:integer; X, Y:integer);
        Var i,k:integer;
        begin
            For i:=0 to N do
                If( (A[i-1]+A[i]) mod 10 = 0) then
                    begin
                        k := (A[i-1]+A[i]);
                        A[i-1] := k;
                        A[i] := k;
                    end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, IntType())), 
        VarDecl(Id("N"), IntType()), VarDecl(Id("X"), IntType()), VarDecl(Id("Y"), IntType())], 
        [VarDecl(Id("i"), IntType()), VarDecl(Id("k"), IntType())], 
        [For(Id("i"), IntLiteral(0), Id("N"), True, 
        [If(BinaryOp("=", BinaryOp("mod", BinaryOp("+", ArrayCell(Id("A"), BinaryOp("-", Id("i"), IntLiteral(1))), 
        ArrayCell(Id("A"), Id("i"))), IntLiteral(10)), IntLiteral(0)), [Assign(Id("k"), 
        BinaryOp("+", ArrayCell(Id("A"), BinaryOp("-", Id("i"), IntLiteral(1))), ArrayCell(Id("A"), Id("i")))), 
        Assign(ArrayCell(Id("A"), BinaryOp("-", Id("i"), IntLiteral(1))), Id("k")), 
        Assign(ArrayCell(Id("A"), Id("i")), Id("k"))], [])])], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_multiple18(self):
        input = """
        function foo (A:array[0 .. 10] of REAL; N:integer ) : Boolean;
        Var Flag:Boolean;
            i :integer;
        begin
            Flag:=True;
            For  i :=1 to N do
                If(A[i] <> A[N-i+1]) then
                    Flag := False;
                return flag;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, FloatType())), VarDecl(Id("N"), IntType())], 
        [VarDecl(Id("Flag"), BoolType()), VarDecl(Id("i"), IntType())], 
        [Assign(Id("Flag"), BooleanLiteral(True)), For(Id("i"), IntLiteral(1), Id("N"), True, 
        [If(BinaryOp("<>", ArrayCell(Id("A"), Id("i")), 
        ArrayCell(Id("A"), BinaryOp("+", BinaryOp("-", Id("N"), Id("i")), IntLiteral(1)))), 
        [Assign(Id("Flag"), BooleanLiteral(False))], [])]), Return(Id("flag"))], 
        BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_multiple19(self):
        input = """
        function foo ( A:array[0 .. 10] of REAL; N :integer) : Boolean;
        Var Flag : Boolean;
            i :integer;
        begin
            Flag := True;
            i:= 0;
            while(i<n) do 
                begin
                    If(A[i] < A[i-1]) then
                        Flag :=False;
                    i:=i+1;
                end
            return Flag;
        end
                """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, FloatType())), 
        VarDecl(Id("N"), IntType())], [VarDecl(Id("Flag"), BoolType()), VarDecl(Id("i"), IntType())], 
        [Assign(Id("Flag"), BooleanLiteral(True)), Assign(Id("i"), IntLiteral(0)), 
        While(BinaryOp("<", Id("i"), Id("n")), 
        [If(BinaryOp("<", ArrayCell(Id("A"), Id("i")), ArrayCell(Id("A"), BinaryOp("-", Id("i"), IntLiteral(1)))), 
        [Assign(Id("Flag"), BooleanLiteral(False))], []), 
        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]), Return(Id("Flag"))], 
        BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_multiple21(self):
        input = """
        procedure foo(A:array[0 .. 10] of real;N: integer; k, X:integer);
        var i :integer;
        begin
            For i:=N downto k + 1 do
                A[i] := A[i-1];
                A[k] := X;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("A"), ArrayType(0, 10, FloatType())), 
        VarDecl(Id("N"), IntType()), VarDecl(Id("k"), IntType()), VarDecl(Id("X"), IntType())], 
        [VarDecl(Id("i"), IntType())], [For(Id("i"), Id("N"), BinaryOp("+", Id("k"), IntLiteral(1)), False, 
        [Assign(ArrayCell(Id("A"), Id("i")), ArrayCell(Id("A"), BinaryOp("-", Id("i"), IntLiteral(1))))]), 
        Assign(ArrayCell(Id("A"), Id("k")), Id("X"))], 
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_multiple22(self):
        input = """
        function foo(x:integer):integer;
        begin
            if x = 0 then
                return 1;
            else
                return x*foo(x-1);
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("x"), IntType())], [], 
        [If(BinaryOp("=", Id("x"), IntLiteral(0)), [Return(IntLiteral(1))], 
        [Return(BinaryOp("*", Id("x"), CallExpr(Id("foo"), 
        [BinaryOp("-", Id("x"), IntLiteral(1))])))])], 
        IntType())]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_multiple23(self):
        input = """
        function fibo(x: integer): integer;
        var f1,f2: integer;
        begin
            if x<=2 then
                return 1;
            else
                return fibo(x-2)+ fibo(x-1);
        end
        """
        expect = str(Program([FuncDecl(Id("fibo"), [VarDecl(Id("x"), IntType())], [VarDecl(Id("f1"), IntType()), 
        VarDecl(Id("f2"), IntType())], [If(BinaryOp("<=", Id("x"), IntLiteral(2)), 
        [Return(IntLiteral(1))], [Return(BinaryOp("+", CallExpr(Id("fibo"), 
        [BinaryOp("-", Id("x"), IntLiteral(2))]), CallExpr(Id("fibo"), 
        [BinaryOp("-", Id("x"), IntLiteral(1))])))])], IntType())]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_multiple24(self):
        input = """
        function ok(i : integer):boolean;
        var k : integer;
        begin
            ok := true;
            for k := 2 to i div 2 do
            if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                begin
                    ok := false;
                    exit();
                end
        end
        """
        expect = str(Program([FuncDecl(Id("ok"), [VarDecl(Id("i"), IntType())], 
        [VarDecl(Id("k"), IntType())], [Assign(Id("ok"), BooleanLiteral(True)), 
        For(Id("k"), IntLiteral(2), BinaryOp("div", Id("i"), IntLiteral(2)), True, 
        [If(BinaryOp("=", CallExpr(Id("copy"), [Id("s"), BinaryOp("+", BinaryOp("-", Id("i"), 
        BinaryOp("*", IntLiteral(2), Id("k"))), IntLiteral(1)), Id("k")]), 
        CallExpr(Id("copy"), [Id("s"), BinaryOp("+", BinaryOp("-", Id("i"), Id("k")), 
        IntLiteral(1)), Id("k")])), [Assign(Id("ok"), BooleanLiteral(False)), CallStmt(Id("exit"), [])], [])])], 
        BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_multiple25(self):
        input = """
        procedure Daoso(n: integer);
        begin
            Assign(f,fo);
            Rewrite(f);
            If n > 0 then
            begin
                Write(f,n mod 10);
                Daoso(n div 10);
            end
            Close(f);
        end
        """
        expect = str(Program([FuncDecl(Id("Daoso"), [VarDecl(Id("n"), IntType())], [], 
        [CallStmt(Id("Assign"), [Id("f"), Id("fo")]), CallStmt(Id("Rewrite"), [Id("f")]), 
        If(BinaryOp(">", Id("n"), IntLiteral(0)), [CallStmt(Id("Write"), [Id("f"), BinaryOp("mod", Id("n"), IntLiteral(10))]), 
        CallStmt(Id("Daoso"), [BinaryOp("div", Id("n"), IntLiteral(10))])], []), 
        CallStmt(Id("Close"), [Id("f")])],
        VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_multiple26(self):
        input = "procedure main();begin begin end end"
        expect = str(Program([FuncDecl(Id("main"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_multiple27(self):
        input = "procedure foo(); begin foo(a,2)[2]:=4; begin return b; end return c; end"
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(CallExpr(Id("foo"),[Id("a"),IntLiteral(2)]),IntLiteral(2)),IntLiteral(4)),Return(Id("b")),Return(Id("c"))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test_complex28(self):
        input = """
        procedure Camelcase();
        var
            text, cc: string;
            c: string;
            i: integer;
            lastSpace: boolean;

        begin
            readln(text);
            lastSpace := true;
            cc := " ";
            for i := 1 to Length(text) do
            begin
                c := text[i];
                if ((c >= "65") and (c <= "90")) or ((c >= "97") and (c <= "122")) then
                begin
                    if (lastSpace) then
                    begin
                        if ((c >= "97") and (c <= "122")) then
                            c := chr(ord(c) - 32);
                    end
                    else
                        if ((c >= "65") and (c <= "90")) then
                            c := chr(ord(c) + 32);
                    cc := cc + c;
                    lastSpace := false;
                end
                else
                    lastSpace := true;
            end
            writeln(cc);
        end
        """
        expect = str(Program([FuncDecl(Id("Camelcase"),[],[VarDecl(Id("text"),StringType()),VarDecl(Id("cc"),StringType()),VarDecl(Id("c"),StringType()),VarDecl(Id("i"),IntType()),VarDecl(Id("lastSpace"),BoolType())],[CallStmt(Id("readln"),[Id("text")]),Assign(Id("lastSpace"),BooleanLiteral(True)),Assign(Id("cc"),StringLiteral(" ")),For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'Length'),[Id(r'text')]),True,[Assign(Id(r'c'),ArrayCell(Id(r'text'),Id(r'i'))),If(BinaryOp(r'or',BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'65')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'90'))),BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'97')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'122')))),[If(Id(r'lastSpace'),[If(BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'97')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'122'))),[Assign(Id(r'c'),CallExpr(Id(r'chr'),[BinaryOp(r'-',CallExpr(Id(r'ord'),[Id(r'c')]),IntLiteral(32))]))],[])],[If(BinaryOp(r'and',BinaryOp(r'>=',Id(r'c'),StringLiteral(r'65')),BinaryOp(r'<=',Id(r'c'),StringLiteral(r'90'))),[Assign(Id(r'c'),CallExpr(Id(r'chr'),[BinaryOp(r'+',CallExpr(Id(r'ord'),[Id(r'c')]),IntLiteral(32))]))],[])]),Assign(Id(r'cc'),BinaryOp(r'+',Id(r'cc'),Id(r'c'))),Assign(Id(r'lastSpace'),BooleanLiteral(False))],[Assign(Id(r'lastSpace'),BooleanLiteral(True))])]),CallStmt(Id(r'writeln'),[Id(r'cc')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_complex29(self):
        input = """
        procedure foo();
        BEGIN
            while (true) do 
                begin 
                    begin
                    end 
                end
        END
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BooleanLiteral("True"),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_all2(self):
        input = """
        var i:array [-3 .. -2] of integer;
			j,x:array [-1 .. -2] of integer;
		procedure main();
		begin
		end
        """
        expect = str(Program([VarDecl(Id("i"),ArrayType(-3,-2,IntType())),
        VarDecl(Id("j"),ArrayType(-1,-2,IntType())),VarDecl(Id("x"),ArrayType(-1,-2,IntType())),
        FuncDecl(Id("main"),[]
        ,[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_all3(self):
        input = """
        procedure main(a:INTEGER;b:real;c:real;d:boolean;e:boolean;f:boolean);
        var b:real;c:boolean;d:boolean;e,f,h:array[1 .. 2] of real;
        begin
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
        VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),BoolType()),VarDecl(Id("e"),BoolType()),VarDecl(Id("f"),BoolType())],
        [VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),BoolType()),
        VarDecl(Id("e"),ArrayType(1,2,FloatType())),VarDecl(Id("f"),ArrayType(1,2,FloatType())),
        VarDecl(Id("h"),ArrayType(1,2,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_all4(self):
        input = """
        procedure main(); 
        begin 
            with a:real;b,c:boolean;d:INTEGER; do 
                begin
                    with a:integer; do  
                        begin 
                            foo(); 
                        end
                    with b:real;c,d:integer; do 
                        begin 
                        end
                end
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),IntType())],[With([VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[])]),With([VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_all5(self):
        input = """
        function foo(): integer;
        begin
            if true
            then
            begin
                b := 1;
                a := b;
            end
            else
            begin
                b := 2;
                a := b;
            end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BooleanLiteral(True),[Assign(Id("b"),IntLiteral(1)),Assign(Id("a"),Id("b"))],[Assign(Id("b"),IntLiteral(2)),Assign(Id("a"),Id("b"))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_all6(self):
        input = """
        function foo(): String;
        begin
        if (true) then 
            begin
            x:=9;
            a:=x;
            end
        else 
           begin
              x:=5/2;
              break;
           end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BooleanLiteral(True),[Assign(Id("x"),IntLiteral(9)),Assign(Id("a"),Id("x"))],[Assign(Id("x"),BinaryOp("/",IntLiteral(5),IntLiteral(2))),Break()])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_all7(self):
        input = """
        procedure foo();
        var x: real; y:array[1 .. 3] of boolean;
        begin
            if (x <> 5 and then foo(x) ) then
                y[0]:=x; 
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),ArrayType(1,3,BoolType()))],[If(BinaryOp("andthen",BinaryOp("<>",Id("x"),IntLiteral(5)),CallExpr(Id("foo"),[Id("x")])),[Assign(ArrayCell(Id("y"),IntLiteral(0)),Id("x"))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_all8(self):
        input = """
        function foo(): boolean;
        begin
            if x = 5 then 
                x:=9;
            else 
            if x > 9 then 
                x:=3/2;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp("=",Id("x"),IntLiteral(5)),[Assign(Id("x"),IntLiteral(9))],[If(BinaryOp(">",Id("x"),IntLiteral(9)),[Assign(Id("x"),BinaryOp("/",IntLiteral(3),IntLiteral(2)))],[])])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_all9(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            a[1] := 1;
            a[5] := 0 OR ELSE a[1];
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("a"),ArrayType(1,10,IntType()))],[Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(Id("a"),IntLiteral(5)),BinaryOp("orelse",IntLiteral(0),ArrayCell(Id("a"),IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test_all10(self):
        input = """
        function foo(): integer;
        begin
            with a,b:integer; c: array [1 .. 2] of real; do
                begin
                    a := 1;
                    b := 2;
                    d := c[a] + c[b];
                end
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[With([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,2,FloatType()))],[Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Assign(Id("d"),BinaryOp("+",ArrayCell(Id("c"),Id("a")),ArrayCell(Id("c"),Id("b"))))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_all11(self):
        input = """
        function foo(): integer;
        begin
            y := x/2 + 1;
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("y"),BinaryOp("+",BinaryOp("/",Id("x"),IntLiteral(2)),IntLiteral(1)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_all12(self):
        input = """
        function foo(): integer;
        var a: array [1 .. 10] of integer;
        begin
            a[1] := 1;
            a[5] := 0 OR ELSE a[1];
        end
        """
        expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("a"),ArrayType(1,10,IntType()))],[Assign(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1)),Assign(ArrayCell(Id("a"),IntLiteral(5)),BinaryOp("orelse",IntLiteral(0),ArrayCell(Id("a"),IntLiteral(1))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_all13(self):
        input = """
        procedure main(); 
        begin 
            with a:real;b,c:boolean;d:integer; do 
                begin
                    with a:integer; do 
                        begin
                            print(a);
                        end
                    with b:real;c,d:integer; do 
                        begin
                            print(b + c/d);
                        end
            end
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
        [With([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),IntType())],
        [With([VarDecl(Id("a"),IntType())],[CallStmt(Id("print"),[Id("a")])]),
        With([VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],[CallStmt(Id("print"),
        [BinaryOp("+",Id("b"),BinaryOp("/",Id("c"),Id("d")))])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))
    
    def test_all14(self):
        input = """
            var a,b,c,s,p: real;
            procedure main() ;
            begin
                clrscr();
                writeln("tam giac:");
                writeln("---------------------------------");
                write("nhap a : ");readln(a);
                write("nhap b : ");readln(b);
                write("nhap c : ");readln(c);
                if ((a+b)>c)and((b+c)>a)and((a+c)>b) then
                    begin
                        p:=(a+b+c)/2;
                        s:=sqrt(p*(p-a)*(p-b)*(p-c));
                        writeln("Chu vi tam giac:",2*p);
                        writeln("Dien tich tam giac:",s);
                    End
                else 
                    writeln(a,", ", b,", ", c, " khong phai la ba canh cua tam giac");
                    readln();
            end
        """
        expect = str(Program([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("s"),FloatType()),VarDecl(Id("p"),FloatType()),FuncDecl(Id("main"),[],[],[CallStmt(Id("clrscr"),[]),CallStmt(Id("writeln"),[StringLiteral("tam giac:")]),CallStmt(Id("writeln"),[StringLiteral("---------------------------------")]),CallStmt(Id("write"),[StringLiteral("nhap a : ")]),CallStmt(Id("readln"),[Id("a")]),CallStmt(Id("write"),[StringLiteral("nhap b : ")]),CallStmt(Id("readln"),[Id("b")]),CallStmt(Id("write"),[StringLiteral("nhap c : ")]),CallStmt(Id("readln"),[Id("c")]),If(BinaryOp("and",BinaryOp("and",BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),Id("c")),BinaryOp(">",BinaryOp("+",Id("b"),Id("c")),Id("a"))),BinaryOp(">",BinaryOp("+",Id("a"),Id("c")),Id("b"))),[Assign(Id("p"),BinaryOp("/",BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")),IntLiteral(2))),Assign(Id("s"),CallExpr(Id("sqrt"),[BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("p"),BinaryOp("-",Id("p"),Id("a"))),BinaryOp("-",Id("p"),Id("b"))),BinaryOp("-",Id("p"),Id("c")))])),CallStmt(Id("writeln"),[StringLiteral("Chu vi tam giac:"),BinaryOp("*",IntLiteral(2),Id("p"))]),CallStmt(Id("writeln"),[StringLiteral("Dien tich tam giac:"),Id("s")])],[CallStmt(Id("writeln"),[Id("a"),StringLiteral(", "),Id("b"),StringLiteral(", "),Id("c"),StringLiteral(" khong phai la ba canh cua tam giac")])]),CallStmt(Id("readln"),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392))
        
    def test_if_stmt1(self):
        input = """procedure main(); 
            begin 
                if (a>2) and (b=4) then a:=2;b:=3;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp("and",BinaryOp(">",Id("a"),IntLiteral(2)),BinaryOp("=",Id("b"),IntLiteral(4))),[Assign(Id("a"),IntLiteral(2))],[]),Assign(Id("b"),IntLiteral(3))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_if_stmt3(self):
        input = """procedure main(); 
            begin 
                if a>2 then if a>4 then a:=4;else a:=2;foo(1,a);
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("a"),IntLiteral(2)),[If(BinaryOp(">",Id("a"),IntLiteral(4)),[Assign(Id("a"),IntLiteral(4))],[Assign(Id("a"),IntLiteral(2))])],[]),CallStmt(Id("foo"),[IntLiteral(1),Id("a")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_for_stmt(self):
        input = """procedure main(); 
            begin 
                for a:=1 to 10 do break;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),IntLiteral(1),IntLiteral(10),True,[Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_for_stmt3(self):
        input = """procedure main(); 
            begin 
                for a:=(6+x)*y to f(2)[2] do b:=foo();
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(6),Id("x")),Id("y")),ArrayCell(CallExpr(Id("f"),[IntLiteral(2)]),IntLiteral(2)),True,[Assign(Id("b"),CallExpr(Id("foo"),[]))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_while_break(self):
        input = """procedure main(); 
            begin 
                while a=b do 
                foo();
                a := b[10]:= foo()[3]:= x := 1 ;
                if a=5 then break;
            end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10))),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Break()],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_function3(self):
        input = """
            var a,b: integer;
            function f():integer; 
            begin 
                while a=b do 
                foo();
                a := b[10]:= foo()[3]:= x := 1 ;
                if a=5 then break;
                return a;
            end"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),FuncDecl(Id("f"),[],[],[While(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[])]),Assign(Id("x"),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),Assign(ArrayCell(Id("b"),IntLiteral(10)),ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10))),If(BinaryOp("=",Id("a"),IntLiteral(5)),[Break()],[]),Return(Id("a"))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_arr_decl(self):
        input = """var i:array [-3 .. -2] of integer;
        procedure main();
        begin
        end
        var j,x:array [-1 .. -2] of string;"""
        expect = str(Program([VarDecl(Id("i"),ArrayType(-3,-2,IntType())),FuncDecl(Id("main"),[],[],[],VoidType()),VarDecl(Id(("j")),ArrayType(-1,-2,StringType())),VarDecl(Id("x"),ArrayType(-1,-2,StringType()))]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_with(self):
        input = """procedure main(); 
        begin 
        with a:real;b,c:boolean;d:INTEGER; do begin
        with a:integer; do begin foo(); end
        with b:real;c,d:integer; do begin end
        end
        end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),BoolType()),VarDecl(Id("c"),BoolType()),VarDecl(Id("d"),IntType())],[With([VarDecl(Id("a"),IntType())],[CallStmt(Id("foo"),[])]),With([VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,400))   
