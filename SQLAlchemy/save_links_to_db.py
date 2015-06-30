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
    __tablename__ = 'article_links'

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
    # depth is set to 12 in settings.py
    for i in range(0, 13):
        # index counter
        j = 0
        # can not sure how many items, so keep loop running until IndexError occurs
        while True:
            try:
                # combine domain to one complete web-link
                dic = {"link": "https://www.ptt.cc" + data[i].values()[0][j]}
                # check this web-link exists in database or not
                row = session.query(Posts).filter(Posts.link == dic["link"]).all()
                if row:
                    print "this row of data exists"
                else:
                    # if not exists, then save
                    session.add(Posts(**dic))
                    session.commit()
                j += 1
            except IndexError:
                print "end of values"
                break

    print "\nAll SQL commands executed"
