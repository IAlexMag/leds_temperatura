print("Ingresa tu número de telefono de la siguiente manera:\n \nxxx-xxx-xxxx\n")
phone_number = input("Coloca el número de telefóno: ")

def IsPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True
print(IsPhoneNumber(phone_number))   

# forma corta 
#%%
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search("Mi número es 551-129-8118")

print(f'Número encontrado: {mo.group()}')
