# RAFAEL MIRANDA JIMENEZ
# 3202
# INGENIERIA EN SISTEMAS COMPUTACIONALES
# ALGEBRA LINEAL

import cmath
import math
import matplotlib.pyplot as plt

def menu():
    print("----------CALCULADORA DE NUMEROS COMPLEJOS----------")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. POTENCIAS A LA N")
    print("6. POTENCIAS DE I")
    print("7. RAICES DE NUMEROS COMPLEJOS")

def switch(case, q, w, e, r):
    sw={
    }
    return sw.get(case,default())

def default():
    return "La opcion %s no existe en el menu"% case

repetir=True
while repetir:
    print("**************Calculadora de Numeros Complejos**************")
    print("Numeros de la forma a+bi")
    print("Con a como la parte real y b la parte imaginaria")
    menu()
    case=int(input("Selecciona una operacion "))
    if case == 1:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        n=a+c
        m=b+d
        z= complex(n, m)
        print ("El resultado es", z)
        x = [n]
        y = [m]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 2:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        n=a-c
        m=b-d
        z= complex(n,m)
        print ("El resultado es", z)
        x = [n]
        y = [m]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 3:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Nunero ingresado: ",(z))
        n = (a*c) - (b*d)
        m = (b*c) + (a*d)
        z = complex (n,m)
        print("El resultado es", z)
        x = [n]
        y = [m]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 4:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        modulo2 = c*c + d*d
        n = (a*c) + (b*d)
        real = n / modulo2
        m = (b*c) - (a*d)
        imag = m / modulo2
        z = complex(real,imag)
        print("El resultado es", z)
        x = [real]
        y = [imag]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 5:
        a=int(input("Digite la parte real del numero complejo "))
        b=int(input("Digite la parte imaginaria del numero complejo "))
        c= int(input("Ingresa la potencia "))
        z = complex(a,b)
        print("Numero ingresado: ", z, "^", c )
        s = math.sqrt(a** 2 + b** 2)
        angulo = math.atan(b/a)
        h = math.degrees(angulo)
        rPotencia = s ** c
        anguloMultiplicado = h * c
        rad = anguloMultiplicado * math.pi/180
        rads = anguloMultiplicado * math.pi/180
        cos = math.cos(rad)
        sen = math.sin(rads)
        rReal = cos * rPotencia
        rImag = sen * rPotencia
        z = complex(rReal,rImag)
        print("El resultado es", z)
        x = [rReal]
        y = [rImag]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 6:
        a =int(input("Inresa la potencia que quieres elevar a i "))

        print("Numero ingresado",  "i",  "^", str(a,))

        b = a%4

        if b == 0:
            print("El resultado es 1")
        elif b == 1:
            print("El resultado es i")
        elif b == 2:
            print("El resultado es -1")
        elif b == 3:
            print("El resultado es -i")
        x = [b]
        y = 0
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.show()
        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
    elif case == 7:
        a=int(input("Digite la parte real del numero complejo "))
        b=int(input("Digite la parte imaginaria del numero complejo "))
        c= int(input("Ingresa la raiz "))
        s = math.sqrt(a** 2 + b** 2)
        angulo = (b/a)
        x = math.atan(angulo)
        h = math.degrees(x)
        raiz= s**(1/float(c))
        contador = 0
        while contador < c:
                rRaiz = contador * 360
                f= rRaiz + h
                z = f/c
                rad = z * math.pi/180
                rads = z * math.pi / 180
                cos = math.cos(rad)
                sen = math.sin(rads)
                rReal = cos * raiz
                rImag = sen * raiz
                z = complex(rReal,rImag)
                print("El resultado es: ", z)
                contador = contador + 1
                x = [rReal]
                y = [rImag]
                plt.scatter(x,y)
                plt.ylabel('Imaginario')
                plt.xlabel('Real')
                plt.show()

        rep=input("¿Desea realizar otra operacion? [S/N]")
        if rep == "s" or rep == "S":
                repetir = True
        else:
                repetir=False
