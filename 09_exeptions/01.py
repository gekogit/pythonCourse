"""
 Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
  W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
"""
my_list = [13, 'zoo', 3.45, 0, True, (1, 2), {"k": 2}, [32, 43]]

print('Divide by 10 elements: ', my_list)

for el in my_list:
    print(el)
    try:
        result = el / 10
    except Exception as s:
        print(s.__class__)


