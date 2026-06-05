"""using Flask server for enabling bot to run on or with the help of Flask server. Use this file to run bot when you are using hosting services such as render to deploy bot as a web service.
"""

from flask import Flask
from discord.ext import commands
from dotenv import load_dotenv
from animes import random_anime
from sync_commands import sync_cmds
import threading
import discord
import asyncio
import os

load_dotenv(dotenv_path=".env")
app = Flask(__name__)

@app.get("/")
def bot_status():
    return "Cookie discord bot is now alive!"

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
def run_flask_server():
    PORT = os.getenv("PORT")
    app.run(host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    try:
        asyncio.run(load_slash_commands())
        BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
        flask_thread = threading.Thread(target=run_flask_server)
        flask_thread.daemon = True
        flask_thread.start()
        
        bot.run(BOT_TOKEN)
    except KeyboardInterrupt:
        print("bye!")  # <- Just for development testing purpose
