def invertir_cadena(cadena):
    invertida = ""
    
    cadena = input("Ingresar nombre: ")
    for i in range(len(cadena) - 1, -1, -1):
        invertida += cadena[i]
    return invertida

cadena = ""
print("Cadena invertida:", invertir_cadena(cadena))
