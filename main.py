x = input("Czy to palindrom? Podaj tekst: ")
def palindrome(x):
    x_clear = [char for char in x.lower() if char.isalnum() == True]
    x_reversed = x_clear[::-1]
   
    if x_clear == x_reversed:
        return True
    else:
        return False

print(palindrome(x))