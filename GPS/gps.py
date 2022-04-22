import serial
import datetime


def serial_init():
    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    return ser


def check_serial_open(ser):
    if ser.isOpen():
        print(ser.name + '\nSerial is open...')


def file_init():
    with open("gps_log.txt", 'a', encoding='utf-8') as log_data:
        log_data.write('GPS frame')


def main():

    print('GPS')
    file_init()
    gps_serial = serial_init()
    while True:
        bytes_to_read = gps_serial.inWaiting()
        data = gps_serial.read(bytes_to_read)
        print(data)


if __name__ == '__main__':
    main()


