# database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select

Base = declarative_base()

DATABASE_URL = "sqlite+aiosqlite:///./test.db" 

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(engine, class_= AsyncSession, expire_on_commit=False)


class PostDB(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    title = Column(String)
    body = Column(String)


async def init_db():
    """Загружаем таблицы"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы созданы")


class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_all(self, posts: list[PostDB]):
        """Сохраняем все посты в базу данных"""
        try:
            
            self.session.add_all(posts) 
            await self.session.commit() 
          
        except Exception as e:
            await self.session.rollback() 
            print(f"Ошибка при сохранении данных: {e}")
