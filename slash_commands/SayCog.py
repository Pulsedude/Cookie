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
bot = commands.Bot(command_prefix=",", intents=intents, help_command=None)


class SayCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='say', description='Make bot say something')
    async def say(self, interaction: discord.Interaction, message: str):
        """Say Cog

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash command)
        """
        await interaction.response.defer()
        try:
            await interaction.followup.send(message)
        except Exception as e:
            embed = discord.Embed(
                description=f"Oops! Something went wrong. Please try again in few moments. {e}" or "Cooldown! Try again in few seconds.",
                color=discord.Color.orange()
            )

            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(SayCog(bot))
