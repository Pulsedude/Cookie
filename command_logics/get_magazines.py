import httpx
import json


async def manga_magazines():
    """Retrive manga magazines list through Jikan's API

    Returns:
        dict: list of manga magazines 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/magazines")

        return json.loads(response.text)
    except Exception as e:
        return e
