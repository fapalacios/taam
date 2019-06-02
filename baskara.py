# esse programa encontra as raizes de uma equação de 2o. grau da forma a*x**2 + b*x + c = 0
# dados a, b e c

astr = input('a =')
bstr = input('b =')
cstr = input('c =')

a = float(astr)
b = float(bstr)
c = float(cstr)

delta = b**2 - 4*a*c

if delta > 0:
	x1 = (-b + delta**0.5)/(2*a)
	x2 = (-b - delta**0.5)/(2*a)
	print('x1 = ', x1,'. x2 = ', x2, '.')
elif delta == 0:
	x = -b/(2*a)
	print('x = ', x)
else:
	rx = -b/(2*a)
	ix = (-delta)**0.5/(2*a)
	print('x1 = ', rx, ' + i', ix, '. x2 = ', rx, '- i', ix,'.')
