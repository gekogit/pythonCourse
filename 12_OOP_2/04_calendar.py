"""
4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc podawać aktualną datę oraz wyświetlać ile
dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał datę, godzinę oraz widok
 dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.
"""
import calendar
import datetime


class Calendar:

    def get_date(self):
        current_date = datetime.datetime.now().date()
        return current_date

    def get_month(self):
        return datetime.datetime.now().month

    def get_year(self):
        return datetime.datetime.now().year

    def get_day_name(self):
        d = calendar.weekday(self.get_year(), self.get_month(), self.get_day())
        print(calendar.day_name[d])

    def get_day(self):
        return datetime.datetime.now().day

    def show_month(self):
        print('\nWhole month view:')
        s = calendar.TextCalendar(calendar.FRIDAY)
        c_str = s.formatmonth(self.get_year(), self.get_month())
        print(c_str)


class Watch:

    def get_time(self):
        system_time = datetime.datetime.now()
        print(system_time.strftime("Local time; HH-MM-SS  %H:%M:%S"))


class CalendarWatch(Calendar, Watch):

    def today_is(self):
        print('\nToday is:')
        print(f'{super().get_date()}')
        super().get_day_name()

    def current_month(self):
        super().show_month()


def main():

    earth_time = CalendarWatch()
    earth_time.today_is()
    earth_time.get_time()
    earth_time.current_month()


if __name__ == '__main__':
    main()
