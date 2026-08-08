def add(a:int, b:int)->int:
    return a+b

def subtract(a:int, b:int)->int:
    return a-b

def multiply(a:int, b:int)->int:
    return a*b

def divide(a:int ,b:int)->float:
    return a/b

def main():
    OPERATOR={"+":add,"-":subtract,"*":multiply,"/":divide}
    print("------------------------calculator------------------------")
    try:
        a,b=map(int, input("Enter the values of a and b: ").split())
        op=input("enter the operator: ")
    except ValueError:
        print("Invalid Input!!")
        return
    if op in OPERATOR:
        try:
            print(OPERATOR[op](a,b))
        except ZeroDivisionError:
            print("division by zero is not possible!")
            return
    else:
        print("Invalid input")
if __name__=="__main__":
    main()