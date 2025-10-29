from discord.ext import commands
from discord import app_commands
from command_logics.get_anime_genres import anime_genres
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class AnimeGenresCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='angenres', description='See top 25 anime genres')
    async def get_anime_genres(self, interaction: discord.Interaction):
        """Cog to see top 25 anime genres list

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash command)
        """
        user = interaction.user
        await interaction.response.defer()
        try:
            genres = await anime_genres()
            all_genres = ""
            for genre in genres['data']:
                all_genres += f"{genre["mal_id"]}. **{genre["name"]}**   [See on MyAnimeList]({genre["url"]})\n"

            embed = discord.Embed(
                title="Top 25 anime genres",
                description=all_genres,
                color=discord.Color.yellow()
            )
            embed.set_footer(
                text=f"Requested by {user.name}",
                icon_url=user.display_avatar.url
            )
            await interaction.followup.send(embed=embed)

        except Exception:
            embed = discord.Embed(
                description="Oops! Something went wrong. Please try again in few moments.",
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(AnimeGenresCog(bot))
