import aiohttp ,logging, asyncio, re
from utils.validation import PostList
from pydantic import ValidationError



API_URL = "https://jsonplaceholder.typicode.com/posts"

async def get_data_from_api():
    """ запрос к API JSON Placeholder"""

    try:
        async with aiohttp.ClientSession() as sesia:
            async with sesia.get(API_URL) as response:
               
                if response.status == 200:

                    data = await response.json()
                    data = convert_keys_to_snake_case(data)
                try:
                    data = PostList.model_validate(data)
                    return data
                except ValidationError as e:
                    logging.error(f"Ошибка валидации: {e}")
                    return None
                
                else:
                    logging.error("Ошибка подключения")
                    return None

    except:
        logging.error("Не возможно подкл к API")
        return None
    
def camel_to_snake(name) -> str:
    """Преобразует camelCase в snake_case"""

    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def convert_keys_to_snake_case(data):
    """Рекурсивно преобразует ключи всех словарей в snake_case"""

    if isinstance(data, dict):
        
        return {camel_to_snake(k): convert_keys_to_snake_case(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(item) for item in data]
    else:
        return data



# async def main():

#     data = await get_data_from_api()

#     if data:
#         print(data)

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         raise("Exit")