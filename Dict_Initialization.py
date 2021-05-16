def Dict_Init():
    import csv
    filename="Sorceries_Wisdom_of_a_Sage.csv"
    Sorceries_Wisdom_of_a_Sage = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Sorceries_Wisdom_of_a_Sage = line
          
    filename="Knights_Honor_Sorted_by_Categories_Boss_Soul_Weapons.csv"
    Knights_Honor_Sorted_by_Categories_Boss_Soul_Weapons = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Knights_Honor_Sorted_by_Categories_Boss_Soul_Weapons = line
            
            
    filename="guide.csv"
    Guide = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Guide = line

    filename="Knights_Honor_Sorted_by_Categories_Guaranteed_Loot.csv"
    Knights_Honor_Sorted_by_Categories_Guaranteed_Loot = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Knights_Honor_Sorted_by_Categories_Guaranteed_Loot = line

    filename="Knights_Honor_Sorted_by_Categories_Tails.csv"
    Knights_Honor_Sorted_by_Categories_Tails = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Knights_Honor_Sorted_by_Categories_Tails = line

    filename="Knights_Honor_Sorted_by_Categories_Weapon_Drops.csv"
    Knights_Honor_Sorted_by_Categories_Weapon_Drops = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Knights_Honor_Sorted_by_Categories_Weapon_Drops = line

    filename="Knights_Honor_Sorted_by_Inventory_Order.csv"
    Knights_Honor_Sorted_by_Inventory_Order = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Knights_Honor_Sorted_by_Inventory_Order = line

    filename="Miracles_Prayer_of_a_Maiden.csv"
    Miracles_Prayer_of_a_Maiden = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Miracles_Prayer_of_a_Maiden = line

    filename="Pyromancies_Bond_of_a_Pyromancer.csv"
    Pyromancies_Bond_of_a_Pyromancer = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Pyromancies_Bond_of_a_Pyromancer = line

    filename="Weapon_Upgrades_Andre_of_Astora.csv"
    Weapon_Upgrades_Andre_of_Astora = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Weapon_Upgrades_Andre_of_Astora = line

    filename="Weapon_Upgrades_Giant_Blacksmith.csv"
    Weapon_Upgrades_Giant_Blacksmith = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Weapon_Upgrades_Giant_Blacksmith = line

    filename="Weapon_Upgrades_Rickert_of_Vinheim.csv"
    Weapon_Upgrades_Rickert_of_Vinheim = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Weapon_Upgrades_Rickert_of_Vinheim = line

    filename="Weapon_Upgrades_Vamos.csv"
    Weapon_Upgrades_Vamos = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            Weapon_Upgrades_Vamos = line