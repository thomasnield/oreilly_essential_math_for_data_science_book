from sympy import *

# plot relu
x = symbols('x')
relu = Max(0, x)
plot(relu)