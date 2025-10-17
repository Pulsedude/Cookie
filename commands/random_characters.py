from discord.ext import commands
from command_logics.get_random_characters import random_characters
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


@bot.command(name="rcharacter")
async def get_random_character(ctx: commands.Context):
    user = ctx.author
    try:
        character = await random_characters()
        ch = character['data']

        embed = discord.Embed(
            color=discord.Color.yellow()
        )

        # Character image
        embed.set_image(
            url=ch['images']['jpg']['image_url'])

        # Name
        embed.add_field(
            name="Name", value=f"[{ch['name']}]({ch['url']})", inline=False)

        # About
        embed.add_field(name="About", value=truncate(
            ch.get('about')), inline=False)

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
