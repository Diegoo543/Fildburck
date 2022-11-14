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

    user = input('Ingrese un mail:')

    if '@' == user:
        print(f'El mail es valido: {user}')
        break
    else:
        print('mail no valido, intentelo nuevamente')
if __name__ == '__main__':
    main()
