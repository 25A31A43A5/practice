def add(a:int, b:int):
    return a+b
def subtract(a:int, b:int)->int:
    return a-b
def multiply(a:int, b:int):
    return a*b
def divide(a:int ,b:int):
    return a/b

def choice(operator:chr):
    match operator:
        case '+':
            return add
        case '-':
            return subtract
        case '/':
            try:
                return divide
            except ZeroDivisionError as e:
                print("division by zero is not possible")
                exit
        case '*':
            return multiply
def main():
    print("------------------------calculator------------------------")
    a,b=map(int, input("Enter the values of a and b: ").split())
    op=input("enter the operator")
    print(choice(op)(a,b))

if __name__=="__main__":
    main()