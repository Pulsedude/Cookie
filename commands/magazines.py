from discord.ext import commands
from command_logics.get_magazines import manga_magazines
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
# 'magazines' command
# ---------------------------


@bot.command(name="magazines")
async def get_manga_magazines(ctx: commands.Context):
    user = ctx.author
    try:
        list_of_magazines = await manga_magazines()
        all_magazines = ""
        for magazine in list_of_magazines['data']:
            all_magazines += f"{magazine["mal_id"]}. **{magazine["name"]}**   [See on MyAnimeList]({magazine["url"]})\n"

        embed = discord.Embed(
            title="Manga mangazines",
            description=all_magazines,
            color=discord.Color.yellow()
        )
        embed.set_footer(
            text=f"Requested by {user.name}",
            icon_url=user.display_avatar.url
        )

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="Oops!",
            description=e,
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
