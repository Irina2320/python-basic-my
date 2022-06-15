incorrect_sym = list('@№$%^&*()')
end_file = ['.txt', '.docx']

while True:
    file_name = input('\nНазвание файла: ')
    for i in incorrect_sym:
        if file_name.startswith(i):
            print('Ошибка: название начинается на один из специальных символов:', i)
            break
    else:
        if file_name.endswith('.txt') or file_name.endswith('.docx'):
            print('Файл назван верно.')
        else:
            print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')

# Зациклил для более удобной проверки)