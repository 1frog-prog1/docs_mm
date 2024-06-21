def findFunction(x, y0, h):
    y = [y0]
    for i in range(len(x) - 1):
        k0 = f(x[i], y[i])
        k1 = f(x[i] + h/2, y[i] + h/2*k0)
        k2 = f(x[i] + h/2, y[i] + h/2*k1)
        k3 = f(x[i] + h, y[i] + h*k2)
        y.append(y[i] + h/6 * (k0 + 2*k1 + 2*k2 + k3))
    return y