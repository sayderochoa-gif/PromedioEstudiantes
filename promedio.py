print("Bienvenido a la calculadora de promedIAs")

suma_promedios = 0
numero_estudiantes = int(input("Cuantos estudiantes son: "))

reprobado = 0
aprobado = 0
for i in range(numero_estudiantes):

    name = input("Cual es tu nombre: ")

    print(f"Hola {name} vamos a calcular tu promedio")

    nota1 = float(input("Digita tu primera nota: "))
    nota2 = float(input("Digita tu segunda nota: "))               
    nota3 = float(input("Digita tu tercera nota: ")) 

    promedio = (nota1 + nota2 + nota3) / 3
    suma_promedios += promedio
    print(f"Tu promedio es: {round(promedio, 2)}")  

    if promedio >= 3.0:
        print("Haz aprobado la materia.")
        aprobado +=1
    
    else: 
        print("Haz reprobado tu materia, sigue esforzandote.")
        reprobado +=1

print(f"{reprobado} reprobaron y {aprobado} aprobaron")
print(f"El promedio total de estudiantes es: {round(suma_promedios/numero_estudiantes)}")
