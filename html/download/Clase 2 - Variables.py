#Nota : En python la es importante que la sintaxis este correcta
#Nota : Esto esa siendo mostrado como comentario usando el #, por lo que no afecta al codigo a menos que se elimine el # de cada linea
#Nota : Para compilar el programa debemos dar click en el triangulo de lado, en la parte posterior derecha de la pantalla
#Clase numero 2 

#Uso de las variables con datos
#Aprenderemos a utlizar los diferentes datos en forma de variable mediante ejemplos previamentes demostrativos e indicativos
#Tipos de datos que vamos a utilizar
#1.-Int(Entero)
#2.-Float(Punto Flotante)
#3.-String(Texto)
#4.-Char(Caracter)
#5.-Boolean(Booleano)

#               Fase numero 1 : Uso del dato tipo int
#Antes demos una repaso sobre la anterior clase
#Para crear un dato tipo int, crearemos una variable tipo global, es decir la definiremos al comienzo del codigo
numero = 12
#Esta es la manera en la que declaramos una variable con un dato ya colocado, aunque tambien le podemos asignar un dato usandolo de esta manera 
#dato = None
#Pedir_dato_int = int(input("Texto que deseamos que se muestre"))
#Usamos input para indicarle al programa que cuando llegue a esa accion nosotros somo los que vamos a ingresar un dato, es importante seguir 
#La sintaxis, la cual es declarar int antes del input, y cerrando entre parantesis como se puede ver
#Para poder ver el contenido del dato en python se lo realiza de la siguiente manera print("Nombre del dato"), cabe aclarar que el nombre que escojamos del dato puede 
#ser cualquiera mientras no sea una palabra clave del lenguaje de programacion.

#           Practica 1            #
#Muestra el dato de la variable "numero"

#Crea una variable con el nombre Tipo_entero, usa el input y muestralo en consola 



####Ejemplo de codigo####
#numero_int = int(input("Ingrese un numero : "))
#print(numero_int)

#               Fase numero 2 : Uso del dato tipo float

#Para poder crear una dato tipo float hay que entender que es este tipo de dato son datos numericos los cuales llevan decimales
#Por ejemplo 11/2, el resultado de esta divison es 10.5, estos tipos de datos que llevan decimales son los tipos float
#Cabe aclarar que se debe usar el punto decimal (2.5), en vez de un coma (2,5)
Tipo_float = 2.5
#Tan solo usamos print para poder mostrar en pantalla el dato que contiene esa variable tipo float
#De igual manera podemos asignarle un dato usando el print

#           Practica 2           #

#Muestra el dato dato de la variable "Tipo_float"

#Crea una variable con el nombre Tipo_float, usa el input y muestra en consola


####Ejemplo de codigo####
#numero_float = float(input("Ingrese un numero : "))
#print(numero_float)

#               Fase numero 3 : Uso del dato tipo string y tipo char

#Para crear y usar un dato tipo string o char se lo realiza de la siguiente manera
#Declaramos el nombre de la variable y dentro del conentido debemos usar doble comillas "Dentro del texto" o comillas simples ´ ´ 
#texto = "hola mundo"
#texto2 = 'hola mundo'
#Y simplemente lo imprimimos en la pantalla 
#En este ejemplo hemos usado un dato tipo string, pero tambien podemos usar un dato tipo char en el mismo dato de la variable
#La diferencia entre un dato tipo string y tipo char son su funcionalidad
#String : Muestra una cadena de texto
#Char : Muestra un caracter
#Pero veamos en un ejemplo
Tipo_string = "Hola mundo"
# La variable Tipo_string contiene el texto "Hola mundo", pero si queremos obtener tan solo el primer caracter de esa cadena de texto
# Debemos realizarlo de la siguiente manera
# Tipo_char = Tipo_string[0]
# Lo que acabamos de realizar fue obtener la primera letra de esa cadena de texto
# Hemos creado una variable y dentro de esa variable hemos llamado a la variable que contenia el texto
# Usamos los corchetes para obtener el dato tipo string a tipo char [0]
Tipo_char = Tipo_string[0]
# Se ha colcado el numero 0 para indicar que queremos obtener la primera letra de este texto
# Cabe aclarar que los numero en programacion empiezan desde 0, a lo que usualmente nosotros lo usamos como 1
# 0 = 1, 1 = 2, 2 = 3, 3 = 4, y asi susecivamente

#       Ejercicio       #
#Muestra el dato de la variable "Tipo_string" y tambien el dato de la variable "Tipo_char"

#Crea una variable llamada "nombre" y usando el input coloca tu nombre para luego ser mostrado en consola

#Adicional crea una variable tipo char y muestra la primera letra de tu nombre para luego ser mostrado en consola

####Ejemplo de codigo####
#nombre_muestra = input("Ingrese su nombre : ")
#print(nombre_muestra)
#nombre_char = nombre_muestra[0]
#print("La primera letra del nombre es ", nombre_char)

#               Fase numero 4 : Uso del dato tipo boolean

#Este tipo de dato es sumamente intutitivo ya que estos son verdaderos o falso, o tambien 1 o 0
#Un ejemplo para poder entenderlo es como el switch de un foco
#Si el foco esta apagado esta en 0 o su dato es falso
#Mientras si nostros apretamos el switch y se enciende el foco esta en 1 o su dato es verdadero
#Lo que hacemos con este tipo de datos es declarar si queremos que se active o se desactive
#Para hacer interactivo vamos a realizar lo siguiente, se creara un ejemplo el cual estara en forma de comentario
#Solo elimina el # de cada linea de codigo a continuacion para que deje de ser comentario y el compilador
#pueda leerlo 
#Codigo
#Foco = False
#opcion = input("Ingrese 1 si desea encender el foco: ")
#if opcion == "1":
#    Foco = True
#    if Foco == True:
#        print("El foco está encendido")
#        opcion2 = input("Si desea apagar el foco ingrese 1: ")
#        if opcion2 == "1":
#            Foco = False
#            print("El foco se apagó")
#        else:
#            print("El foco se mantiene encendido")
#    else:
#        print("El foco se mantuvo apagado")

#Hemos usado una condicional if, la cual nos sirve para validar cierto dato, que si el resultado es igual al esperado realize cierta accion
#Esto lo veremos en la clase numero 3

#Bueno esto fue todo por la primera clase, hay que comentar que los datos toman el tipo una vez colocada el dato
#Es importante que practiquemos el como podemos usarla y animarnos a seguir aprendiendo
#Y sobre todo entender que todos podemos ser programadores

#Podemos usar las variables para poder realizar operaciones, veamos un ejemplo de como podemos utilizar
#Por ejemplo una suma
Num1 = 12
Num2 = 12.5
Resultado = float(Num1+Num2)
print(Resultado)
#Como podemos ver, lo que hicimos es llamar a los datos de la variable mediante su nombre, creamos una nueva variable la cual contendra la operacion
#Y le hemos agregado, la palabra float y entre parentesis los datos para que pase hacer de enteros a decimales, y siemplemente imprimimos el dato
#Con el nombre de la variable de la formula
#Pueden sumarse enteros con enteros, decimales con decimales, o enteros con deciamles, pero debemos especificar el resultado del tipo de dato
#Ahora realizemos una concanetacion
#Vamos a mostrar un texto agregado con el resultado de la suma anterior
Texto = "El resultado fue :"
print(Texto,Resultado)
#Como vemos usamos tanto datos tipos int,float y string para mostrarlo, pero la usar la coma, el programa entiende que esta separado por secciones
#Y de esta manera el codigo con choque entre si, solo interprete en diferentes partes