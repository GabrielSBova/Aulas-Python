digito = input('Escreva algo: ')
print('O tipo primitivo desse valor é {} '.format(type(digito)))
print('Só tem espaços? {} '.format(digito.isspace()))
print('É um número? {} '.format(digito.isnumeric()))
print('Está em letras maiúsculas? {} '.format(digito.isupper()))
print('Está em letras minúsculas? {} '.format(digito.islower()))
print('Está capitalizada? {}'.format(digito.istitle()))
print('É alphabético? {}'.format(digito.isalpha()))
print('É alphanumérico? {}'.format(digito.isalnum()))


