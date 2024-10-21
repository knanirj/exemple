def eq2grau(a, b, c):
    Delta = b**2-4*a*c
    x1 = (-b-Delta**0.5)/(2*a)
    x2 = (-b+Delta**0.5)/(2*a)
    return x1, x2, Delta
r1, r2, raja = eq2grau(1, 7, 10)
print("delta = ", raja, ", x1 = ", r1, ",x2 = ", r2)
