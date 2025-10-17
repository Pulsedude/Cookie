from discord.ext import commands
from discord import app_commands
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


class JpTranslationCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='injp', description='Translate given text into japanese')
    async def JpTranslation(self, interaction: discord.Interaction, text: str):
        """Cog for translating given text to japanese

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash command)
            text (str): text to translate into japanese
        """
        try:
            await interaction.response.defer()
            translated_text = await jp_translate(text=text)
            await interaction.followup.send(translated_text)

        except Exception as e:
            embed = discord.Embed(
                title="Oops!",
                description=e,
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(JpTranslationCog(bot))
