print("***********************************************************")
print("* Welcome to the Pokemmo Breeding Cost Calculator *")
print("***********************************************************")

print("Do you want the bred Pokemon to have a specific nature?\n")
nature = int(input("Yes (1)\nNo (2)\n:"))

import math

if nature == 1:
    print("Are you breeding a rare species or a common species?\n")
    rare_pokemon = int(input("Rare species (1)\nCommon species (2)\n:"))

    if rare_pokemon == 1:
        gender_1 = int(input("Enter the cost of choosing the breeder's gender: "))
        gender_2 = int(input("Enter the cost of choosing the Pokemon's gender: "))
        everstone = int(input("Enter the cost of the Everstone: "))
        num_stats = int(input("How many stats do you want in your offspring? (2-6): "))

        if 2 <= num_stats <= 6:
            num_pokemon = int(2 ** (num_stats - 1) * 2)
            cost_power_items = int((10000 * (math.log2(num_pokemon) * 2)) - (num_stats * 10000))
            cost_gender = int((gender_1 * (num_pokemon / (2**(num_stats - 1)))) - (num_stats * gender_1) + (num_stats * gender_2))
            everstone_cost = num_stats * everstone
            total_cost = int(cost_power_items + cost_gender + everstone_cost)
            print("The number of Pokemon you need is:", num_pokemon)
            print("The total cost for the desired breeding is: $", total_cost)
            print("$", cost_gender, "to choose the offspring's gender")
            print("$", cost_power_items, "for the Power Items and $", everstone_cost)

        else:
            print("The entered number is not acceptable.")

    elif rare_pokemon == 2:
        gender_1 = int(input("Enter the cost of choosing the breeder's gender: "))
        gender_2 = 0
        everstone = int(input("Enter the cost of the Everstone: "))
        num_stats = int(input("How many stats do you want in your offspring? (2-6): "))

        if 2 <= num_stats <= 6:
            num_pokemon = int(2 ** (num_stats - 1) * 2)
            cost_power_items = int(10000 * (math.log2(num_pokemon) * 2) - (num_stats * 10000))
            cost_gender = int((gender_1 * (num_pokemon / (2**(num_stats - 1)))))
            total_cost = int(cost_power_items + cost_gender + everstone)
            print("The number of Pokemon you need is:", num_pokemon)
            print("The total cost for the desired breeding is: $", total_cost)
            print("$", cost_gender, "to choose the offspring's gender")
            print("$", cost_power_items, "for the Power Items and $", everstone)

        else:
            print("The entered number is not acceptable.")

    else:
        print("That option is not available")

elif nature == 2:
    print("Are you breeding a rare species or a common species?\n")
    rare_pokemon = int(input("Rare species (1)\nCommon species (2)\n:"))
    if rare_pokemon == 1:
        gender_1 = int(input("Enter the cost of choosing the breeder's gender: "))
        gender_2 = int(input("Enter the cost of choosing the Pokemon's gender: "))
        num_stats = int(input("How many stats do you want in your offspring? (2-6): "))

        if 2 <= num_stats <= 6:
            num_pokemon = int(2 ** (num_stats - 2) * 2)
            cost_power_items = int(10000 * (math.log2(num_pokemon) * 2))
            cost_gender = int((gender_1 * (num_pokemon / (2**(num_stats - 1)))) - (num_stats * gender_1) + (num_stats * gender_2))
            total_cost = int(cost_power_items + cost_gender)
            print("The number of Pokemon you need is:", num_pokemon)
            print("The total cost for the desired breeding is: $", total_cost)
            print("$", cost_gender, "to choose the offspring's gender")
            print("$", cost_power_items, "for the Power Items")

        else:
            print("The entered number is not acceptable.")

    elif rare_pokemon == 2:
        gender_1 = int(input("Enter the cost of choosing the breeder's gender: "))
        gender_2 = 0
        num_stats = int(input("How many stats do you want in your offspring? (2-6): "))

        if 2 <= num_stats <= 6:
            num_pokemon = int(2 ** (num_stats - 2) * 2)
            cost_power_items = int(10000 * (math.log2(num_pokemon) * 2))
            cost_gender = int((gender_1 * (num_pokemon / (2**(num_stats - 1)))))
            total_cost = int(cost_power_items + cost_gender)
            print("The number of Pokemon you need is:", num_pokemon)
            print("The total cost for the desired breeding is: $", total_cost)
            print("$", cost_gender, "to choose the offspring's gender")
            print("$", cost_power_items, "for the Power Items")

        else:
            print("The entered number is not acceptable.")

    else:
        print("That option is not available")

else:
    print("That option is not available")

print("End.")
