[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Sara Lucía Jara Jaramillo
ID:  000540483
---
### Título del proyecto
Seguimiento de hábitos personales 

### Descripción 
Los hábitos son sumamente importantes para el desarrollo personal, de ellos depende un buen rendimiento, autoconcimiento y estilo de vida. 
Sin embargo, puede ser difícil para muchos organizarce y tener constancia para llevarlos a cabo. Es importante planificar el día a día e implementar rutinas saludables para mejorar y crecer como persona. 
Por ende, es necesario tener un registro de actividades acorde a los gustos y necesidades de cada persona. Teniendo en cuenta esto, 
se busca con este programa facilitarle al usuario establecer hábitos diarios saludables que se ajusten a su estilo de vida y tiempo; donde registre las tareas realizadas y pueda observar su progreso.

### Alcance 
El programa busca ayudar al usuario a implementar hábitos saludables. 
Inicialmente, preguntará información personal: nombre, edad y correo electrónico. 
Luego, información relacionada con los hábitos que desea implementar incluyendo: el hábito (hacer ejercicio, meditar, leer, journaling), los días que lo va a realizar y la duración de este. 
Le permitirá al usuario visualizar su lista de hábitos cumplidos diarios, así como el tiempo que se tomó haciendo cada uno. 
Al final se hará una cuenta de la cantidad de veces y de tiempo que realizó cierta actividad. 

### Estructuras de datos utilizadas
Diccionarios, listas 

### Pseudocódigo

Inicio 

 lista_habitos = []

    Funcion datos_usuario()
      usuario = {}
      Escribir "Ingrese su nombre:"
      Leer nombre 
      Escribir "Ingrese su edad:"
      Leer edad 
      Escribir "Ingrese su correo electrónico:"
      Leer correo
      usuario["nombre"] = nombre 
      usuario["edad"] = edad 
      usuario["correo"] = correo 
      Retornar usuario
    Fin Funcion 

    Funcion agregar_habito()
      habito = {}
      Escribir "Indique el hábito que quiere añadir:"
      Leer nombre_habito
      Escribir "Indique los días de la semana que quiere realizarlo:"
      Leer dias
      Escribir "Indique cuánto tiempo le dedicará a este habito (en minutos):"
      Leer tiempo
      habito["nombre"] = nombre_habito
      habito["dias"] = dias
      habito["tiempo"] = tiempo
      lista_habitos.agregar(habito)
      Escribir ("Hábito agregado correctamente")
    Fin Funcion 

    

            
        