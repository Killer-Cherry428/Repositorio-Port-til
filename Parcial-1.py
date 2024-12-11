#Miguel Andres Ordoñez Hernandez

#$------------------------------EJERCICIO 1-------------------------------------
print("\n------------------------------EJERCICIO 1-------------------------------------\n")
Numero=int(input("Ingrese el numero del que desa conocer el cuadrado: ")) #Ingreso por consola del valor deseado
def cuadrados(nu):  #definimos una funcion para optimizar, se le debe ingresar un parametro
    if (nu>=0):         #Se confirma que el numero no es negativo
        NumeroCua=nu**2
        print("El cuadrado del numero ",nu,"es igual a:")
    else:
        print("El numero ingresado es negativo")
    return NumeroCua #Como a la funcion se le ingresa un parametro, esta debe retornar un valor, en este caso el valor del cuadrado

print(cuadrados(Numero)) #Se imprime el valor del cuadrado, llamando la funcion e ingresando como parametro el numero ingresado por consola 

#$-------------------------------EJERCIO 2------------------------------------
print("\n------------------------------EJERCICIO 2-------------------------------------\n")

Entero=int(input("Ingres el valor numerico: ")) #Ingreso por consola del valor deseado
Ent=0
while (Entero!=1): #El cilo se ejecutara indefinidamente hasta que el valor del entero sea 1, en ese momento el ciclo se terminará
    if(Entero%2==0): #Se implementa el modulo, con el que se identifica el residuo de la division, si el valor es cero el numero ingresado es par
        Entero=Entero/2
        print("El numero es par, por ende El valor de la division es: ",Entero) #Impresion en pantalla de la operacion
    else:            #Si no es un numero par, se ejecuta la siguente condicion
        Entero=3*Entero+1 
        print("El numero es impar, por lo tanto el valor de la ecuacion es: ",Entero) #Impresion en pantalla de la operacion

#$--------------------------------EJERCICIO 3-----------------------------------

#Pais A =25 millones crecimiento 2%
#Pais B=18.9 millones crecimiento del 3%
print("\n------------------------------EJERCICIO 3-------------------------------------\n")
PaisA=25000000 #Inicializacion de la variables
PaisB=18900000  
contadorAnual=0

while True: #implementamos un ciclo while infinito, que se ejecutará hasta que la condicion IF, rompa el ciclo por medio del Break
    CreA=PaisA*0.02 #Sacar porcentaje
    CreB=PaisB*0.03
    CreciA=CreA+PaisA #sumar el porcentaje al valor original
    CreciB=CreB+PaisB
    if(PaisB>PaisA):#Revisar si el valor de B es mayor a A
        paB=int(PaisB) #conversion del valor flotante a entero
        paA=int(PaisA)
        print("La poblacion del pais B es de ",paB," y la de el pais A es ",paA)
        print("Para el año ",2022+contadorAnual," el pais B superara la poblacion del pais A, en total pasaron",contadorAnual," años \n")
        break #Se encarga de romper el ciclo para que se deje de ejecutar

    contadorAnual=contadorAnual+1 #Contado de años que aumenta con cada iteracion del programa
    PaisA=CreciA #asignacion del nuevo valor del poblacion del pais 
    PaisB=CreciB
    #Test
