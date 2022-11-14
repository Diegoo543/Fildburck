#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dyujr
#
# Created:     15/10/2022
# Copyright:   (c) dyujr 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
    lista= [4,78,45,150,33]
    mayor= lista[0]
    for a in lista:
        if a > mayor:
            mayor = a
    print(f'El numero mayor es {mayor}!')
if __name__ == '__main__':
    main()
