# -*- coding: utf-8 -*-
import json
import time

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Posts(Base):
    # create a table named posts
    __tablename__ = 'articles'

    # define Columns in the new table
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(150, collation='utf8_unicode_ci'), nullable=True)
    board = Column(String(150, collation='utf8_unicode_ci'), nullable=True)
    title = Column(String(150, collation='utf8_unicode_ci'), nullable=True)
    link = Column(String(180, collation='utf8_bin'), unique=True, nullable=True)
    content = Column(Text(collation='utf8_unicode_ci'), nullable=True)
    create_time = Column(DateTime, nullable=True)
    push_count = Column(Integer, nullable=True)
    hiss_count = Column(Integer, nullable=True)
    comment_count = Column(Integer, nullable=True)
    author_ip = Column(String(30, collation='utf8_unicode_ci'), nullable=True)

    def __init__(self, author, board, title, link, content, create_time,\
                 push_count, hiss_count, comment_count, author_ip):
        self.author = author
        self.board = board
        self.title = title
        self.link = link
        self.content = content
        self.create_time = create_time
        self.push_count = push_count
        self.hiss_count = hiss_count
        self.comment_count = comment_count
        self.author_ip = author_ip

    def __repr__(self):
        return "Posts('%s', %s','%s','%s','%s','%s', '%s','%s','%s','%s','%s','%s','%s')" \
               % (self.author, self.board, self.title, self.title, \
                  self.content,self.create_time, self.push_count, \
                  self.hiss_count, self.comment_count, self.author_ip)


if __name__ == '__main__':
    # use below command to install driver, do "not" install deb on MySQL site
    # pip install mysql-connector-python --allow-external mysql-connector-python
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/ptt_tech_job' \
                           , echo=True)

    # create new table if it doesn't exist
    Base.metadata.create_all(engine)

    # Insert needs session
    Session = sessionmaker(bind=engine)
    session = Session()
    session.autoflush = False

    # read json file to list
    with open('articles.json') as articles_file:
        data = json.load(articles_file)

    # add counters for loop
    i = 0
    while True:
        print data
        time.sleep(2)

    print "\nAll SQL commands executed"
