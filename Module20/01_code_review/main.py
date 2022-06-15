students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def students_hobby(students):
    students_hobby_set = {hobby for students_dict in students.values()
                           for hobby in students_dict.get('interests')}

    surname_len = sum(len(surname) for students_dict in students.values()
                           for surname in students_dict.get('surname'))
    return students_hobby_set, surname_len


id_age = [(students_id, students_age) for students_id in students
          for key, students_age in students[students_id].items() if key == 'age']



print('Список пар "ID студента - Возраст":', id_age)
students_hobby_set, surname_len = students_hobby(students)
print('Полный список интересов всех студентов:', students_hobby_set, '\nОбщая длина всех фамилий студентов:', surname_len)
