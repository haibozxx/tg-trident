import typing
from sqlalchemy import create_engine
from alchemysession import AlchemySessionContainer
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:123456@192.168.5.17:10004/telegram_session?charset=utf8mb4")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

container = AlchemySessionContainer(engine=engine)

