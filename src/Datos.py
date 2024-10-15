import datetime

usuario = {}
lista_habitos = []


# Función para el registro del usuario
def datos_usuario():
        nombre  = input("Ingrese su nombre completo: ").upper()
        edad = int(input("Ingrese su edad: "))
        correo = input("Ingrese su correo electrónico: ")
        # Añade la información al diccionario usuario
        usuario["Nombre"] = nombre 
        usuario["Edad"] = edad 
        usuario["Correo electrónico"] = correo
        
        print(f"{nombre}, su información ha sido guardada correctamente")

#Función para agregar un hábito
def agregar_habito(nombre_habito):
     if nombre_habito not in lista_habitos:
         dias = input("Indique los días de la semana que quiere realizarlo: ")
         tiempo = int(input("Indique cuánto tiempo le dedicará a este hábito (en minutos): "))
         #Añade la información al diccionario habito
         nuevo_habito = {
              "nombre_habito": nombre_habito,
              "dias" : dias,
              "tiempo" : tiempo
         }
         lista_habitos.append(nuevo_habito)
         print(f"El hábito '{nuevo_habito['nombre_habito']}' ha sido agregado. Recuerda realizarlo el día {dias} por {tiempo} minutos ")
     else: 
          print("Ingrese un nuevo habito")

# Función para marcar un hábito completado
def habito_completado(nombre_habito):
    for habito in lista_habitos:
        if habito["nombre_habito"] == nombre_habito:
            fecha_completado = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Hábito '{nombre_habito}' completado el {fecha_completado}.")
            return
    print(f"Hábito '{nombre_habito}' no encontrado.")   

# Función para visualizar los hábitos
def ver_habitos():
     if not lista_habitos: 
               print(f"No hay hábitos agregados")
               return
     for habito in lista_habitos:
          print(f"Hábito: {habito['nombre_habito']}, Días: {habito['dias']}, Tiempo: {habito['tiempo']} minutos")

# Función para eliminar hábitos
def habito_delete(nombre_habito):
     print("Indique el hábito que desea eliminar: ")
     for i in range(len(lista_habitos)):
          if lista_habitos[i]["nombre_habito"] == nombre_habito:
           del lista_habitos[i]
           print(f"Hábito '{nombre_habito}' eliminado")
           return 
     print(f"Hábito no encontrado")

#Función menú 
def menu():
     while True:
          opcion = int(input("¿Qué desea realizar?: \n1. Resgistrar usuario\n2. Agregar un hábito\n3. Marcar un hábito completado\n4. Visualizar sus hábitos\n5. Eliminar un hábito\n6. Salir "))
          if opcion == 1: 
               datos_usuario()
          elif opcion == 2: 
               nombre_habito = int(input("Escoja el número del hábito que desea añadir: \n1. Hacer ejercicio\n2. Meditar\n3. Leer\n4. Journaling "))
               if nombre_habito == 1:
                    nombre_habito = ("Hacer ejercicio")
               elif nombre_habito == 2:
                    nombre_habito = ("Meditar")
               elif nombre_habito == 3:
                    nombre_habito = ("Leer")
               else: 
                    nombre_habito = ("Journaling")
               agregar_habito(nombre_habito)
          elif opcion == 3:
               nombre_habito = int(input("Escoja el número del hábito que completó: \n1. Hacer ejercicio\n2. Meditar\n3. Leer\n4. Journaling "))
               if nombre_habito == 1:
                    nombre_habito = ("Hacer ejercicio")
               elif nombre_habito == 2:
                    nombre_habito = ("Meditar")
               elif nombre_habito == 3:
                    nombre_habito = ("Leer")
               else: 
                    nombre_habito = ("Journaling")
               habito_completado(nombre_habito)
          elif opcion == 4:
               ver_habitos()
          elif opcion == 5: 
               nombre_habito = int(input("Escoja el número del hábito que desea eliminar: \n1. Hacer ejercicio\n2. Meditar\n3. Leer\n4. Journaling "))
               if nombre_habito == 1:
                    nombre_habito = ("Hacer ejercicio")
               elif nombre_habito == 2:
                    nombre_habito = ("Meditar")
               elif nombre_habito == 3:
                    nombre_habito = ("Leer")
               else: 
                    nombre_habito = ("Journaling")
               habito_delete()
          else: 
               print("Saliendo del programa")
               break           
# Correcciones hechas con ayuda de chat gpt y copilot     
                          
if __name__ == "__main__":
     menu()


