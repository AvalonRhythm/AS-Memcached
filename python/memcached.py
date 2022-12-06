from pymemcache.client import base

client = base.Client(('memcached', 11211))
results = [""]
resultsSQL = [""]

print("# ***************** \\\\\\TAREAS BÁSICAS////// ***************** #")

#------------------- EJEMPLO 1 -------------------#

print("* Ejemplo 1: Intentamos obtener un dato pasandole su clave y si no existe lo creamos \n")

#Mostrar elemeto almacenado en caché
data = client.get("Ejemplo1")

if not data:
	#Si no existe el elemento lo guardamos durante 90 segundos
	client.set(key="Ejemplo1", value="Hola Mundo", expire=90)
	data = client.get(key="Ejemplo1")
	print("El elemento ha sido guardado en caché durante 90 segundos")

print("Si funciona correctamente deberia imprimir el mensaje 'Hola Mundo': \n\n", data.decode('utf-8'), "\n")
results.append("El dato es: " + data.decode("utf-8") + "\n")

#------------------- EJEMPLO 2 -------------------#

print("* Ejemplo 2: Almacenamos un dato numérico e incrementamos y decrementamos su valor \n")

data = client.get("Ejemplo2")
if not data:
	#Si no existe el elemento lo guardamos durante 90 segundos
	client.set(key="Ejemplo2", value=1, expire=90) 
	data = client.get(key="Ejemplo2")
	
#El valor del dato es 1
print("El valor del dato es: ", data.decode('utf-8'), "\n")
results.append("El dato es: " + data.decode("utf-8") + "\n")

print("Incrementamos el valor en cuatro: \n")
#Incrementamos el valor del dato almacenado en 4
client.incr(key="Ejemplo2", value=4)

#Ahora el valor del dato es 5
data = client.get(key="Ejemplo2")
print("El valor del dato es: ", data.decode('utf-8'), "\n")
results.append("El dato es: " + data.decode("utf-8") + "\n")

print("Decrementamos el valor en cuatro: \n")
#Decrementamos el valor del dato almacenado en 4
client.decr(key="Ejemplo2", value=4)

#Ahora el valor del dato es 1
data = client.get(key="Ejemplo2")
print("El valor del dato es: ", data.decode('utf-8'), "\n")
results.append("El dato es: " + data.decode("utf-8") + "\n")

with open('data/results.txt', 'wb') as file:
	mssg = "+ Resultados tarea base: memcached \n"
	file.write(mssg.encode('utf-8', 'ignore'))
	for line in results:
		file.write(line.encode('utf-8', 'ignore'))


print("# ***************** \\\\\\TAREA ADICIONAL////// ***************** #")


import mysql.connector

connection = mysql.connector.connect(
	user='root', password='root', host='mysql', port="3306", database='db')

print("DB connected \n")

#------------------- EJEMPLO 1 -------------------#

cursor = connection.cursor()

print("Ejecutamos la siguiente consulta: SELECT * FROM students")
cursor.execute('SELECT * FROM students')

students = cursor.fetchall()

print("El resultado obtenido es el siguiente: ", students, "\n")

print(" ---------------------------------------------------- \n")

for i in range(0,5):

	data = client.get("DatosEstudiantes")
	if not data:
		#Si no existe el elemento lo guardamos durante 90 segundos
		client.set(key="DatosEstudiantes", value=str(students), expire=10) 
		data = client.get(key="DatosEstudiantes")
		print("+ Iteración número " + str(i) + " : El dato se ha guardado en caché durante 10 segundos: \n")
		print(data.decode("utf-8") + "\n")
	else:
		print("+ Iteración número " + str(i) + " : El dato ha sido recuperado del caché \n")
		print(data.decode("utf-8") + "\n")


with open('data/results.txt', 'ab') as file:
	mssg = "+ Resultados tarea adicional: MySQL + memcached \n"
	file.write(mssg.encode('utf-8', 'ignore'))
	mssg = "El valor del dato es: " + str(students) + "\n"
	file.write(mssg.encode('utf-8', 'ignore'))

connection.close()

client.close()





