from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from base import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    salt = Column(String)
    email = Column(String)


class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True)
    attempt_status = Column(String)
    timestamp = Column(DateTime)
    client_id = Column(Integer, ForeignKey("clients.id"))
    clientrel = relationship("Client", backref="login_attempts")


class BlockedUser(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True)
    block_start = Column(DateTime)
    block_end = Column(DateTime)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", backref="blocked_users")


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", backref="tokens")

engine = create_engine("sqlite:///bank.db")
# will create all tables
Base.metadata.create_all(engine)
