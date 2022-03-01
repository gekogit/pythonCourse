"""
Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

"""
print("\nTo calculate your BMI your mass and height is needed.")

mass = int(input("Write your mass [kg]:..."))
height = float(input("Write your height [m]:..."))
BMI = round(mass/height**2)
print(f'Your BMI roughly is: {BMI}')

if BMI > 30:
    print("Obesity!!!")
elif BMI > 25:
    print("Overweight!")
elif BMI > 19:
    print("Weight ok.")
else:
    print("Underweight!")
