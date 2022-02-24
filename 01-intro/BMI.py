print("\nTo calculate your BMI your mass and height is needed.")

mass = int(input("Write your mass [kg]:..."))
height = float(input("Write your height [m]:..."))

print(f'Your BMI roughly is: {round(mass/height**2)}')
