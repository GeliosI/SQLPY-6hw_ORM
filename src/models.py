import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

    def __str__(self):
        return f"<{type(self).__name__}(id={self.id} name={self.name})>"


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f"<{type(self).__name__}(id={self.id} name={self.title} id_publisher={self.id_publisher})>"


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

    def __str__(self):
        return f"<{type(self).__name__}(id={self.id} name={self.name})>"


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f"<{type(self).__name__}(id={self.id} id_book={self.id_book} id_shop={self.id_shop} count={self.count})>"


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.String(length=40), nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f"<{type(self).__name__}(id={self.id} price={self.price} date_sale={self.date_sale} id_stock={self.id_stock} count={self.count})>"


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)