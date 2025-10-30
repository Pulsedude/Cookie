import httpx
import json


async def top_mangas():
    """Retrive top mangas list through Jikan's API

    Returns:
        dict: list of top mangas 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/top/manga")

        return json.loads(response.text)
    except Exception as e:
        return e
