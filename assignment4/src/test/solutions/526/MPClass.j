.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "bat dau with"
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 1 is a I from Label2 to Label3
.var 2 is b I from Label2 to Label3
Label2:
	iconst_1
	istore_1
	iconst_2
	istore_2
	iload_1
	iload_2
	iadd
	invokestatic io/putInt(I)V
Label3:
	ldc "ket thuc with"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
