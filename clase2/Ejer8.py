#-------------------------------------------------------------------------------
# Name:        module2
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
    menor= lista[0]
    for a in lista:
        if a < menor:
            menor = a
    print(f'El numero menor es {menor}!')
if __name__ == '__main__':
    main()
