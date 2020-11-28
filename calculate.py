from colorama import Fore,Back,Style
x=int(input('enter a number:: '))
y=int(input('enter the next number:: '))
operator=input('enter an operator(+ ,- ,* ,/):: ')
a=x+y
b=x-y
c=x*y
d=x/y
if operator=="+":
	print(a)
elif operator=="-":
	print(b)
elif operator=="*":
	print(c)
elif operator=="/":
	print(d)
else:
	print(Fore.RED+"you must enter an operator")
	
