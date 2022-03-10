"""
Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
"""


def checkBmi(mass, height):
    BMI = round(mass / height ** 2)
    if BMI > 30:
        return "Obesity!!!"
    elif BMI > 25:
        return "Overweight!"
    elif BMI > 19:
        return "Weight ok."
    else:
        return "Underweight!"


userMass = int(input("Write your mass [kg]:..."))
useHeight = float(input("Write your height [m]:..."))
print(checkBmi(userMass, useHeight))

