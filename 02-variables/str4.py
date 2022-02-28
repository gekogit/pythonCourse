"""
Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book
"""
print("\nYo Man L:) Write info about your book.")
title = input("Title:..")
author = input("Author(lastname):..")
pages = input("Number of pages:..")

#print(f'Title and name without digits? {not title.isnumeric() and not author.isnumeric()}')
print(f'Title and name without digits? { title.isalpha() and  author.isalpha()}')
print(f'Pages are numeric? {pages.isdigit()}')
title = title.title()
author = author.title()
print(f'Cap L title and author: {title}. {author}.')
book = title + " " + author + "."
print("Title + author: ", book)
print(f'Length of book: {len(book)}')
