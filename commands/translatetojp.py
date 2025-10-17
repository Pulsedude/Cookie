from discord.ext import commands
from command_logics.jptranslate import jp_translate
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
# 'injp' command
# ---------------------------


@bot.command(name="injp")
async def translate_text(ctx: commands.Context, *, text: str):
    try:
        translated_text = await jp_translate(text=text)
        await ctx.reply(translated_text)

    except Exception:
        embed = discord.Embed(
            description="Cooldown! Try again in few seconds.",
            color=discord.Color.orange()
        )
        await ctx.reply(embed=embed)
