import math
from coloristic import *

def f(u,t):
    if u<(2*t):
        return (u**(-1))-(t**(-1))
    elif u >(2*t):
        return (u-t)**2
            

def main():
    Yes = 'да'
    printc(user3("Правила\nx должен быть больше 0;\ny по модулю должен быть больше x;\ny и x не должен быть равен 0;\n"))

    while Yes == 'да' or Yes == 'yes':
        x = float(input('Введите X-значение:>'))
        y = float(input('Введите Y-значение:>'))

        if (-1<=x/y<=1):
            if (math.acos(x/y)!=0) and (y!=0) and (x!=0):
                z1 = f(abs(math.log(x)+y), (math.sin(y-x)/math.acos(x/y)))
                z2 = math.cos(math.sqrt(f(math.exp(y),(2*x-1)**3)))
                z3 = math.tan(f(y/x,math.asin(x/y)))

                print('Результат: Z({}, {}'.format(round(x,2), round(y,2)),') = ', round(z1+z2+z3,2),'\nz =', z1+z2+z3, sep='')
            else:
                print("шо твориш")
        else:
                print("шо твориш2")

        Yes = input('Повторить ввод [да|yes]:>')
        
        Yes = 'да'
        Yes = Yes.lower()
        print()


main()
