import httpx
import json


async def getmanga():
    """Retrieve random mangas

    Returns:
        Any: Manga with specific details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url="https://api.jikan.moe/v4/random/manga")

        manga = json.loads(response.text)
        return manga
    except Exception as e:
        return e
