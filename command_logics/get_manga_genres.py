import httpx
import json


async def manga_genres():
    """Retrive manga genres list through Jikan's API

    Returns:
        dict: list of manga genres 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/genres/manga")

        return json.loads(response.text)
    except Exception as e:
        return e
