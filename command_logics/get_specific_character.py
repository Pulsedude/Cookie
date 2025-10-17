import httpx
import json


async def specific_characters(name: str):
    """See any anime character details

    Args:
        name (str): Character name

    Returns:
        Any: Details of character
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=f"https://api.jikan.moe/v4/characters?q={name}&limit=1")

        return json.loads(response.text)
    except Exception as e:
        return e
