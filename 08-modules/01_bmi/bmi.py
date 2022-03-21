

def check_bmi(mass, height):
    BMI = round(mass / height ** 2)
    if BMI > 30:
        return "Obesity!!!"
    elif BMI > 25:
        return "Overweight!"
    elif BMI > 19:
        return "Weight ok."
    else:
        return "Underweight!"


def main():
    user_mass = int(input("Write your mass [kg]:..."))
    user_height = float(input("Write your height [m]:..."))
    print(check_bmi(user_mass, user_height))


if __name__ == '__main__':
    main()
