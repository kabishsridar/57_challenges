from sympy import diff, integrate, symbols, sin, exp, sqrt, Integral, factor, expand, latex, init_printing, solve, limit, dsolve, Eq
init_printing() # automatically enables better printer available
x, y, z = symbols("x y z")
d = diff(sin(x) * exp(x), x)
print(d)
i = integrate(sin(x))
print(i)
print(sqrt(8))
expression = x**2 + 2*x + 1
fac = factor(expression)
print(fac)
print(expression - x**2)
print(f"The expanded form is {expand(expression)}")
print(solve(x**2 -2, x))
print(limit(sin(x)/x,x,0))
print(latex(Integral(sqrt(1/x), x)))