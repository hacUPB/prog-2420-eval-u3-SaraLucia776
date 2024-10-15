usuario = {}
lista_habitos = []
habito_registro = {}
habitos_selec = { 
     "1": "Hacer ejercicio", 
     "2": "Meditar", 
     "3": "Leer",
     "4": "Journaling"
}

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
def agregar_habito():
     nombre_habito = input("Escoja el número del hábito que desea añadir: \n1. Hacer ejercicio\n2. Meditar\n3. Leer\n4. Journaling ")
     if nombre_habito in habitos_selec:
         dias = input("Indique los días de la semana que quiere realizarlo: ")
         tiempo = int(input("Indique cuánto tiempo le dedicará a este hábito (en minutos): "))
         #Añade la información al diccionario habito
         nuevo_habito = {
              "nombre_habito": habitos_selec[nombre_habito],
              "dias" : dias,
              "tiempo" : tiempo
         }
         lista_habitos.append(nuevo_habito)
         print(f"El hábito '{nuevo_habito['nombre_habito']}' ha sido agregado. Recuerda realizarlo el día {dias} por {tiempo} minutos ")
     else: 
          print("Ingrese un número válido")

# Función para marcar un hábito completado
def habito_completado(nombre_habito, tiempo:int):
     fecha = (input("Ingrese la fecha de cuando realizó el hábito (DD/MM/AAAA): "))
     hab_list = False 
     for habito in lista_habitos:
               if habito["nombre_habito"] == nombre_habito: 
                    habito["fecha"] = fecha
                    habito["tiempo"] = tiempo 
                    print(f"Hábito '{nombre_habito}' registrado el día {fecha} con una duración de {tiempo}.")
                    hab_list = True
                    break
     if not hab_list:
        print("Hábito no registrado")

# Función para eliminar hábitos
def habito_delete(nombre_habito):
     for habito in lista_habitos:
          if habito["nombre_habito"] == nombre_habito:
           lista_habitos.remove(habito)
           print(f"Hábito '{nombre_habito}' eliminado")
           return 
     print(f"Hábito no encontrado")

# Función para visualizar los hábitos
def ver_habitos():
     if not lista_habitos: 
               print(f"No hay hábitos agregados")
               return
     for habito in lista_habitos:
          print(f"Hábito: {habito['nombre_habito']}, Días: {habito['dias']}, Tiempo: {habito['tiempo']} minutos")
          
     
                          
if __name__ == "__main__":
 datos_usuario()
 agregar_habito()
 habito_completado("nombre_habito", "tiempo:int")
 habito_delete("nombre_habito")
 ver_habitos()



