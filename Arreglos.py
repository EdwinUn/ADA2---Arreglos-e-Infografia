import random

ALUMNOS = 500
MATERIAS = 6

tabla = [[random.randint(0, 10) for _ in range(MATERIAS)] for _ in range(ALUMNOS)]

ancho_alumno = 12
ancho_materia = 10

# ===== ENCABEZADO =====
print(f"{'Alumno':<{ancho_alumno}}", end="|")
for m in range(1, MATERIAS + 1):
    print(f"{('Materia ' + str(m)):<{ancho_materia}}|", end="")
print()

print("-" * (ancho_alumno + (ancho_materia + 1) * MATERIAS))

# ===== FILAS =====
for i in range(ALUMNOS):
    print(f"{('Alumno ' + str(i+1)):<{ancho_alumno}}", end="|")
    for cal in tabla[i]:
        print(f"{cal:<{ancho_materia}}|", end="")
    print()

# ===============================
# 🔍 FUNCIÓN PRINCIPAL
# ===============================
def main():
    while True:
        print("\n--- BUSCAR CALIFICACIÓN ---")
        alumno = int(input("Ingresa número de alumno (1-500) o 0 para salir: "))
        
        if alumno == 0:
            print("Saliendo del sistema...")
            break
        
        materia = int(input("Ingresa número de materia (1-6): "))

        alumno_idx = alumno - 1
        materia_idx = materia - 1

        if 0 <= alumno_idx < ALUMNOS and 0 <= materia_idx < MATERIAS:
            print(f"Alumno {alumno}, Materia {materia} = {tabla[alumno_idx][materia_idx]}")
        else:
            print("Número fuera de rango.")


# Ejecutar programa
main()

