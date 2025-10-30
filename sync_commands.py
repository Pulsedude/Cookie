from discord.ext import commands
from commands import (
    anime_genres,
    translatetojp,
    serverinfo,
    magazines,
    ping,
    say,
    random_manga,
    specific_manga,
    random_characters,
    specific_character,
    random_anime,
    specific_anime,
    manga_genres,
    top_animes,
    top_mangas,
    help
)
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents, help_command=None)


def sync_cmds(bot):
    """Sync all prefix commands
    """
    bot.add_command(translatetojp.translate_text)
    bot.add_command(serverinfo.server_info)
    bot.add_command(magazines.get_manga_magazines)
    bot.add_command(ping.ping)
    bot.add_command(say.say)
    bot.add_command(random_manga.get_random_manga)
    bot.add_command(specific_manga.get_specific_manga)
    bot.add_command(random_characters.get_random_character)
    bot.add_command(specific_character.get_specific_character)
    bot.add_command(random_anime.get_random_anime)
    bot.add_command(specific_anime.get_specific_anime)
    bot.add_command(anime_genres.get_anime_genres)
    bot.add_command(manga_genres.get_manga_genres)
    bot.add_command(top_animes.top_animes_list)
    bot.add_command(top_mangas.top_mangas_list)
    bot.add_command(help.help)
