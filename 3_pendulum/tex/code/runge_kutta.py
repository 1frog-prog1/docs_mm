def solve_odu2(f, t, u):
    a = [u0[0]]
    z = [u0[1]]
    u = u0
    for i in range(len(t) - 1):
        k0 = f(t[i], u)
        k1 = f(t[i] + h/2, u + h/2*k0)
        k2 = f(t[i] + h/2, u + h/2*k1)
        k3 = f(t[i] + h,u + h*k2)
        u = u + h/6 * (k0 + 2*k1 + 2*k2 + k3)

        a.append(u[0])
        z.append(u[1])
        
    return a, z 