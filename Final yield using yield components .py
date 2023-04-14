seed_weight = float(input("1000-Seed Weight (g):"))
seed_number = int(input("Seed Number per Plant:"))
plant_number = int(input("Plant Number per Hectare:"))

Yield = round(seed_weight * seed_number * plant_number/1000000)
if Yield <= 1000:
     print('Final yield:', Yield,'kg/ha which means low yield')
elif Yield > 1000 and Yield < 1500:
     print('Final yield:', Yield,'kg/ha which means moderate yield')
elif Yield > 1500:
     print('Final yield:', Yield,'kg/ha which means high yield')
else:
    print('There is an error with your input')
