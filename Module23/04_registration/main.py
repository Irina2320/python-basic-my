def data_validation(data):
    data = data.split()
    if len(data) != 3:
        raise IndexError
    elif not data[0].isalpha():
        raise NameError
    elif '@' not in data[1] or '.' not in data[1]:
        raise SyntaxError
    elif not 10 <= int(data[2]) <= 99:
        raise ValueError
    else:
        with open('registrations_good.log', 'a') as registrations_good:
            registrations_good.write(' '.join(data) + '\n')


with open('registrations.txt', 'r') as registrations:
    for users_data in registrations:
        if users_data[-1] == '\n':
            users_data = users_data[:-1]
        try:
            data_validation(users_data)

        except IndexError:
            with open('registrations_bad.log', 'a') as registrations_bad:
                message = users_data + '\t\tНЕ присутствуют все три поля\n'
                registrations_bad.write(message)

        except NameError:
            with open('registrations_bad.log', 'a') as registrations_bad:
                message = users_data + '\t\tПоле «Имя» содержит НЕ только буквы\n'
                registrations_bad.write(message)

        except SyntaxError:
            with open('registrations_bad.log', 'a') as registrations_bad:
                message = users_data + '\t\tПоле «Имейл» НЕ содержит @ и . (точку)\n'
                registrations_bad.write(message)

        except ValueError:
            with open('registrations_bad.log', 'a') as registrations_bad:
                message = users_data + '\t\tПоле «Возраст» НЕ является числом от 10 до 99\n'
                registrations_bad.write(message)
