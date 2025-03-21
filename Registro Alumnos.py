alumA = set()
alumB = set()

while True:
    print("\nSistema de Registro de Alumnos y Cursos")
    print("1. Agregar alumno al Curso A")
    print("2. Agregar alumno al Curso B")
    print("3. Lista de alumnos en ambos cursos ")
    print("4. Lista de alumnos inscritos en los dos cursos ")
    print("5. Lista de alumnos solo en el Curso A ")
    print("6. Lista de alumnos solo en el Curso B ")
    print("7. Lista de alumnos inscritos en un solo curso pero no en ambos ")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        nom = input("Ingrese el nombre del alumno para Curso A: ")
        alumA.add(nom)
        print(f"Alumno {nom} agregado con éxito a Curso A.")
    elif opcion == '2':
        nom = input("Ingrese el nombre del alumno para Curso B: ")
        alumB.add(nom)
        print(f"Alumno {nom} agregado con éxito a Curso B.")
    elif opcion == '3':
        print("Alumnos en al menos un curso:", alumA | alumB)
    elif opcion == '4':
        print("Alumnos en ambos cursos:", alumA & alumB)
    elif opcion == '5':
        print("Alumnos solo en Curso A:", alumA - alumB)
    elif opcion == '6':
        print("Alumnos solo en Curso B:", alumB - alumA)
    elif opcion == '7':
        print("Alumnos en un solo curso pero no en ambos:", alumA ^ alumB)
    elif opcion == '8':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")