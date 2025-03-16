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
    all_points = [start]
    i = 0
    while i < iter and np.linalg.norm(grad(*point)) > presicion:
        grad_value = np.array(grad(*point))
        next_point = point - step * grad_value
        point = next_point
        i += 1
        all_points.append(point)
    return point, i, all_points