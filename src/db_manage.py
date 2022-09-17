import json

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale


class DbManage:
    def __init__(self, dbms_name, login, password, host, port, db_name):
        DSN = f'{dbms_name}://{login}:{password}@{host}:{port}/{db_name}'
        engine = sq.create_engine(DSN)
        create_tables(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()        

    def populate_database_with_data_from_file(self, file_path):
        """Populates the database with data from a json-file

        Keyword Arguments:
            - file_path -- path to json

        """

        with open(file_path, 'r') as fd:
            data = json.load(fd)

        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            current_model = model(id=record.get('pk'), **record.get('fields'))
            self.session.add(current_model)
        self.session.commit()

    def find_store_by_publisher_name(self, publisher_name):
        """Finds stores that sell the publisher by his name

        Keyword Arguments:
            - publisher_name -- publisher name

        """

        print(f'Publisher with name {publisher_name} featured in the stores ', end='')
        for c in self.session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all():
            print(c.name, end=' ')
        print()

    def find_store_by_publisher_id(self, publisher_id):
        """Finds stores that sell the publisher by his id

        Keyword Arguments:
            - publisher_id -- publisher id

        """

        print(f'Publisher with id {publisher_id} featured in the stores ', end='')
        for c in self.session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == publisher_id).all():
            print(c.name, end=' ')
        print()

    def __del__(self):
        self.session.close()          