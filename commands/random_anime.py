from discord.ext import commands
from command_logics.get_random_anime import random_anime
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)

# ---------------------------
# 'rchar' command
# ---------------------------


MAX_FIELD_LENGTH = 1024


def truncate(text, limit=MAX_FIELD_LENGTH):
    if not text:
        return "N/A"
    return text if len(text) <= limit else text[:limit-3] + f"..."


@bot.command(name="ranime")
async def get_random_anime(ctx: commands.Context):
    user = ctx.author
    try:
        anime = await random_anime()
        an = anime['data']

        embed = discord.Embed(
            color=discord.Color.yellow()
        )

        # Anime banner
        embed.set_image(
            url=an['images']['jpg']['large_image_url'])

        # Name
        embed.add_field(
            name="Name", value=f"[{an['title']}]({an['url']})", inline=False)

        # Synopsis
        embed.add_field(name="Synopsis", value=truncate(
            an.get('synopsis')), inline=False)

        # Background
        embed.add_field(name="Background", value=truncate(
            an.get('background')), inline=False)

        # Season
        embed.add_field(name="Season", value=truncate(
            an.get('season')), inline=True)

        # Episodes
        embed.add_field(name="Episodes", value=an['episodes'], inline=True)

        # Status
        embed.add_field(name="Status", value=an['status'], inline=True)

        # Score
        embed.add_field(name="Score", value=an['score'], inline=True)

        # Rank
        embed.add_field(name="Rank", value=an['rank'], inline=True)

        # Studios
        studios = ", ".join([s['name']
                            for s in an.get('studios', [])]) or "N/A"
        embed.add_field(name="Studios", value=truncate(studios), inline=True)

        # Genres
        genres = ", ".join([s['name'] for s in an.get('genres', [])]) or "N/A"
        embed.add_field(name="Genres", value=truncate(genres), inline=True)

        # Themes
        themes = ", ".join([s['name'] for s in an.get('themes', [])]) or "N/A"
        embed.add_field(name="Themes", value=truncate(themes), inline=True)

        embed.set_footer(
            text=f"Requested by {user.name}",
            icon_url=user.display_avatar.url
        )

        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(
            description="Cooldown! Try again in few seconds.",
            color=discord.Color.orange()
        )
        await ctx.reply(embed=embed)
