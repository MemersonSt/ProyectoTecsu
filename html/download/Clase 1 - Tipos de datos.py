#Nota : En python la es importante que la sintaxis este correcta
#Nota : Esto esa siendo mostrado como comentario usando el #, por lo que no afecta al codigo a menos que se elimine el # de cada linea
#Nota : Para compilar el programa debemos dar click en el triangulo de lado, en la parte posterior derecha de la pantalla

#Clase 1 
#Tipos de datos
#Dentro del mundo  de la programacion existen varios tipos de datos los cuales son los siguientes
#Int(Numeros enteros)
#Float(Numeros con decimales)
#String(Cadena de texto)
#Char(Caracter)
#Boolean(Verdadero o falso)
#Veamos como es el funcionamiento de estos

#Tipos de datos entero
#Estos tipos de datos nos permite guardar informacion dentro de una variable la cual sera numeros naturales
#Para poder usarlo se lo realiza de la siguiente manera
Numeros_Enteros = 1
Numeros_Enteros1 = 100
Numeros_Enteros2 = -1
#Lo que hemos realizado es crear un variable en la cual se guardan los datos
#En pyhton las variables tomaran un tipo de dato, cuando se le ingrese un dato de cierto tipo
#Podemos ver el contenido de la variable tipo int, usando la siguiente linea de codigo a continuacion
print("Datos tipo int")
print(Numeros_Enteros)
print(Numeros_Enteros1)
print(Numeros_Enteros2)
#Usamos print cuando queremos mostrar el contenido de un dato mediante la consola, de esta forma podemos tanto visualizar
#O guiar al usuario mediante texto como se mostrara a continuacion
print(Numeros_Enteros2," Es un numero negativo")
#Lo que acabamos de realizar, es una concanetacion, lo que es mostrar varios datos en una linea
#Luego de haber colocado el nombre de la variable usamos la, para que entienda el programa que estamos separando por secciones
#Y luego usamos las dobles comillas, que es como se inserta un dato tipo string que veremos mas adelante
#Esto se puede realizar con cualquier tipo de dato o funcion

#Tipos de datos float
#Los datos de tipos float funciona de manera parecida a los datos tipo int, con la particularidad que estos manejan los decimales
#Por ejemplo, si realizamos una divison (11 dividido entre 2), el resultado de esta divison es 5.5
#Eso es un dato tipo float, numeros que usan decimales, cosa que si lo mostramos como un dato tipo int, solo aperece los numeros enteros
#Para poder usarlo se lo realiza de la siguiente 
Numero_float = 5.5
Numero_float1 = 10.66
Numero_float2 = -5.5
#Como vemos, tambien podemos guardar numeros negativos
#Y para poder visualisarlos lo hacemos de igual manera usando el print
print("Datos tipo float")
print(Numero_float)
print(Numero_float1)
print(Numero_float2)

#Tipos de datos string
#Los datos de tipos string con una cadena de texto
#Mostrara toda las palabras que esten dentro de la variable, en la cual podemos guardar informacion como nombres, datos o incluso numeros
#Aunque no es recomendable guardar numeros en una variable tipo string, ya que no podremos realizar calculos mas adelantes
#Para poder usarlo se lo realiza de la siguiente manera
print("Datos tipo string")
Datos_string = "Nombre"
Datos_string1 = 'Hoy esta soleado'
Datos_string2 = "12"
#Lo que hemos usados para que el programa entienda que es un dato tipo string son las dobles comilla " ", y dentro de la doble comillas se coloca
#el texto que deseamos que este
#Tambien se lo puede hacer usando las comillas simples '',
#Lo mostramos a continuacion usando print
print(Datos_string)
print(Datos_string1)
print(Datos_string2)

#Tipos de datos char
#Los datos de tipo char, son resumidamente el uso de caracter, veamos un ejemplo:
nombre = "Juan"
#Tenemos la variable tipo string llamada "nombre", el cual contiene el texto Juan
#Los tipos de datos char, lo que toma en cuenta es el caracter, ya sea numero o letra
#Para poder obtener un caracter, de ese texto debemos hacer lo siguiente
#Crear una nueva variable y usar los corchetes, y dentro de este un numero de acuerdo a la posicion del caracter que queremos obtener
#Pero veamos un ejemplo para entender mejor
Tipo_char = nombre[0]
print(Tipo_char)
#Lo que acabamos de hacer es obtener el primer caracter de este texto, hemos usado el numero 0 porque dentro de la progamacion, es el primer numero
#Por ejemplo las posiciones son de la siguiente manera, 0 = 1, 1 = 2, 2 = 3, 3 = 4, y asi consecutivamente
#Empezamos contando desde cero como numero inicial
#Como usamos 0 dentro del corchete, obtenemos la letra n, siendo esta la letra inicial de este texto, si colocaramos 2, obtendriamos m, siendo
#este la tercera letra del texto

#Tipos de datos boolean
#Son datos de verdadero o falso, o 1 y 0, lo cual si lo vemos con un ejemplo serian como un switch para encender un foco
#Si el dato es verdadero o 1, el foco estara encendido, mientras que si es falso o 0, el foco estara apagado
#Y se lo realiza de la siguiente manera
Encendido = True
Apagado = False
#Estos datos suelen ser complementarios de acciones, la cuales realizaran una funcion si el dato es True o False



