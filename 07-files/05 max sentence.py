"""
Wykorzystaj plik zawierający fragment Pana Tadeusza. Znajdź najdłuższe słowo występujące w zadanym fragmencie
"""


def load_content():
    with open('pan_tadeusz.txt', encoding='utf-8') as f:
        text_from_file = f.read()
        return text_from_file


def clean_txt(text):
    sig = '.,()!'
    for i in sig:
        text = text.replace(i, '')
        return text


def find_max(text):
    max_len = 0
    text = text.split()
    for index in range(len(text)):
        if len(text[index]) > max_len:
            max_len = index
    return text[max_len]


#main
content = load_content()
content = clean_txt(content)
print("\nMax word in the file:", find_max(content))
