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
# 'ping' command
# ---------------------------


@bot.command()
async def ping(ctx):
    latency = bot.latency
    try:
        if latency is None or latency != latency:
            await ctx.reply("Latency is not available right now ;-;")
            return

        latency_ms = round(latency * 1000)  # latency in milliseconds
        await ctx.send(f"Pong! `{latency_ms}ms`")
    except Exception as e:
        await ctx.send(e)
