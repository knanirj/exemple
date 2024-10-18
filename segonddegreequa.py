def eq2grau():
    #Coeficientes
    a = input("Entre com o coef a: ")
    a = float(a)
    b = input("Entre com o coef b: ")
    b = float(b)
    c = float(input("Entre com o coef c: "))
    Delta = b**2-4*a*c
    x1 = (-b-Delta**0.5)/(2*a)
    x2 = (-b+Delta**0.5)/(2*a)
    print("Coeficientes: ", a, b, c)
    print("Delta = ", Delta)
    print("Soluções: x1 = ", x1, "x2 = ", x2)
eq2grau()
