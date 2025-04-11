from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from db.model import PostDB
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class PostRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_all(self, posts: list[PostDB]):
        """Сохраняем в сессию"""
        try: 
            print(f"Сохраняем {len(posts)} постов.")
            stmt = insert(PostDB).values([{
                'id': post.id,
                'user_id': post.user_id,
                'title': post.title,
                'body': post.body
            } for post in posts])
            await self.session.execute(stmt)
            await self.session.commit()
            print("Данные сохранены в базе данных.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

