def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'El desplazamiento debe ser un número entero.'
    if shift < 1 or shift > 25:
        return 'El desplazamiento debe estar entre 1 y 25.'
    if not encrypt:
        shift = -shift
        
    # 1. Lógica para las letras (26 caracteres)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # 2. Lógica para los números (10 caracteres)
    numbers = '0123456789'
    shift_num = shift % 10  # El operador módulo (%) ajusta el salto a 10 dígitos
    shifted_numbers = numbers[shift_num:] + numbers[:shift_num]
    
    # 3. Construimos la tabla de traducción final uniendo letras mayúsculas, minúsculas y números
    caracteres_originales = alphabet + alphabet.upper() + numbers
    caracteres_movidos = shifted_alphabet + shifted_alphabet.upper() + shifted_numbers
    
    translation_table = str.maketrans(caracteres_originales, caracteres_movidos)
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

# === INTERFAZ DE USUARIO ===

print("========================================")
print(" 🔒 MÁQUINA DE CIFRADO CÉSAR PRO 🔒 ")
print("========================================")

while True:
    print("\nOpciones:")
    print("1. Encriptar un mensaje")
    print("2. Desencriptar un mensaje")
    print("3. Salir")
    
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    if opcion == '3':
        print("\nApagando la máquina... ¡Hasta pronto, Domingo!")
        break
        
    if opcion in ['1', '2']:
        mensaje = input("\n📝 Escribe tu mensaje (letras y números): ")
        
        # Este 'try' protege al programa si el usuario escribe letras en vez de números
        try:
            saltos = int(input("🔑 Número de saltos (1-25): "))
        except ValueError:
            print("❌ Error: Debes escribir un número entero. Intenta de nuevo.")
            continue
            
        if opcion == '1':
            resultado = encrypt(mensaje, saltos)
            print(f"\n🔐 MENSAJE ENCRIPTADO: {resultado}")
        elif opcion == '2':
            resultado = decrypt(mensaje, saltos)
            print(f"\n🔓 MENSAJE DESENCRIPTADO: {resultado}")
    else:
        print("\n❌ Opción no válida. Por favor elige 1, 2 o 3.")