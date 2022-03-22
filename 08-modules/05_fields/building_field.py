import fields


def print_menu():
    print("Shape of the room:\n1 - square \n2 - rectangle \n3 - triangle")


def main():
    rooms = int(input("Number of rooms?:"))
    total_field = 0
    for r in range(rooms):
        print_menu()
        room_type = input()
        match room_type:
            case '1':
                side = float(input("Write base:"))
                room_field = fields.square(side)
                total_field += room_field
            case '2':
                a = float(input("Write a:"))
                b = float(input("Write b:"))
                room_field = fields.rectangle(a, b)
                total_field += room_field
            case '3':
                a = float(input("Write a:"))
                h = float(input("Write h:"))
                room_field = fields.triangle(a, h)
                total_field += room_field
            case _:
                print("Wrong input")
    print(f'Total field = {round(total_field,2)}')


if __name__ == '__main__':
    main()
