'#Programa para saber si una matriz de 3x3 tiene inversa'
def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
#Recepcion de numeros
Ma11=int(input("Ingrese Ma11: "))
Ma12=int(input("Ingrese Ma12: "))
Ma13=int(input("Ingrese Ma13: "))
Ma21=int(input("Ingrese Ma21: "))
Ma22=int(input("Ingrese Ma22: "))
Ma23=int(input("Ingrese Ma23: "))
Ma31=int(input("Ingrese Ma31: "))
Ma32=int(input("Ingrese Ma32: "))
Ma33=int(input("Ingrese Ma33: "))
#Compilacion de matriz
Ma=([[Ma11,Ma12,Ma13],
[Ma21,Ma22,Ma23],
[Ma31,Ma32,Ma33]])
print("Matriz:")
#Impresion de 
for i in Ma: print(i)
M1,M2,M3=Ma[0]
M22M32M23M33=[x[1:] for x in Ma[1:]]
M12M32M13M33=[x[::2] for x in Ma[1:]]
M12M22M13M23=[x[0:2] for x in Ma[1:]]
det = (
    Ma11 * det2x2(M22M32M23M33)
    - Ma21 * det2x2(M12M32M13M33)
    + Ma31 * det2x2(M12M22M13M23)
)
if det==0:
    print("El determinante es 0 y por esa razon no hay inverso.")
else:
    print("Tiene inverso.")

