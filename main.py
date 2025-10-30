from discord.ext import commands
from dotenv import load_dotenv
from animes import random_anime
from sync_commands import sync_cmds
import discord
import os
import asyncio

load_dotenv(dotenv_path=".env")

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents, help_command=None)

# ----------------------------
# Bot Events
# ----------------------------


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{random_anime()}")
    )
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.tree.sync()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(error)

# ----------------------------
# Sync perfix commands
# ----------------------------
sync_cmds(bot)


# ----------------------------
# Sync slash commands
# ----------------------------
async def load_slash_commands():
    command_dir = os.path.join(os.path.dirname(__file__), "slash_commands")
    for filename in os.listdir(command_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            ext = f"slash_commands.{filename[:-3]}"
            print(f"Loading: {ext}")
            await bot.load_extension(ext)


# ----------------------------
# Run the Bot
# ----------------------------
async def main():
    await load_slash_commands()
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if not TOKEN:
        print("❌ Please set the DISCORD_BOT_TOKEN environment variable.")
    else:
        await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bye!")  # <- Just for testing purpose
