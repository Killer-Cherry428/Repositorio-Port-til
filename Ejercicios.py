#TAREA-------------- EJERCICIOS -------------


#Revision de elementos repetidos en la lista ---------------------------------------

#determinar si la lista tiene elementos que se repiten.
print("\n-------------- DETERMINAR SI HAY ELEMENTOS EN LA LISTA QUE SE REPITEN -----------\n")

def revisionElemetos(lista):
    #se crea un diccionario
    frecuencia={}

    for dato in lista:   #Se recorre la lista elements por elemento 
        if (dato in frecuencia):
            return True #si el valor dato ya se encuentra en frecuencia entonces esta repetido.
        else:
            frecuencia[dato]=1 #si no existe este elemeto entonces los añadimos con un contador =+1
    return False #si no se encuentra ningun elemento repetido en la lista.

listado=[]

#tamaño de la lista
nelemetos=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento in range(nelemetos):
    ele=input(f"Ingresa el elemento de la lista numero {elemento+1}: ") # se puede ingresar cualquier tipo de dato 
    listado.append(ele) #agrega un elemento al final de la lista

if(revisionElemetos(listado)):
    print("\nLa lista contiene elementos repetidos. ")
else:
    print("\nLa lista no posee elemetos repetidos. ")



#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# DESARROLLAR UN PROGRAMA QUE DETERMINE SI UN ELEMENTO ES UN PALINDROMO
#SI EXISTE SE IMPRIME LA CADENA Y SI NO EXISTE ENTONCES SE IMPRIME UN MENSAJE DE NO EXISTE

print("\n-------------- ENCONTRAR PALINDROMO EN LA LISTA -----------\n")

listadoPali=[]

nelemetos1=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento1 in range(nelemetos1):
    ele1=input(f"Ingresa el elemento de la lista numero {elemento1+1}: ")
    listadoPali.append(ele1) #agrega un elemento al final de la lista


def palindromo(listadoPali):

    muchosPalindromos=[]

    for ele1 in listadoPali:
        #debe ser obligatoriamente un string
        eleOriginal=ele1 #Guardamos el elemento original para usarlo en dado caso que sea palindromo
        ele1=str(ele1) #se convierte el valor a string
        ele1=ele1.lower() #se convierte a minuscula
        ele1=ele1.replace(" ","") #los espacios en blanco se eliminan, haciando un reemplazo

        if(ele1 == ele1[::-1]): #se revisa si la cadena es igual que la cadena pero visto a la inversa
           muchosPalindromos.append(eleOriginal) #si el elemento si es un palindromo se guarda en la nueva lista 

    if(len(muchosPalindromos)==0):
        return "No hay palindromos en la lista ingresada. " #en dado caso que la lista sea cero es porque no existio ningun palindromo
    else:
        return f"Los palindromos existentes en la lista son: {muchosPalindromos}"

print(f"La lista original es: {listadoPali}")
print("Los elementos que son palindromos: ",palindromo(listadoPali))


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

# DESARROLLAR UN PROGRAMA QUE DETERMINE SI EN LA LISTA SE ENCUENTRA UNA CADENA DE CARACTERES CON DOS O MAS VOCALES
#CONTAR VOCALES

print("\n-------------- ENCONTRAR VOCALES EN LA LISTA-----------\n")

listadoVocales=[]

nelemetos2=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento2 in range(nelemetos2):
    ele2=input(f"Ingresa el elemento de la lista numero {elemento2+1}: ")
    listadoVocales.append(ele2) #agrega un elemento al final de la lista

def contador(cadena):
    vocales="aeiou"
    contadorVocales=0
    for letra in cadena: #se recorre cada caracter de la cadena ingresada 
        if (letra in vocales):
            contadorVocales=contadorVocales+1 #si ese caracter es igual a las vocales se itera 
    return contadorVocales

def contarVocales(listadoVocales):
    muchosVocales=[]
    for ele2 in listadoVocales:
        ele2=str(ele2) #se convierte el valor a string
        ele2=ele2.lower() #se convierte a minuscula
        ele2=ele2.replace(" ","") #los espacios en blanco se eliminan,
        if (contador(ele2)>=2):
            muchosVocales.append(ele2) 
        
    return muchosVocales
        

print("Lista original: ",listadoVocales)
print(f"Los elementos contenidos en la lista con mas de dos vocales son: {contarVocales(listadoVocales)}")


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#Lista es palindrome 

print("\n-------------- DETERMINAR SI LA LISTA ES PALINDROME -----------\n")

lista=[]

