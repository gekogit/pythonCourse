distance = 120
consumption = 6.4
literPrice = 5.04
costs = consumption/100 * distance * literPrice
print(f'\nDistance [km]: {distance} \nConsumption [l/100km]: {consumption} \nPrice per liter [PLN/l]: {literPrice} \nYour costs: {round(costs,2)} PLN')

distance = int(input("Write distance [km]:.."))
consumption = float(input("Write your car consumption [l/100km]:.."))
literPrice = float(input("Write gas price [PLN]:.."))
print(f'\nDistance [km]: {distance} \nConsumption [l/100km]: {consumption} \nPrice per liter [PLN/l]: {literPrice} \nYour costs: {round(costs,2)} PLN')
