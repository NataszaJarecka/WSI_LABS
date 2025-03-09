import numpy as np
import sympy as sp

def gradient(f, variables):
    f_expr = f(*variables)
    gradients = [sp.diff(f_expr, var) for var in variables]
    gradient_func = sp.lambdify(variables, gradients, "numpy")

    return gradient_func

def gradient_descent(f, variables, step, start, presicion, iter):
    grad = gradient(f, variables)
    point = np.array(start)
    i = 0
    while i < iter and np.linalg.norm(grad(*point)) > presicion:
        grad_value = np.array(grad(*point))
        next_point = point - step * grad_value
        while f(*next_point) >= f(*point):
            step = step/2
            next_point = point - step * grad_value
        point = next_point
        i += 1
    return point

x1, x2 = sp.symbols('x1 x2')
print(gradient_descent(lambda x1, x2:(x1-2)**4 + (x2 + 3)**4 + 2*((x1 - 2)**2)*((x2 + 3)**2), [x1, x2], 0.1, (1, 0), 0.0001, 1000))
# print(gradient_descent(lambda x: (x -2 )**2, [x], 0.1, [-1], 0.0001, 10000))
