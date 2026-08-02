import math_utils as mu
import day2.string_utils as su

def main():
    print("-----------------------day 2-----------------------")
    print("1.square of a number\n2.cube of a number\n3.factorial of a number\n4.To check prime\n5.greatest common divisor for two numbers\n6.least common multiple for two numbers")
    print("7.reverse string\n8.count of vowels\n9.count of consonants\n10.To check palindrome\n11.count of words")

    try:
        a=int(input("Enter your input"))
    except ValueError:
        print("Invalid Input")
        return

    match a:
        case 1:
            try:
                n=int(input("enter a number to square: "))
            except ValueError:
                print("Invalid Input")
                return
            print(mu.square(n))
        case 2:
            try:
                n=int(input("enter a number to cube: "))
            except ValueError:
                print("Invalid Input")
                return
            print(mu.cube(n))
        case 3:
            try:
                 n=int(input("enter a number: "))
            except ValueError:
                print("Invalid Input")
                return
            try:
                print(mu.factorial(n))
            except ValueError as e:
                print(e)
                return
        case 4:
            try:
                n=int(input("Enter a number to check for prime: "))
            except ValueError:
                print("Invalid Input")
                return
            print(mu.is_prime(n))
        case 5:
            try:
                x,y=map(int,input("enter two numbers x and y: ").split())
            except ValueError:
                print("Invalid Input")
                return
            print(mu.gcd(x,y))
        case 6:
            try:
               x,y=map(int,input("enter two numbers x and y: ").split())
            except ValueError:
                print("Invalid Input")
                return
            print(mu.lcm(x,y))
        case 7:
            try:
                string=input("enter a string to reverse")
            except ValueError:
                print("Invalid Input")
                return
            print(su.reverse_string(string))
        case 8:
            try:
                string=input("enter a string to count number of vowels")
            except ValueError:
                print("Invalid Input")
                return
            print(f"number of vowels are {su.count_vowels(string)}")
        case 9:
            try:
                string=input("enter a string to reverse")
            except ValueError:
                print("Invalid Input")
                return
            print(f"number of consonants are:{su.count_consonants(string)}")
        case 10:
            try:
                string=input("Enter a string to check palindrome condition")
            except ValueError as e:
                print(f"Invalid Input: {e}")
                return
            print(su.is_palindrome(string))
        case 11:
            try:
                string=input("Enter a string to count the number of words: ")
            except ValueError as e:
                print(f"Invalid Input: {e}")
                return
            print(su.word_count(string))
        case _:
            print("Invalid input: enter a value between 1-11")
            return

if __name__=="__main__":
    main()