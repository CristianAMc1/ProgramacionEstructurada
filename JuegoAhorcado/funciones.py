import random

def seleccionarPalabra():
  lineas = open("Frutas_Verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra
  
def entradaUsuario():

  letra = input("Introdusca una letra: ")
  return letra.lower()

def actualizarJugada(palabra,letra,jugada):
  n_letras = len(palabra)
  
  for i in range(0, n_letras): 
    if palabra[i] == letra:
      jugada[i] = letra

  return jugada

def actualizarAlfabeto(letra,alfabeto):
  alfabeto = alfabeto.replace(letra," ")
  return alfabeto

def imprimirActualizacion(alfabeto, jugada):
  print(f"Jugada: {jugada}")
  print(f"Letras disponibles: {alfabeto} ")
  
def verificarJugada(suposision, palabra):
  success = False
  if suposision == palabra:
    success = True
  return success

