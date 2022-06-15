def upper_mode():
    for i in password:
        if i.isupper():
            return True

def num_mode():
    tik = 0
    for i in password:
        if i.isdigit():
            tik += 1
        if tik == 3:
            return True

while True:
    password = list(input('Придумайте пароль: '))
    if len(password) > 7 and upper_mode() and num_mode():
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
