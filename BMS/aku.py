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
    for el in range(1, len(data_sp)-2):
        safe_line(str(int(data_sp[el], 16))+ ',')
    safe_line('\n')


def file_init():
    with open("aku_log.txt", 'a', encoding='utf-8') as log_data:
        log_data.write('v\ta\ttemp\tv1\tv2\tv3\tv4\tb\to\n')


def safe_line(data):
    with open("aku_log.txt", 'a', encoding='utf-8') as log_data:
        log_data.write(data)


def main():
    print('BMS log BTO_14,6V_200Ah')
    file_init()
    ser_port = serial_init()
    check_serial_open(ser_port)
    counter = 0
    while True:
        ser_port.write(b'\x1A\x4F')
        time.sleep(1)
        bytes_to_read = ser_port.inWaiting()
        if bytes_to_read == 73:
            data = ser_port.read(bytes_to_read)
            to_dec(data)
            counter += 1
            print('Sample ', counter)
            time.sleep(1)
        print(data)



if __name__ == '__main__':
    main()


