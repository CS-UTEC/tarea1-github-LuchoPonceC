palindromo = input()
if(palindromo == ''.join(reversed(palindromo))):
    print("Es palindromo")
    exit()
print("No es palindromo")
