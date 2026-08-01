class student:
    def __init__(self,a,b,c)->None:
        self.name:str=a
        self.age:int=b
        self.percentage:float=c
    def check_age(self)->bool:
        return True if self.age>=18 else False
    def grade(self)->str:
        if self.percentage>=90:
            return "A"
        elif self.percentage>=75:
            return "B"
        elif self.percentage>=65:
            return "C"
        elif self.percentage>=50:
            return "D"
        elif self.percentage >=35:
            return "E"
        else:
            return "F"

def main():
    pass
