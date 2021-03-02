#coding:utf-8
from sqlalchemy import Table,Column,Integer,String,TIMESTAMP,create_engine,func,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker,relationship
from sqlalchemy.schema import ForeignKey
import pymysql

#设置一系列的基本参数
Base = declarative_base()
DB_CONNECT_STR = "mysql+pymysql://root:@localhost:3306/job_crawler?charset=utf8"
engine = create_engine(DB_CONNECT_STR,encoding="utf8",convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

#表,懒惰使我选择了String
class Posts(Base):
    __tablename__ = 'posts'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    code = Column(String(255),nullable=False,primary_key=True)
    name = Column(String(255),nullable=False)
    
    agency = Column(String(255),nullable=False)
    agency_type = Column(String(255),nullable=False)
    agency_level = Column(String(255),nullable=False)
    job_type = Column(String(255),nullable=False)
    job_position = Column(String(255),nullable=False)
    major = Column(String(255),nullable=False)
    education = Column(String(255),nullable=False)
    degree = Column(String(255),nullable=False)
    age = Column(String(255),nullable=False)
    sex = Column(String(255),nullable=False)
    experience = Column(String(255),nullable=False)
    subject = Column(String(255),nullable=False)
    others = Column(String(255),nullable=False)
    category_type = Column(String(255),nullable=False)
    ps = Column(String(255),nullable=False)
    phone = Column(String(255),nullable=False)

    plan = Column(String(255),nullable=True)
    submitted_num = Column(String(255),nullable=True)
    qualified_num = Column(String(255),nullable=True)
    paid_num = Column(String(255),nullable=True)



#创建全部表的主函数
def main():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
