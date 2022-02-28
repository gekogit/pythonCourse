"""
Przekopiuj zawartość import this do zmiennej.
import this
Policz liczbę wystąpień słowa better.
Usuń z tekstu symbol gwiazdki
Zamień jedno wystąpienie explain na understand
Usuń spacje i połącz wszystkie słowa myślnikiem
Podziel tekst na osobne zdania za pomocą kropki
"""
thisPython = "The Zen of Python, by Tim Peters\n\
Beautiful is better than ugly.\n\
Explicit is better than implicit.\n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!"

import this

print(f'\nWord "better" appeared {thisPython.count("better")} times.')
print(f'\n"*" deleted from the text:\n {thisPython.replace("*","")}')
print(f'\nReplaced one explain for understand :\n {thisPython.replace("explain","understand",1)}')
print(f'\n Removed " " and joined with "-"{thisPython.replace(" ","-")}')
thisPython = thisPython.replace("\n", "")
print(f'\nSplit by coma {thisPython.split(".")}')
