import typing
from alchemysession import AlchemySessionContainer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


tg_session_engine = create_engine("mysql+pymysql://root:123456@192.168.5.17:10004/telegram_session?charset=utf8mb4")
container = AlchemySessionContainer(engine=tg_session_engine)

engine = create_engine("mysql+pymysql://root:123456@192.168.5.17:10004/telegram_control?charset=utf8mb4", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, create_engine

    base = declarative_base()
    sess = SessionLocal()

    # aufoflush = False 时，add没有提交sql，下面的操作会主键冲突

    class Session(base):
           __tablename__ = '{prefix}sessions'.format(prefix="")
           session_id = Column(String(255), primary_key=True)
           dc_id = Column(Integer, primary_key=True)


    sess.query(Session).filter(Session.session_id == "123").delete()
    session = Session(session_id="123", dc_id=2)
    sess.add(session)

    sess.query(Session).filter(Session.session_id == "123").delete()
    session = Session(session_id="123", dc_id=2)
    sess.add(session)

    sess.commit()
