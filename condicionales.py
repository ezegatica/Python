a = 2
b = 3.4
oracion = "El resultado es "

resultado = a*b

print(oracion + str(resultado))

if (a == 2 and b == 3.4):
    print("En el primer if")
    c = a + b
    if(c == 5.8 or a == 2):
        print("En el segundo if")

# if (a == 2):
#     pass

while (a <= 5):
    print("El valor de a es: " + str(a))
    a = a + 1
