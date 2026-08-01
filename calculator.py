def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a=0.0,b=0.0):
    return a/b
def modulo(a,b):
    return a%b
def power(a,b):
    return a**b

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "pow": power
}

def Input_integer():
    a,b=map(float,input("enter two integers: ").split())
    return a,b
def Input_choice():
    c=input("+ for addition\n-for subtraction\n* for multiplication\n/ for division\n% for modulus\npow for power\nExit to exit\nHis to show history\nchoice: ").lower()
    return c
def show_history():
    with open("history.txt") as p:
       data= p.read()
       print(f"\n{data}")
def main():
    print("========Calculator========")
    with open("history.txt","a") as f:
        while True:
            choice=Input_choice()
            if(choice=="exit"):
                print("Exiting....")
                break
            if(choice=="his"):
                show_history()
                continue
            a,b=Input_integer()

            if choice in operations:
                try:
                    print(f"result: {operations[choice](a,b)}")
                    f.write(f"{a} {choice} {b} = {operations[choice](a,b)}\n")
                    f.flush()
                except ZeroDivisionError as e:
                    print(e)
            else:
                print("invalid operator")


main()