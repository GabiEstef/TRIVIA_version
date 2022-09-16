
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random 
import time

puntaje = 0
iniciar_trivia = True
intentos = 0

puntaje = random.randint(0, 10)
print (GREEN+"Bienvenid@ a mi trivia sobre Biologia")

time.sleep(1)

print ("Pondremos a prueba tus conocimientos"+RESET)

time.sleep(2)

print ("Tienes", puntaje, "puntos")

nombre = input ("Ingresa tu nombre: ")

time.sleep(2)

print (BLUE+"\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)

while iniciar_trivia == True:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  time.sleep(2)
  # Pregunta 1
  print (MAGENTA+"1) ¿Dónde realizan las plantas la fotosíntesis?"+RESET)
  print ("")
  print ("a) En el tallo")
  print ("b) En el aire")
  print ("c) En la raíz")
  print ("d) En las hojas")
  
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "d":
    puntaje += 10
    print ("Muy bien", nombre, "!")
  else:
    print ("Incorrecto", nombre, "!")
  print("")
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)

  time.sleep(2)
  # Pregunta 2
  print (MAGENTA+"\n2) ¿Qué músculo impulsa la sangre por todo nuestro cuerpo?"+RESET)
  print ("")
  print ("a) Corazon")
  print ("b) Cerebro") 
  print ("c) Pulmones")
  print ("d) Lengua")
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "b":
    print ("Incorrecto!", nombre)
    puntaje = puntaje - 5
  elif respuesta_2 == "c":
    print ("Incorrecto!", nombre)
    puntaje = puntaje / 2
  elif respuesta_2 == "d":
    print ("Incorrecto!", nombre)
  else:
    puntaje += 10
    print ("Muy bien", nombre, "!")
  print("")
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)
  
  time.sleep(2)
  # Pregunta 3
  print (MAGENTA+"\n3) ¿Qué necesitan las células para dividirse?"+RESET)
  print ("")
  print ("a) Nada")
  print ("b) Sangre")
  print ("c) Energia")
  print ("d) Otra celula")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje - 5
  elif respuesta_3 == "b":
    print ("...")
    puntaje = puntaje / 2
  elif respuesta_3 == "d":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
  print("")
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)
  time.sleep(2)
  # Pregunta 4
  print (MAGENTA+"\n4) ¿Qué tipos de semillas hay?"+RESET)
  print ("")
  print ("a) Monocotiledóneas")
  print ("b) Monocotiledóneas y dicotiledóneas.")
  print ("c) Dicotiledóneas.")
  print ("d) Con fruto o sin fruto")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje - 5
  elif respuesta_3 == "c":
    print ("...")
    puntaje = puntaje / 2
  elif respuesta_3 == "d":
    print ("Incorrecto! ...")
    puntaje = puntaje - 10
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 4
    print ("")
  print("")
  print(RED+ nombre, "llevas", puntaje, "puntos"+RESET)
  time.sleep(2)
  print("")
  print (CYAN+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  
  print(GREEN+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
  
  if repetir_trivia != "si":
    print(YELLOW+"\nEspero", nombre,"que lo hayas pasado bien, hasta pronto!"+RESET)
    iniciar_trivia = False  