from palabras import obtener_palabra_aleatoria
from muñeco import ETAPAS_AHORCADO

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = set()
    letras_intentadas = set()
    vidas = 6
    
    print("\n========================================")
    print("      ¡BIENVENIDO AL JUEGO DEL AHORCADO     ")
    print("========================================")

    while vidas > 0:
        # Generar la visualización de la palabra oculta con guiones bajos
        palabra_mostrada = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
        
        print(f"\nPalabra oculta: {palabra_mostrada}")
        print(f"Vidas restantes: {vidas}")
        
        entrada = input("Ingrese una letra: ").strip()

        if len(entrada) != 1 or not entrada.isalpha():
            print("Debe ingresar solo 1 letra")
            continue

        letra = entrada.upper()
        if letra in letras_intentadas:
            print("Ya ha utilizado la letra")
            continue

        letras_intentadas.add(letra)

        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            
            if all(l in letras_adivinadas for l in palabra_secreta):
                print(f"\n¡Ganaste! La palabra oculta era: {palabra_secreta}")
                break
        else:
            vidas -= 1
            indice_error = 6 - vidas
            print(ETAPAS_AHORCADO[indice_error])
            
            # Comprobar si se quedó sin vidas
            if vidas == 0:
                print("Has perdido")
                print(f"La palabra oculta era: {palabra_secreta}")
                break

def main():
    while True:
        jugar_ahorcado()
        
        opcion = input("\n¿Qué desea hacer?\n1. Jugar de nuevo\n2. Finalizar programa\nSeleccione una opción (1 o 2): ").strip()
        
        if opcion == '2':
            print("¡Gracias por jugar! Finalizando programa.")
            break
        elif opcion != '1':
            print("Opción no válida, pero se cerrará el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()