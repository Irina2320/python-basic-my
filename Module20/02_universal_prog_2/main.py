def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return True


def crypto(interable):
    return [obj for index, obj in enumerate(interable) if is_prime(index)]


print(crypto('О Дивный Новый мир!'))

# Как я понял, условие задачи не требует инпута, потому делал без него
