import os

import file_sevice as safety_service

print('Write One Two Three to test.txt file. ')
safety_service.write_file('test.txt', 'One Two Three')
print('Write second time One Two Three to test.txt file. ')
safety_service.write_file('test.txt', 'One Two Three')

print('Read from test.txt file. ')
txt = safety_service.read_file('test.txt')
print(f'Content: {txt}')
os.remove('test.txt')
print('Read from ghost file. ')
txt = safety_service.read_file('test.txt')