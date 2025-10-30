import httpx
import json


async def top_animes():
    """Retrive top animes list through Jikan's API

    Returns:
        dict: list of top animes 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/top/anime")

        return json.loads(response.text)
    except Exception as e:
        return e
