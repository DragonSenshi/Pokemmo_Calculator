print("***********************************************************")
print("* Bienvenido a la calculadora de costos para cría pokemmo *")
print("***********************************************************")


print("¿El pokemon a criar lo quieres con una naturaleza específica?: \n")
naturaleza = int(input("Si (1 \nNo (2 \n:"))

import math

if naturaleza == 1:
    print("¿Vas a criar un pokemon de una especie rara o con una especie común?: \n")
    poke_raro = int(input("especie rara (1 \nespecie común (2 \n:"))

    
    if poke_raro == 1:
        sexo_1 = int(input("Introduce el precio de elegir el género del breeder: "))
        sexo_2 = int(input("Introduce el precio de elegir el género del pokemon: "))
        piedraeterna = int(input("Introduce el precio de la piedraeterna: "))
        cant_est = int(input("¿De cuantas estadísticas quieres a tu cría? (2-6): "))
    
        if cant_est >= 2 and cant_est <= 6:
            cant_poke = int(2 ** (cant_est - 1) * 2)
            cost_brazales = int((10000 * (math.log2(cant_poke) * 2)) - (cant_est * 10000))
            cost_sexo = int((sexo_1 * (cant_poke / (2**(cant_est - 1)))) - (cant_est * sexo_1) + (cant_est * sexo_2))
            piedraeterna = cant_est * piedraterna
            cost_total =int(cost_brazales + cost_sexo + piedraeterna)
            print("La cantidad de pokemones que necesitas es:", cant_poke)
            print("El costo total para la cría que quieres es de: $", cost_total)
            print("$", cost_sexo, "para elegir el sexo de la cría")
            print("$", cost_brazales, "para los 'Power Item' y $", piedraeterna)
            
        else:
            print("El número introducido no es aceptable.")

            
    elif poke_raro == 2:
        sexo_1 = int(input("Introduce el precio de elegir el género del breeder: "))
        sexo_2 = 0
        piedraeterna = int(input("Introduce el precio de la piedraeterna: "))
        cant_est = int(input("¿De cuantas estadísticas quieres a tu cría? (2-6): "))
    
        if cant_est >= 2 and cant_est <= 6:
            cant_poke = int(2 ** (cant_est - 1) * 2)
            cost_brazales = int(10000 * (math.log2(cant_poke) * 2) - (cant_est * 10000))
            cost_sexo = int((sexo_1 * (cant_poke / (2**(cant_est - 1)))))
            cost_total =int(cost_brazales + cost_sexo + piedraeterna)
            print("La cantidad de pokemones que necesitas es:", cant_poke)
            print("El costo total para la cría que quieres es de: $", cost_total)
            print("$", cost_sexo, "para elegir el sexo de la cría")
            print("$", cost_brazales, "para los 'Power Item' y $", piedraeterna)
            
        else:
            print("El número introducido no es aceptable.")

            
    else:
        print("Esa opción no está disponible") 


elif naturaleza == 2:
    print("¿Vas a criar un pokemon de una especie rara o con una especie común?: \n")
    poke_raro = int(input("especie rara (1 \nespecie común (2 \n:"))
    if poke_raro == 1:
        sexo_1 = int(input("Introduce el precio de elegir el género del breeder: "))
        sexo_2 = int(input("Introduce el precio de elegir el género del pokemon: "))
        cant_est = int(input("¿De cuantas estadísticas quieres a tu cría? (2-6): "))
    
        if cant_est >= 2 and cant_est <= 6:
            cant_poke = int(2 ** (cant_est - 2) * 2)
            cost_brazales = int(10000 * (math.log2(cant_poke) * 2))
            cost_sexo = int((sexo_1 * (cant_poke / (2**(cant_est - 1)))) - (cant_est * sexo_1) + (cant_est * sexo_2))
            cost_total =int(cost_brazales + cost_sexo)
            print("La cantidad de pokemones que necesitas es:", cant_poke)
            print("El costo total para la cría que quieres es de: $", cost_total)
            print("$", cost_sexo, "para elegir el sexo de la cría")
            print("$", cost_brazales, "para los 'Power Item'")
        else:
            print("El número introducido no es aceptable.")



    elif poke_raro == 2:
        sexo_1 = int(input("Introduce el precio de elegir el género del breeder: "))
        sexo_2 = 0
        cant_est = int(input("¿De cuantas estadísticas quieres a tu cría? (2-6): "))
    
        if cant_est >= 2 and cant_est <= 6:
            cant_poke = int(2 ** (cant_est - 2) * 2)
            cost_brazales = int(10000 * (math.log2(cant_poke) * 2))
            cost_sexo = int((sexo_1 * (cant_poke / (2**(cant_est - 1)))))
            cost_total =int(cost_brazales + cost_sexo)
            print("La cantidad de pokemones que necesitas es:", cant_poke)
            print("El costo total para la cría que quieres es de: $", cost_total)
            print("$", cost_sexo, "para elegir el sexo de la cría")
            print("$", cost_brazales, "para los 'Power Item'")
        else:
            print("El número introducido no es aceptable.")
        
    else:
        print("Esa opción no está disponible") 


    
else:
    print("Esa opción no está disponible")

print("Fin.")
