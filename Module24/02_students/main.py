import random

names = ('Соколиный Глаз', 'Человек Муравей', 'Железный Человек', 'Капитан Америка', 'Черная Вдова',
         'Невероятный Халк', 'Красная Ведьма', 'Черная Пантера', 'Зимний Солдат', 'Николас J Фьюри')
students = []
students_academic_performance = dict()


class Student:

    def __init__(self, name, group, academic_performance):
        self.name = name
        self.group = group
        self.academic_performance = academic_performance

    def grade_point_average(self):
        return sum(self.academic_performance) / len(self.academic_performance)

    def print_data(self):
        print(f'Студент: {self.name} \nГруппа: {self.group} \nОценки: {self.academic_performance}')


def group_generator():
    print('Учитывая рандом решил показать всех студентов:')
    for student_name in names:
        student_group = random.randint(1001, 1010)
        student_marks = [random.randint(1, 10) for _ in range(5)]
        students.append(Student(student_name, student_group, student_marks))
        print(f'Студент: {student_name} \nГруппа: {student_group} \nОценки: {student_marks}\n')
    else:
        print('- * ' * 10)


def students_sorting():
    for student in students:
        student_GPA = student.grade_point_average()
        if student_GPA not in students_academic_performance:
            students_academic_performance[student_GPA] = {student}
        else:
            students_academic_performance[student_GPA].add(student)

    for GPA in sorted(students_academic_performance):
        for student in students_academic_performance[GPA]:
            print('\nСредний балл:', GPA)
            student.print_data()


group_generator()
students_sorting()


