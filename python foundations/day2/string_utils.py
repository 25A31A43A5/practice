def reverse_string(string:str)->str:
    result=""
    lenght=len(string)
    for i in range(lenght):
        result+=string[lenght-i-1]
    return result

def count_vowels(text:str)->int:
    n=0
    text=text.lower()
    VOWELS="aeiou"
    for a in text:
        if a in VOWELS:
            n+=1
    return n

def count_consonants(text:str)->int:
    n=0
    text=text.lower()
    VOWELS="aeiou"
    for a in text:
         if a not in VOWELS and a.isalpha():
                n+=1
    return n

def is_palindrome(text:str)->bool:
    return True if reverse_string(text)==text else False

def word_count(text:str)->int:
    return len(text.split())
