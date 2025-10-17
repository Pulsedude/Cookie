from discord.ext import commands
from discord import app_commands
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


class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Check bot latency')
    async def get_manga_magazines(self, interaction: discord.Interaction):
        """Cog to check bot latency

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash command)
        """
        await interaction.response.defer()
        latency = bot.latency
        try:
            if latency is None or latency != latency:
                await interaction.followup.send("Latency is not available right now ;-;")
                return

            latency_ms = round(latency * 1000)  # latency in milliseconds
            await interaction.followup.send(f"Pong! `{latency_ms}ms`")
        except Exception as e:
            await interaction.followup.send(e)


async def setup(bot: commands.Bot):
    await bot.add_cog(PingCog(bot))
