#-------------------------------------------------------------------------------
# Name:        module2
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
lista = ['element1', 'element2', 'element3', 'element4', 'element5']
contar = 0

for i in lista:
    contar = contar + 1
    print(contar)

print(f'La cantidad total es: {contar}')
if __name__ == '__main__':
    main()
