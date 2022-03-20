"""
Wyświetl tylko 5 pierwszych linii.
"""
print()
with open('cytaty.txt',encoding='utf-8') as cyt_file:
    for x in range(5):
        print('Line ', x+1, ' : ', cyt_file.readline())
