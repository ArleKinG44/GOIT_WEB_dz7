from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime
import random

fake = Faker('uk_UA')

engine = create_engine('postgresql://postgres:akg@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()

def generate_random_data():
    groups = ['Група 1', 'Група 2', 'Група 3']
    for group_name in groups:
        group = Group(name=group_name)
        session.add(group)

    for _ in range(5):
        teacher = Teacher(name=fake.name())
        session.add(teacher)

    subjects = ['Математика', 'Фізика', 'Хімія', 'Історія', 'Література', 'Інформатика', 'Біологія', 'Географія']
    for subject_name in subjects:
        teacher_id = random.randint(1, 5)
        subject = Subject(name=subject_name, teacher_id=teacher_id)
        session.add(subject)

    for _ in range(40):
        student = Student(name=fake.name(), group_id=random.randint(1, 3))
        session.add(student)
        for subject_id in range(1, 9):
            grade = random.randint(1, 100)
            date_received = fake.date_between(start_date='-1y', end_date='today')
            grade = Grade(student_id=student.id, subject_id=subject_id, grade=grade, date_received=date_received)
            session.add(grade)

    session.commit()

if __name__ == "__main__":
    generate_random_data()
