# -*- coding: utf-8 -*-
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
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    author = Column(String(150, collation='utf8_unicode_ci'))
    board = Column(String(150, collation='utf8_unicode_ci'))
    title = Column(String(150, collation='utf8_unicode_ci'))
    link = Column(String(180, collation='utf8_bin'), unique=True)
    content = Column(Text(collation='utf8_unicode_ci'))
    create_time = Column(DateTime)
    push_count = Column(Integer)
    hiss_count = Column(Integer)
    comment_count = Column(Integer)
    author_ip = Column(String(30, collation='utf8_unicode_ci'))
    location = Column(String(50, collation='utf8_bin'), nullable=True)

    def __init__(self, author, board, title, link, content, create_time,\
                 push_count, hiss_count, comment_count, author_ip, location):
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
        self.location = location

    def __repr__(self):
        return "Posts('%s', %s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
               % (self.author, self.board, self.title, self.link, self.content,\
                  self.create_time, self.push_count, self.hiss_count, \
                  self.comment_count, self.author_ip, self.location)


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

    # create a for loop to create 100 sets of data
    for i in range(1, 151):
        # create a dict, this is one set of data
        # source is post_link.id, needs create value at first
        # create_time can not use timestamp directly, it needs to be converted
        dic = {"author": "John Doe -" + str(i), \
                   "board_id": 5566, "board": "PTT_Gossiping", \
                   "title": "title -" + str(i), \
                   "link": "https://www.ptt.cc/bbs/Gossiping/" + str(i) + ".html", \
                   "description": "this is a test -" + str(i), \
                   "thumbnail": "avatar-" + str(i) + ".png", "content": "no more", \
                   "create_time": "2015-06-16T10:33:27", "likeCount": i, \
                   "shareCount": i, "commentCount": i, "dislikeCount": i, \
                   "viewCount": i, "location": "Taipei"}

        row = session.query(Posts).filter(Posts.link == dic["link"]).all()
        if row:
            print "this row of data exists"
            continue
        else:
            session.add(Posts(**dic))
            session.commit()

        print "\nAll SQL commands executed"
