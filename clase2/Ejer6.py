#-------------------------------------------------------------------------------
# Name:        module4
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
    numeros = [30,20,15,25,10]
    total = 0
    cant = 0
    for n in numeros:
        total = total + n
    for m in numeros:
        cant = cant + 1
    promedio = total / cant

    print(f"La suma de la lista es: {total}")
    print(f"La cantidad de elementos de la lista es: {cant}")
    print(f'El promedio de la lista es: {promedio}!')
if __name__ == '__main__':
    main()
