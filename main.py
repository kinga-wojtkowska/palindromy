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
        return True
    else:
        return False

print(palindrome(x))