from math import *

def f(u,t):
	if u<(2*t):
            return (u**(-1))-(t**(-1))
        elif (u >2*t):
            return (u-t)**2
            

def main():
	Yes = 'да'
	while Yes == 'да' or Yes == 'yes':
		
		x = float(input('Введите X-значение:>'))
		y = float(input('Введите Y-значение:>')) 
		
		z1 = f(abs(log(x)+y), (sin(y-x)/arccos(x/y)))
		z2 = cos(sqrt(f(exp(y),(2*x-1)**3)))
		z3 = tan(f(y/x,arcsin(x/y)))
		
		print('Результат: Z(', x,y,') = ', round(z1+z2+z3,2),'/n z =', z1+z2+z3)

		Yes = input('Повторить ввод [да|yes]:>')
		Yes = Yes.lower()
		print()


main()
