from student import *
import argparse
from logger import logger


def parser_func():
    parser = argparse.ArgumentParser(description="Принимаем строку с ФИО студента")
    parser.add_argument('-n', type=str)
    parser.add_argument('-pn', type=str)
    parser.add_argument('-ln', type=str)
    args = parser.parse_args()
    logger.info(f'Студент добавлен через терминал.')
    return Student(args.n, args.pn, args.ln)


if __name__ == '__main__':
    student_3 = parser_func()
    print(student_3)