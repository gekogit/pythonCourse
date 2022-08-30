import bmi


def print_advice(bmi_return):
    match bmi_return:
        case "Obesity!!!":
            with open('obesity.txt') as f:
                print(f.readline())
        case "Overweight!":
            with open('overweight.txt') as f:
                print(f.readline())
        case "Weight ok.":
            with open('weight _ok.txt') as f:
                print(f.readline())
        case "Underweight!":
            with open('underweight.txt') as f:
                print(f.readline())

def main():
    user_mass = int(input("Write your mass [kg]:..."))
    user_height = float(input("Write your height [m]:..."))
    bmi_status = bmi.check_bmi(user_mass, user_height)
    print(bmi_status)
    print_advice(bmi_status)


if __name__ == '__main__':
    main()
