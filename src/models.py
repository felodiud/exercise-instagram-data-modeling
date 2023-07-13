import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

Base = declarative_base()
assosiaton_table = Table(
    'follower', 
    Base.metadata,
    Column('user_from_id', ForeignKey('user.id')),
    Column('user_to_id', ForeignKey('user.id')),
    )

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False, unique = True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), nullable = False, unique = True)
    post = relationship('Post')
    comment = relationship('Comment')
    #follower = relationship('Follower')
    assosiaton_table = relationship('Child', secondary = assosiaton_table)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer,ForeignKey('user.id'))
    comment = relationship('Comment')
    media = relationship('Media')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(400))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class MyEnum(enum.Enum):
    mp3 = 'mp3'
    mp4 = 'mp4'
    jpeg = 'jpeg'

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Column(Enum(MyEnum))
    url = Column(String(20000))
    post_id = Column(Integer, ForeignKey('post.id'))

# class Follower(Base):
#     __tablename__ = 'follower'
#     id = Column(Integer, primary_key = True)
#     user_from_id = Column(Integer, ForeignKey('user.id'))
#     user_to_id = Column(Integer, ForeignKey('user.id'))










try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

