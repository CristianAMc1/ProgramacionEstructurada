from funciones import*

def main():
  palabra = seleccionarPalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u b w x y z"
  jugada = ["_"]*len(palabra)

  for turno in range (5):
    print(f"\nTurno: {turno+1}")
    print("-"*20)
    imprimirActualizacion(alfabeto, jugada)

    letra = entradaUsuario()
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    imprimirActualizacion(alfabeto, jugada)
  
    chek = input("Desea adivinar la palabra? (s/n): ")
    if chek.lower() == "s":
      suposision = input("Introdusca su respuesta; ").lower()
      success = verificarJugada(suposision, palabra)
  
      if success:
       print("+"*20)
       print("SIIIUUUUUUU GANOOOOOO :D xd")
       print("+"*20)
       break
    
      else:
       print("+"*20)
       print("La supocicion es incorrecta..,")
       print("+"*20)
    
    if turno == 4:
     print("-"*20)
     print("=( =(Ahorcadooooo noooooooooo")
     print("-"*20)

if __name__ == "__main__":
  main()
