from discord.ext import commands
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
# 'say' command
# ---------------------------


@bot.command(name="say")
async def say(ctx: commands.Context, *, text: str):
    await ctx.send(text)
