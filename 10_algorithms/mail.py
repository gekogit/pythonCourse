

def check_mail(mail_l, user_mail):
    for el in mail_l:
        if el == user_mail:
            return True
    return False


def main():
    mail_list = ['tom@wp.pl', 'pit@google.com', 'a@wp.pl', 'c@wp.pl', 'aa@wp.pl']
    user_mail = input("Type mail for search:")
    result = check_mail(mail_list, user_mail)
    print('Email is on the list: ', result)


if __name__ == '__main__':
    main()
