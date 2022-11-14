#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dyujr
#
# Created:     15/09/2022
# Copyright:   (c) dyujr 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
num1 = int(input('Ingrese Primer Numero'))
num2 = int(input('Ingrese Segundo Numero'))

print('Ingrese una de las siguientes operaciones: 1. Sumar 2. Restar 3. Multiplicar')
while True:
    operacion = input('Ingrese la operacion a realizar').lower()
    if (operacion == 'sumar'):
        sumar = num1 + num2
        print(f'El Resultado es: {sumar}')
        break
    elif (operacion == 'restar'):
        restar = num1 - num2
        print(f'El Resultado es: {restar}')
        break
    elif (operacion == 'multiplicar'):
        multiplicar = num1 * num2
        print(f'El Resultado es: {multiplicar}')
        break
    else:
        print('La opcion ingresada es incorrecta, intente nuevamente')
if __name__ == '__main__':
    main()
