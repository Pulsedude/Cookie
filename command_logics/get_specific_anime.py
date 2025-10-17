import httpx
import json


async def specific_anime(name: str):
    """Get details of any anime 

    Args:
        name (str): Anime name

    Returns:
        Any: Details of Anime
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=f"https://api.jikan.moe/v4/anime?q={name}&limit=1")

        return json.loads(response.text)
    except Exception as e:
        return e
