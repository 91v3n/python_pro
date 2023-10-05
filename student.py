import csv
from logger import logger
from user_exception import *



class Validator:
    def __init__(self, name_full: str = None):
        self.name_full = name_full

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            logger.error(f'Значение - ({value}) должно содержать только буквы')
            raise UserTypeStrError(value)
        if not value.istitle():
            logger.error(f'Значение - ({value}) должно начинаться с заглавной буквы')
            raise UserTypeTextError(value)

class Student:
    name = Validator()
    lastname = Validator()
    patronymic = Validator()
    grade_res = 'оценки'
    test_res = 'результаты тестирования'

    def __init__(self, name,  patronymic, lastname,):
        self.name = name
        self.lastname = lastname
        self.patronymic = patronymic
        self.__study_journal = dict()
        with open('lessons.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter="\n")
            for row in file_reader:
                self.__study_journal[str(*row)] = {self.grade_res: [], self.test_res: []}
        logger.info(f'Студент {self} добавлен.')
    def rate_student(self, subject: str, evaluate: int):
        if   self.__study_journal.get(subject) is None:
            logger.error (f'Предмет не изучается студентом {self}')
            raise UserLessonsError(subject)
        if not 1 < evaluate < 6:
            logger.error(f'Оценка студента {self} не входит в границы.')
            raise UserEstimateError(evaluate, 2, 5)
        self.__study_journal[subject][self.grade_res].append(evaluate)

    def test_score(self, subject: str, score: int):
        if self.__study_journal.get(subject) is None:
            logger.error(f'Предмет не изучается студентом {self}')
            raise UserLessonsError(subject)
        if not -1 < score < 101:
            logger.error(f'Оценка студента {self} не входит в границы.')
            raise UserEstimateError(score, 0, 100)
        self.__study_journal[subject][self.test_res].append(score)

    def average_score(self, subject, what_result):
        if self.__study_journal[subject][what_result]:
            result = sum(self.__study_journal[subject][what_result]) \
                     / len(self.__study_journal[subject][what_result])
            logger.info(f'Добавдены средние {what_result} у студента {self} по предмету "{subject}": {result} балла.')
            return f'Средние {what_result} по предмету "{subject}": {result} балла.'
        logger.debug(f'У студента {self} cредние {what_result} по предмету "{subject}": оценки отсутствуют.')
        return f'Средние {what_result} по предмету "{subject}": оценки отсутствуют.'

    def overall_point_average(self):
        summ = 0
        count = 0
        for i in self.__study_journal:
            summ += sum(self.__study_journal[i][self.grade_res])
            count += len(self.__study_journal[i][self.grade_res])
        logger.info(f'Средний балл студента {self}: {round(summ / count, 2)}.')
        return round(summ / count, 2)

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.lastname}'
    def __repr__(self):
        return f'Student(name="{self.name}", patronymic="{self.patronymic}", lastname="{self.lastname}")'

    @property
    def study_journal(self):
        return self.__study_journal


if __name__ == '__main__':
    grade = 'оценки'
    test = 'результаты тестирования'
    student_1 = Student('Иван', 'Петрович', 'Сидоров')
    student_2 = Student('Анна', 'Ивановна', 'Петрова')
    logger.info(f'Студент {student_1} добавлен.')
    logger.info(f'Студент {student_2} добавлен.')
    print(student_1)
    student_3 = Student('Максим', 'сергеевич', 'Сидоров')