from datetime import date, datetime
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


def create_row(_task, _deadline, session=_session):
    new_row = Task(task=_task, deadline=_deadline)
    session.add(new_row)
    session.commit()


def add_task():
    task = input('Enter task\n')
    deadline = input('Enter deadline\n')
    try:
        datetime.strptime(deadline, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    create_row(task, deadline)


def view_today_tasks():
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
2) Week's tasks
3) All tasks
4) Add task
0) Exit
"""


def view_week_tasks():
    pass


while True:
    print(_greeting)
    input_num = int(input())

    if input_num == 0:
        break
    elif input_num == 1:
        view_today_tasks()
    elif input_num == 2:
        view_week_tasks()
    elif input_num == 3:
        view_all_tasks()
    elif input_num == 4:
        add_task()
    else:
        quit(-1)

print('Bye!')
