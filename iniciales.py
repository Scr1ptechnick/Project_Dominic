# Nombre: Programa para obtener iniciales en mayúscula

#Entradas: 
#   Nombre: Nombre de la persona , 
#   Apellido: Apellido de la persona

#Salidas:
#   iniciales: La primera letra de Nombre y Apellido

#Proceso: Pide el nombre y el apellido de la persona, extrae la primera letra de el nombre y el apellido. Imprime en mayuscula las iniciales.



# Pedir nombre y apellido
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

# Tomar la primera letra de cada uno y ponerla en mayúscula
iniciales = nombre[0].upper() + apellido[0].upper()

# Mostrar el resultado
print("Tus iniciales son:", iniciales)