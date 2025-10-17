from googletrans import Translator


async def jp_translate(text: str) -> str:
    """Translate given text into japanese

    Args:
        text (str): Text to convert into japanese

    Returns:
        str: Japanese text
    """
    translator = Translator()
    jp_text = await translator.translate(text, dest="ja")
    return jp_text.text
