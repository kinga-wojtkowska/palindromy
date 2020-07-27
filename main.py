#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem.
# Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.

#Podpowiedź
#Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

def palindrome(x)
    x = input("Czy to palindrom? Podaj tekst: ")
    for  i in x:
        y = [i for i in x]
        z = [i for i in reversed(x)]   
    if y == z:
        print("Podane przez Ciebie wyrażenie to palindrom")
    else:
        print("Podane przez Ciebie wyrażenie nie jest palindromem")