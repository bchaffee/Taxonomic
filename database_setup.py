from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Creates class for each user


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

# Creates class for each Kingdom


class Kingdom(Base):
    __tablename__ = 'kingdoms'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

# Creates class for each Kingdom


class Phyla(Base):
    __tablename__ = 'phylas'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    meaning = Column(String(250))
    characteristic = Column(String(250))
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    kingdom = relationship(Kingdom)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'meaning': self.meaning,
            'id': self.id,
            'characteristic': self.characteristic,
        }


engine = create_engine('sqlite:///kingdomphyla.db')


Base.metadata.create_all(engine)