nelemetos2=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento3 in range(nelemetos2):
    ele3=input(f"Ingresa el elemento de la lista numero {elemento3+1}: ")
    lista.append(ele3) #agrega un elemento al final de la lista

def ListPalindrome(lista):
    #inversion de lista
    listaInvertida=lista[::-1]

    #verificar si lista es igual a la inversion
    if (lista==listaInvertida):
        return True
    return False

if(ListPalindrome(lista)):
    print(f"La lista {lista} es un palindromo. ")
else:
    print(f"La lista {lista} no es un palindromo")


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


#----------------- Propuestas de nuevos codigos ----------------------

#///////////////////////////////////////////////////////////////////////////

print("\n--------------    ENCONTRAR MAS DE 6 CONSONANTES -----------\n")

listadoConsonantes=[]

nelemetos4=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento4 in range(nelemetos4):
    ele4=input(f"Ingresa el elemento de la lista numero {elemento4+1}: ")
    listadoConsonantes.append(ele4) #agrega un elemento al final de la lista

def contador(cadena):
    consonantes="zxcvbnmñlkjhgfdsqwrtyp"
    contadorConsonantess=0
    for letra in cadena: #se recorre cada caracter de la cadena ingresada 
        if (letra in consonantes):
            contadorConsonantess=contadorConsonantess+1 #si ese caracter es igual a las vocales se itera 
    return contadorConsonantess

def contarVocales(listadoConsonantes):
    muchosConsonantess=[]
    for ele4 in listadoConsonantes:
        ele4=str(ele4) #se convierte el valor a string
        ele4=ele4.lower() #se convierte a minuscula
        ele4=ele4.replace(" ","") #los espacios en blanco se eliminan,
        if (contador(ele4)>=6):
            muchosConsonantess.append(ele4) 
        
    return muchosConsonantess
        

print("Lista original: ",listadoConsonantes)
print(f"Los elementos contenidos en la lista con mas de 6 consonantes son: {contarVocales(listadoConsonantes)}")

#///////////////////////////////////////////////////////////////////////////

#determinar la cadena mas larga y la mas corta de la lista 
print("\n-------------- DETERMINAR CUAL CADENA ES LA MAS CORTA DE LA LISTA -----------\n")

listadoX=[]

nelemetos5=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento5 in range(nelemetos5):
    ele5=input(f"Ingresa el elemento de la lista numero {elemento5+1}: ")
    listadoX.append(ele5) #agrega un elemento al final de la lista


def cadenaLyC(listaaa):
    if not listaaa:
        return None
    
    #Inicializar con la primera cadena para tener claro el punto de partida 
    masCorta=listaaa[0]

    for datoo in listaaa:

        if(len(datoo)<len(masCorta)):
            masCorta=datoo
    return masCorta

cadCorta=cadenaLyC(listadoX)

if( cadCorta):

    print("La cadena mas corta de la lista ingresada es: ",cadCorta)





print("\n-------------- DETERMINAR CUAL CADENA ES LA MAS LARGA DENTRO DE LA LISTA -----------\n")

listadoX=[]

nelemetos5=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento5 in range(nelemetos5):
    ele5=input(f"Ingresa el elemento de la lista numero {elemento5+1}: ")
    listadoX.append(ele5) #agrega un elemento al final de la lista


def cadenaLyC(listaaa):
    if not listaaa:
        return None
    
    #Inicializar con la primera cadena para tener claro el punto de partida 
    masLarga=listaaa[0]

    for datoo in listaaa:
        if(len(datoo)>len(masLarga)):
            masLarga=datoo

    return masLarga

cadLarga=cadenaLyC(listadoX)

if(cadLarga):
    print("La cadena mas larga de la lista ingresada es: ",cadLarga)
 



#usar set para eliminar elementos repetidos de la lista
print("\n-------------- ELIMINAR ELEMENTOS REPETIDOS  -----------\n")

listay=[]
nelemetos6=int(input("Ingrese el tamaño de la lista que desea crear: "))

#Bucle para agregar los elementos en la lista
for elemento6 in range(nelemetos6):
    ele6=input(f"Ingresa el elemento de la lista numero {elemento6+1}: ")
    listay.append(ele6) #agrega un elemento al final de la lista


def repetidos(listay):
    visto=set()
    sinRepetido=[]

    for rep in listay:
        if(rep not in visto):
            sinRepetido.append(rep) #agrega sin importar que se repita
            visto.add(rep) #se agrega, si ya existe entonces no se agrega
    return sinRepetido

lisSinRep=repetidos(listay)

print("\nLista original", listay)
print("Lista sin repeticiones: ",lisSinRep)


