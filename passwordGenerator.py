import random

print('Welcome to the PyPassword Generator!')
u_letters=int(input('How many letters you like in your password?: \n'))
u_numbers=int(input('How many numbers would you like?: \n'))
u_symbols=int(input('How many symbols would you like?: \n'))

#cases
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#Imprimir x letras random.
for i in range(0,u_letters):
    r_letters=random.choices(letters,k=u_letters)
    
final_letters=("".join(r_letters))

#Imprimir x numeros(Son Strings) random.
for i in range(0,u_numbers):
    r_number=random.choices(numbers,k=u_numbers)

final_numbers=("".join(r_number))

#Imprimir x simbolos random.
for i in range(0,u_symbols):
    r_symbol=random.choices(symbols,k=u_symbols)

final_symbol=("".join(r_symbol))

final_password1= final_letters+final_numbers+final_symbol
print('Tu clave es: \n' + final_password1)

#Randomizar toda la clave, para perder el orden de los input
new_list= list(final_password1)
random.shuffle(new_list)

final_password2=("".join(new_list))
print('Tu clave super Segura es: \n' + final_password2)





