import httpx
import json


async def specific_manga(manga: str):
    """Know about any specific manga

    Args:
        manga (str): Manga name

    Returns:
        Any: Details of manga
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=f"https://api.jikan.moe/v4/manga?q={manga}&limit=1")

        manga = json.loads(response.text)
        return manga
    except Exception as e:
        return e
