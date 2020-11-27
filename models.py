# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from contextlib import contextmanager

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@192.168.205.100:3306/flask?charset=utf8')

Base.metadata.create_all(engine)  # 创建表结构
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 自动创建并释放
@contextmanager
def auto_commit():
    session = DBSession()
    try:
        yield session
        session.commit()

    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# 定义User对象:
class User(Base, ):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    pwd = Column(String(20))

    @staticmethod
    def add(name, pwd):
        with auto_commit() as se:
            new_user = User(name=name, pwd=pwd)
            # 添加到session:
            se.add(new_user)

    @staticmethod
    def compare(name, pwd):
        with auto_commit() as se:
            com_user = se.query(User).filter(User.name == name, User.pwd == pwd).first()
            if com_user:
                return True
            else:
                return False

