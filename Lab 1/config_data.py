import numpy as np
import sympy as sp

# constance used in plots
x = sp.symbols('x')
F = lambda x: 10*x**4 + 3*x**3 - 30*x**2 + 10*x
X = np.linspace(-3, 3, 400)
Y_F = F(X)

x1, x2 = sp.symbols('x1 x2')
G = lambda x1, x2: (x1-2)**4 + (x2+3)**4 + 2 * ((x1-2)**2) * ((x2+3)**2)
X1, X2 = np.meshgrid(np.linspace(-50, 50, 50), np.linspace(-50, 50, 50))
Y_G = G(X1, X2)

# constance used in experiments

F_VARIABLES = [x]
F_PRESICION = 0.000001
F_ITER = 10000


G_VARIABLES = [x1, x2]
G_PRECISION = 0.000001
G_ITER = 10000

