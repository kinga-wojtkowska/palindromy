#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem.
# Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.

#Podpowiedź
#Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

x = input("Czy to palindrom? Podaj tekst: ")
def palindrome(x):
    for  i in str(x):
        y = [i for i in x]
        for j in y:
            if j == ' ':
                y.remove(j)
        z = [i for i in reversed(x)]
        for k in z:
            if k == ' ':
                z.remove(k)
    print(y)
    print(z)
    if y == z:
        print("Podane przez Ciebie wyrażenie to palindrom")
    else:
        print("Podane przez Ciebie wyrażenie nie jest palindromem")

palindrome(x)        