from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=date.today())

    def __repr__(self):
        return self.task


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
_session = Session()


def create_row(_task, session=_session):
    new_row = Task(task=_task)
    session.add(new_row)
    session.commit()


def add_task():
    task = input('Enter task\n')
    create_row(task)


def view_tasks():
    rows = _session.query(Task).all()
    if rows is None or len(rows) < 1:
        print('Nothing to do!')
        return
    else:
        today_tasks = []
        for row in rows:
            if row.deadline == date.today():
                today_tasks.append(row.task)

        if len(today_tasks) > 0:
            print('Today:')
            task_num = 1
            for task in today_tasks:
                print(f'{task_num}. {task}')


_greeting = """
1) Today's tasks
2) Add task
0) Exit
"""

while True:
    print(_greeting)
    input_num = int(input())

    if input_num == 0:
        break
    elif input_num == 1:
        view_tasks()
    elif input_num == 2:
        add_task()
    else:
        quit(-1)

print('Bye!')
