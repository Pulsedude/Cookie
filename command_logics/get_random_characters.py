import httpx
import random
import json


async def random_characters():
    """Retrieve random anime character with their details

    Returns:
        Any: Info
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=f"https://api.jikan.moe/v4/characters/{random.randrange(1, 45000)}")

        return json.loads(response.text)
    except Exception as e:
        return e
