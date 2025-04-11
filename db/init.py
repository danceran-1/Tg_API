from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo = True)
async_session = async_sessionmaker(engine,expire_on_commit=False)


async def init_db():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        print("Таблицы созданы")