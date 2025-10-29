import httpx
import json


async def anime_genres():
    """Retrive anime genres list through Jikan's API

    Returns:
        dict: list of anime genres 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/genres/anime")

        return json.loads(response.text)
    except Exception as e:
        return e
