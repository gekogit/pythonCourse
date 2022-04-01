"""
6▹ Utwórz klasę Pracownik.
Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać podatek
 o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka
zdrowotna wynosi 0%.
Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy.
Np. Adam Kowalski Love Python Company
email -> smkwlsk@lovepythoncompany.com
"""


class Employee:

    def __init__(self, position, salary, name, last_name, seniority):
        self.position = position
        self.salary = salary
        self.name = name
        self.last_name = last_name
        self.seniority = seniority

    def email(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        adr = ''
        low_name = self.name.lower()
        low_last_name = self.last_name.lower()
        for c in low_name:
            if consonants.find(c) != -1:
                adr += c
        adr += '.'
        for c in low_last_name:
            if consonants.find(c) != -1:
                adr += c
        adr += '@' + str.lower(self.company[:3]) + '.com'
        return '{}'.format(adr)

    def tax(self):
        return self.actual_tax_rate * self.salary / 100

    def is_student(self):
        self.student_status = True

    def is_not_student(self):
        self.student_status = False

    def med(self):
        return 0 if self.student_status else self.actual_med_rate * self.salary / 100

    def annual(self):
        if self.seniority > 1:
            self.salary += 5 * self.salary/100
        elif self.seniority > 3:
            self.salary += 10 * self.salary/100
        else:
            self.salary += 1 * self.salary / 100

    company = 'ABC in co'
    student_status = False
    actual_tax_rate = 17
    actual_med_rate = 5


def print_company_team(team):
    print('\nCompany team:')
    for el in team:
        print(f'{el.name} {el.last_name} best as {el.position} with {el.seniority} years experience.')
        print(f'Salary: {el.salary}, tax {el.tax()}, med {el.med()}, student? {el.student_status} ')


def main():
    team_abc = [Employee('driver', 5000, 'Tadeusz', 'Rinc', 30), Employee('Killer', 10000, 'Leon', 'Professional', 7)]
    Employee.is_student(team_abc[0])
    print_company_team(team_abc)


if __name__ == '__main__':
    main()
