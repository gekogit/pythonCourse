filename = 'pan_tadeusz.txt'

with open(filename, 'r') as f:
    content = f.read()
    print(content)

with open(filename) as my_f:
    my_list = my_f.readlines()
for nr, value in enumerate(my_list):
    print(f'Linia {nr} --->{value}')

my_list =['Ja', 'Ty']
with open('save.txt', 'w') as fsave:
    fsave.write('Ona')
    fsave.write('\n'.join(my_list))

with open('save.txt') as fsave:
    print(fsave.readlines())

