import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:Dreddred0102-@localhost:5432/hw6"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    value_name = input('Поиск производится по имени "и" и номеру телефона "н": ')
    search = None
    if value_name == 'и':
        search = input('Введите имя издателя')
        q = session.query(Publisher).filter(Publisher.name == search)
        print(q)
        for s in q.all():
            print(s.id, s.name)
    elif value_name == 'н':
        search = int(input('Введите идентификатор издателя'))
        q = session.query(Publisher).filter(Publisher.id == search)
        print(q)
        for s in q.all():
            print(s.id, s.name)




