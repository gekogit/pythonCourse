"""
9▹ Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www.
Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
https://
http://
www
bez www
Może się kończyć za pomocą:
.pl
.com
Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.
Nie masz dość? Swietnie! Przepisz to zadanie za pomocą wyrażeń regularnych (RegEx)
"""
#import antigravity
import webbrowser
from urllib.error import URLError


def is_start_ok(url):
    return url.startswith('https://' or url.startswith('http://'))


def is_end_ok(url):
    return url.endswith('.pl' or url.endswith('.com'))


def is_start_www(url):
    return url.startswith('www.')


def get_url():
    url = input('Give URL:..')
    if is_start_ok(url) and is_end_ok(url):
        return url
    elif is_start_www(url):
        return 'http://' + url
    else:
        raise URLError('URL looks wrong.')


def main():
    while True:
        try:
            url = get_url()
            break
        except URLError as e_message:
            print(e_message)

    webbrowser.open(f'{url}')


if __name__ == '__main__':
    main()
