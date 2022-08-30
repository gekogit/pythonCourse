"""
W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.
"""


def check_bmi(mass, height):
    bmi = round(mass / height ** 2)
    if bmi > 30:
        return "Obesity!!!"
    elif bmi > 25:
        return "Overweight!"
    elif bmi > 19:
        return "Weight ok."
    else:
        return "Underweight!"


def main():
    try:
        user_mass = int(input("Write your mass [kg]:..."))
    except(ValueError, TypeError):
        print('Error, try again, type correctly [kg]')
        user_mass = int(input("Write your mass [kg]:..."))

    try:
        user_height = float(input("Write your height [m]:..."))
    except(ValueError, TypeError):
        print("Error, type in meters[m]! ")
        user_height = float(input("Write your height [m]:..."))

    print(check_bmi(user_mass, user_height))


if __name__ == '__main__':
    main()
