.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo([I)V
.var 0 is x [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label4
Label2:
	iconst_5
	newarray int
	iconst_0
	istore_2
Label3:
	iload_2
	iconst_5
	if_icmpge Label4
	dup
	iload_2
	aload_0
	iload_2
	iaload
	iastore
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label3
Label4:
	astore_0
	iconst_1
	istore_1
Label5:
	iload_1
	iconst_5
	if_icmpgt Label7
	aload_0
	iload_1
	iconst_1
	isub
	iload_1
	iload_1
	imul
	iastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	iconst_1
	istore_1
Label8:
	iload_1
	iconst_5
	if_icmpgt Label10
	aload_0
	iload_1
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is c [I from Label0 to Label1
	iconst_5
	newarray int
	astore_2
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpgt Label4
	aload_2
	iload_1
	iconst_1
	isub
	iload_1
	iastore
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	iconst_1
	istore_1
Label5:
	iload_1
	iconst_5
	if_icmpgt Label7
	aload_2
	iload_1
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label7:
	aload_2
	invokestatic MPClass/foo([I)V
	iconst_1
	istore_1
Label8:
	iload_1
	iconst_5
	if_icmpgt Label10
	aload_2
	iload_1
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
