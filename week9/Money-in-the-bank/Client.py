from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    balance = Column(Integer, default=0)
    message = Column(String)
    email = Column(String)

    def __init__(self, ):
        self.username = username
        self.balance = balance
        self.id = id
        self.message = message
        self.email = email

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message

    def get_email(self):
        return self.__email

engine = create_engine("sqlite:///bank.db")
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new client to the database via the session object")
client1 = Client(username="Rado")
session.add(client1)
session.commit()
