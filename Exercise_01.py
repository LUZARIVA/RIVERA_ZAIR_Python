nombre = input("¿Cuál es tu nombre?:")
Primer_apelido = input("¿Cuál es tu primer apellido?: ")
Segundo_apellido = (input("¿Cuál es tu segundo apellido?: "))
Año_nacimiento = int(input("¿En qué año naciste?: "))

fecha_nacimiento = input("¿En qué día y mes naciste? (formato dd-mm): ")
dia, mes = fecha_nacimiento.split("-")
dia_nacimiento = int(dia)
mes_nacimiento = int(mes)


nombre_completo = f"{nombre} {Primer_apelido} {Segundo_apellido}"
nombre_completo_mayusc = nombre_completo.upper()
print(f"Tu nombre en mayúsculas es: {nombre_completo_mayusc}")


nombre_completo = f"{nombre} {Primer_apelido} {Segundo_apellido}"
nombre_completo_minusc = nombre_completo.lower()
print(f"Tu nombre en minúsculas es: {nombre_completo_minusc}")



fecha_completa = f"{fecha_nacimiento}-{Año_nacimiento}"
print(f"Esta es tu fecha de nacimiento: {fecha_completa}")



vocales = "AEIOUaeiou"
conteo_vocales = 0
for letra in nombre_completo:
    if letra in vocales:
        conteo_vocales += 1
print(f"Mi nombre completo tiene {conteo_vocales} vocales")


conteo_letras = len(nombre_completo)
print(f"Mi nombre completo tiene {conteo_letras} letras")


nombre_completo = f"{nombre} {Primer_apelido} {Segundo_apellido}"
if nombre_completo.isalnum():
    print("Tu nombre completo es alfanumérico")
else:
    print("Tu nombre completo no es alfanumérico")


edad_en_10_anios = 10 + (2023 - Año_nacimiento)

print(f"Tu edad en 10 años será: {edad_en_10_anios}")


# Obtener la edad actual
edad_actual = 2022 - Año_nacimiento

# Obtener la edad en 20 años
edad_en_20_anios = edad_actual + 20

# Obtener la media de la edad actual y la edad en 20 años
media_edades = (edad_actual + edad_en_20_anios) / 2

# Imprimir el resultado
print(f"La media de tu edad actual y tu edad en 20 años es: {media_edades}")
