from discord.ext import commands
from command_logics.get_anime_genres import anime_genres
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
# 'angenres' command
# ---------------------------


@bot.command(name="angenres")
async def get_anime_genres(ctx: commands.Context):
    user = ctx.author
    try:
        genres = await anime_genres()
        all_genres = ""
        for genre in genres['data'][:25]:
            all_genres += f"{genre["mal_id"]}. **{genre["name"]}**   [See on MyAnimeList]({genre["url"]})\n"

        embed = discord.Embed(
            title="Top 25 anime genres",
            description=all_genres,
            color=discord.Color.yellow()
        )
        embed.set_footer(
            text=f"Requested by {user.name}",
            icon_url=user.display_avatar.url
        )

        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(
            description="Oops! Something went wrong. Please try again in few moments.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
