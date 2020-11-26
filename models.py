# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from contextlib import contextmanager
import pymysql

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(20))
    psw = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@192.168.205.100:3306/flask?charset=utf8')

Base.metadata.create_all(engine)  # 创建表结构
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# print(type(DBSession()))
# print(type(DBSession))
# print(type(sessionmaker))


# class DD():
#     pass
#
# dd=DD()
# print(type(DD))
# print(type(dd))

# class DBS(Session):
#     pass

# def add(self,name,psw):
#     pass

#     @contextmanager
#     def auto_commit(self):
#             print('准备')
#             yield
#             print('结束')
#             self().commit()
#             self().close()
#
#
# with DBS.auto_commit(DBSession):
#     session = DBSession()
#     # 创建新User对象:
#     new_user = User(name='169', psw='000')
#     # 添加到session:
#     session.add(new_user)
#     print('任务')


@contextmanager
def auto_commit():
    session = DBSession()
    try:
        yield session
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise e


def add(name, psw):
    # # 创建session对象:
    # session = DBSession()
    # # 创建新User对象:
    # new_user = User(name=name, psw=psw)
    # # 添加到session:
    # session.add(new_user)
    # # 提交即保存到数据库:
    # session.commit()
    # # 关闭session:
    # session.close()

    with auto_commit() as se:
        new_user = User(name=name, psw=psw)
        # 添加到session:
        se.add(new_user)
        # 提交即保存到数据库:


def compare(name, psw):
    # 创建session对象:
    session = DBSession()
    for n, p in session.query(User.name, User.psw):
        if name == n and psw == p:
            return True

    return False
    # for instance in session.query(User):
