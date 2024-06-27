def right(t, x):
     return np.array([
        x[2], 
        x[3],
        2 * w * x[3],
        -2 * w * x[2]
     ])

def solve_odu2(f, y0, a, b, h):
    num = int(np.ceil((b - a) / h))
    t = np.linspace(a, b, num=num, endpoint=False)
    x = [y0] * num

    for i in range(num - 1):
        k0 = f(t[i], x[i])
        k1 = f(t[i] + h/2, x[i] + h/2*k0)
        k2 = f(t[i] + h/2, x[i] + h/2*k1)
        k3 = f(t[i] + h,x[i] + h*k2)
        x[i + 1] = x[i] + h/6 * (k0 + 2*k1 + 2*k2 + k3)

    return t, np.array(x)        