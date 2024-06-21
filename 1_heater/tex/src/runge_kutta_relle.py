def findFunctionWithRelle(x, y0, h, down_bound, up_bound):
    y = [y0]
    a = 1
    for i in range(len(x) - 1):
        if y[i] > up_bound + K_CONST:
            a = 0
        elif y[i] < down_bound + K_CONST and a == 0:
            a = 1
        k0 = f(x[i], y[i], a)
        k1 = f(x[i] + h/2, y[i] + h/2*k0, a)
        k2 = f(x[i] + h/2, y[i] + h/2*k1, a)
        k3 = f(x[i] + h, y[i] + h*k2, a)
        y.append(y[i] + h/6 * (k0 + 2*k1 + 2*k2 + k3))
    return y