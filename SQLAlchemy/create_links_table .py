# -*- coding: utf-8 -*-
import json

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Posts(Base):
    # create a table named posts
    __tablename__ = 'links'

    # define Columns in the new table
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    link = Column(String(180, collation='utf8_bin'), unique=True)

    def __init__(self, link):
        self.link = link

    def __repr__(self):
        return "Posts('%s')" % (self.link)


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
    with open('links.json') as links_file:
        data = json.load(links_file)

    # add counters for loop
    i = 0
    j = 0
    while True:
        try:
            print data[i]
            i += 1
        except IndexError:
            print "end of keys"
            break
    """
    row = session.query(Posts).filter(Posts.link == data[i]["link"]).all()
    if row:
        print "this row of data exists"
    else:
        session.add(Posts(**data[i]))
        session.commit()
    """
    print "\nAll SQL commands executed"
