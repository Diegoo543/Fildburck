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
while True:
    num = int(input('ingrese numero'))
    if (num %2 != 0):
        print('El numero que ingreso es impar')
        break
    else:
        print('El numero que ingreso es par, vuelve a intentar')

if __name__ == '__main__':
    main()
