"""
3▹ Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
 Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do
  kolejki (put), wyjęcie elementu z kolejki (get).
Utwórz kilka obiektów klasy Queue z różnymi parametrami.
"""


class Queue():
    def __init__(self, elements):
        self.elements = elements

    def print_queue(self):
        print("List: ", self.elements)

    def is_empty(self):
        return True if len(self.elements) == 0 else False

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.pop(0)


def main():
    my_q = Queue([12, 32, 43, 54])
    my_q.print_queue()
    my_q.put('2')
    my_q.print_queue()
    my_q.get()
    my_q.print_queue()
    print('Is empty?: ', my_q.is_empty())


if __name__ == '__main__':
    main()




