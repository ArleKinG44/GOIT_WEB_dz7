from sqlalchemy import func, desc
from models import Student, Grade, Group, Subject, Teacher, Session

def select_1():
    session = Session()
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                    .select_from(Grade) \
                    .join(Student) \
                    .group_by(Student.id) \
                    .order_by(desc('avg_grade')) \
                    .limit(5) \
                    .all()
    session.close()
    return result

def select_2(subject_name):
    session = Session()
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                    .select_from(Grade) \
                    .join(Student) \
                    .join(Subject) \
                    .filter(Subject.name == subject_name) \
                    .group_by(Student.id) \
                    .order_by(desc('avg_grade')) \
                    .first()
    session.close()
    return result

def select_3(subject_name):
    session = Session()
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                    .select_from(Grade) \
                    .join(Student) \
                    .join(Group) \
                    .join(Subject) \
                    .filter(Subject.name == subject_name) \
                    .group_by(Group.id) \
                    .all()
    session.close()
    return result

def select_4():
    session = Session()
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                    .scalar()
    session.close()
    return result

def select_5(teacher_name):
    session = Session()
    result = session.query(Subject.name) \
                    .filter(Subject.teacher.has(name=teacher_name)) \
                    .all()
    session.close()
    return result

def select_6(group_name):
    session = Session()
    result = session.query(Student.fullname) \
                    .join(Group) \
                    .filter(Group.name == group_name) \
                    .all()
    session.close()
    return result

def select_7(group_name, subject_name):
    session = Session()
    result = session.query(Student.fullname, Grade.grade) \
                    .join(Group) \
                    .join(Grade) \
                    .join(Subject) \
                    .filter(Group.name == group_name, Subject.name == subject_name) \
                    .all()
    session.close()
    return result

def select_8(teacher_name):
    session = Session()
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                    .join(Subject) \
                    .filter(Subject.teacher.has(name=teacher_name)) \
                    .scalar()
    session.close()
    return result

def select_9(student_name):
    session = Session()
    result = session.query(Subject.name) \
                    .join(Grade) \
                    .join(Student) \
                    .filter(Student.fullname == student_name) \
                    .all()
    session.close()
    return result

def select_10(student_name, teacher_name):
    session = Session()
    result = session.query(Subject.name) \
                    .join(Grade) \
                    .join(Student) \
                    .join(Teacher) \
                    .filter(Student.fullname == student_name, Teacher.name == teacher_name) \
                    .all()
    session.close()
    return result
