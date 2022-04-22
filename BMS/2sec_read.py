import serial
import time
import datetime


def serial_init(com_port):
    try:
        ser = serial.Serial(
            port=com_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
    except Exception:
        print("Check port settings.")
        serial_init(input("Type com port ('COM13'):"))

    return ser


def check_serial_open(ser):
    if ser.isOpen():
        print(ser.name + '\nSerial is open...')
    else:
        print('Can not open the port.')
        raise Exception('port problem')


def to_dec(data):
    now = datetime.datetime.now()
    data_sp = data.decode("utf-8")
    data_sp = data_sp.split(',')
    v = str(int(data_sp[1], 16)) + ','
    print("V = ", v)
    safe_line(v)
    if int(data_sp[2], 16) > 1294967295:
        a_ = '-' + str((4294967295 - int(data_sp[2], 16))) + ','
        print('A = ', a_)
        safe_line(a_)

    else:
        a = str(int(data_sp[2], 16)) + ','
        print('A = ', a)
        safe_line(a)

    for el in range(3, len(data_sp)-2):
        safe_line(str(int(data_sp[el], 16)) + ',')
    safe_line(str(data_sp[len(data_sp)-2]) + ',' + str(data_sp[len(data_sp)-1]) + ',')
    safe_line(str(now.time()) + ',' + str(now.date()))
    safe_line('\n')


def file_init(com_port):
    version_read = True
    while version_read:
        com_port.write(b'\x1A\x4F')
        time.sleep(1)
        bytes_to_read = com_port.inWaiting()
        if bytes_to_read == 73:
            data = com_port.read(bytes_to_read)
            data_sp = data.decode("utf-8")
            data_sp = data_sp.split(',')
            version = 'Firmware version:' + str(data_sp[0]) + '\n'
            with open("aku_log.txt", 'a', encoding='utf-8') as log_data:
                log_data.write(version)
                log_data.write('Voltage[mV], Current[mA], Temperature[C*100], Section1[mv], Section2[mV], Section3[mV],'
                               ' Section4[mV], Balancer, Alarm, Time, Date\n')
            version_read = False
        else:
            print("Didn't receive a good frame. ")


def safe_line(data):
    with open("aku_log.txt", 'a', encoding='utf-8') as log_data:
        log_data.write(data)


def measure(ser_port):
    ser_port.write(b'\x1A\x4F')
    time.sleep(1)
    bytes_to_read = ser_port.inWaiting()

    if bytes_to_read == 73:
        data = ser_port.read(bytes_to_read)
        to_dec(data)
    else:
        safe_line('**************************************')
        safe_line('\n')


def main():
    print('BMS log.')
    ser_port = serial_init('COM13')
    check_serial_open(ser_port)
    file_init(ser_port)
    now = datetime.datetime.now()
    while True:
        now_temp = datetime.datetime.now()
        if abs(now.second - now_temp.second) >= 2:
            now = datetime.datetime.now()
            measure(ser_port)


if __name__ == '__main__':
    main()


