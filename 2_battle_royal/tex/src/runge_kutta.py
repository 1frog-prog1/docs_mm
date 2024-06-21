def f(t, u_orig):
    u = u_orig.copy()
    return np.array([
        (a - c * u[1]) * u[0],
        (-b + d * u[0]) * u[1]
    ])

def runge_kutta(h, u0, t):
    x = [u0[0]]
    y = [u0[1]]
    u = u0
    for i in range(len(t) - 1):
        k0 = f(t[i], u)
        k1 = f(t[i] + h/2, u + h/2*k0)
        k2 = f(t[i] + h/2, u + h/2*k1)
        k3 = f(t[i] + h,u + h*k2)
        u = u + h/6 * (k0 + 2*k1 + 2*k2 + k3)

        x.append(u[0])
        y.append(u[1])
        
    return x, y