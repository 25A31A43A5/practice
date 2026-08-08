def valid_input(a:int,b:int)->bool:
    try:
        int(a)
        int(b)
        return True
    except:
        return False

def valid_operator(op:str)->bool:
    OPERATORS=["+","-","*","/"]
    return op in OPERATORS

def valid_division(a:int,b:int)->bool:
    return b!=0

