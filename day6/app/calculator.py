def add(a:int, b:int)->int:
    return a+b

def subtract(a:int, b:int)->int:
    return a-b

def multiply(a:int, b:int)->int:
    return a*b

def divide(a:int ,b:int)->float:
    return a/b

def result(op:str,a:int,b:int)->int|float:
    OPERATOR={"+":add,"-":subtract,"*":multiply,"/":divide}
    return OPERATOR[op](a,b)
