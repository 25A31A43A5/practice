from . import calculator
from . import validator
from . import logger

def main():
    log=logger.get_logger()

    print("------------------------calculator------------------------")

    a,b=input("enter the values of a and b: ").split()
    if(not validator.valid_input(a,b)):
        log.warning("invalid input")
        return
    a,b=int(a),int(b)
    op=input("Enter the operator: ")
    if(not validator.valid_operator(op)):
        log.warning("Invalid Input")
        return

    if(op=="/" and not validator.valid_division(a,b)):
        log.warning("Zero Division Error")
        return

    result=calculator.result(op,a,b)
    print(f"The  result is {result}")
    
if __name__=="__main__":
    main()