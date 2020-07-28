x = input("Czy to palindrom? Podaj tekst: ")
def palindrome(x):
    x_lower = str(x.lower())
    x_clear = ''.join( c for c in x_lower if  c not in ';:!*,.? ' )  
        
    print(x_clear)
    for i in x_clear:
        y = [i for i in x_clear]
        z = [i for i in reversed(x_clear)]
    print(y)
    print(z)
    
    if y == z:
        return True
    else:
        return False

print(palindrome(x))