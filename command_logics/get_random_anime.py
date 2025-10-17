import httpx
import json


async def random_anime():
    """Retrieve random animes with their details

    Returns:
        Any: Anime 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/random/anime")

        return json.loads(response.text)
    except Exception as e:
        return e
