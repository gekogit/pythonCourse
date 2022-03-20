def print_month(data_in):
    input_data = dict(data_in)
    for month, days in input_data.items():
        print(month)
        for i in days:
            print(i+1, end=' ')
            if i < 9:
                print(end=' ')
            if (i+1) % 7 == 0:
                print()
        print('\n')


data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]
print_month(data)
