from discord.ext import commands
from commands import (
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
    specific_anime
)
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


def sync_cmds(bot):
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
