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


class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='help', description='See all available options')
    async def help(self, interaction: discord.Interaction):
        """Help Cog

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash command)
        """
        await interaction.response.defer()
        try:
            help_description = """
        
            **Basic commands:**
            `,serverinfo`: See server information
            `,tojp`: To translate english text into japanese
            `,ping`: See bot current latency
            `,say`: Make bot say something
            
            
            **Core commands:**
            `,rchar`:  Retrieve random anime & manga character
            `,character [name]`: Inspect about any anime & manga character
            `,rmanga`: Get random mangas (source: MyAnimeList)
            `,ranime`: Get random animes with their specific details 
            `,anime [anime_name]`: Inspect about anime shows
            `,manga [manga_name`: Inspect about any manga
            `,magazines`: Retrieve  top manga magazines list
            `,topanimes`: See list of top anime shows
            `,topmangas`: See list of top mangas
            
            You can even use slash commands by just typing `/` and command name!
            """
            embed = discord.Embed(
                title="Cookie is your cozy anime companion! 🍪",
                description=help_description,
                color=discord.Color.yellow()
            )

            await interaction.followup.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                description=f"Oops! Something went wrong. Please try again in few moments. {e}" or "Cooldown! Try again in few seconds.",
                color=discord.Color.orange()
            )

            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))
