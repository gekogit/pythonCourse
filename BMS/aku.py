import serial
import time


def serial_init():
    ser = serial.Serial(
        port='COM13',
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


def to_dec(data):
    data_sp = data.decode("utf-8")
    data_sp = data_sp.split(',')
    data_sp[1] = int(data_sp[1])
    data_sp[2] = int(data_sp[2])
    return data_sp


def main():
    ser_port = serial_init()
    check_serial_open(ser_port)
    while True:
        value = 0x1A4F
        ser_port.write(b'\x1A\x4F')
        time.sleep(1)
        bytes_to_read = ser_port.inWaiting()
        data = ser_port.read(bytes_to_read)
        time.sleep(1)
        print(data)
        #print(to_dec(data))


if __name__ == '__main__':
    main()


