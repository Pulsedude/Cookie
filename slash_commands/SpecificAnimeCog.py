from discord.ext import commands
from discord import app_commands
from command_logics.get_specific_anime import specific_anime
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class SpecificAnimeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def truncate(self, text, limit=1024):
        if not text:
            return "N/A"
        return text if len(text) <= limit else text[:limit-3] + "..."

    @app_commands.command(name='anime', description='Gee details about any specific anime show')
    async def GetSpecificAnime(self, interaction: discord.Interaction, name: str):
        """Cog for getting details about any specific anime show

        Args:
            interaction (discord.Interaction): _description_
            name (str): Anime name
        """
        user = interaction.user
        await interaction.response.defer()
        try:
            anime = await specific_anime(name=name)
            an = anime['data'][0]

            embed = discord.Embed(
                color=discord.Color.yellow()
            )

            # Anime banner
            embed.set_image(
                url=an['images']['jpg']['large_image_url'])

            # Name
            embed.add_field(
                name="Name", value=f"[{an['title']}]({an['url']})", inline=False)

            # Synopsis
            embed.add_field(name="Synopsis", value=self.truncate(
                an.get('synopsis')), inline=False)

            # Background
            embed.add_field(name="Background", value=self.truncate(
                an.get('background')), inline=False)

            # Season
            embed.add_field(name="Season", value=self.truncate(
                an.get('season')), inline=True)

            # Episodes
            embed.add_field(name="Episodes", value=an['episodes'], inline=True)

            # Status
            embed.add_field(name="Status", value=an['status'], inline=True)

            # Score
            embed.add_field(name="Score", value=an['score'], inline=True)

            # Rank
            embed.add_field(name="Rank", value=an['rank'], inline=True)

            # Studios
            studios = ", ".join([s['name']
                                for s in an.get('studios', [])]) or "N/A"
            embed.add_field(
                name="Studios", value=self.truncate(studios), inline=True)

            # Genres
            genres = ", ".join([s['name']
                               for s in an.get('genres', [])]) or "N/A"
            embed.add_field(
                name="Genres", value=self.truncate(genres), inline=True)

            # Themes
            themes = ", ".join([s['name']
                               for s in an.get('themes', [])]) or "N/A"
            embed.add_field(
                name="Themes", value=self.truncate(themes), inline=True)

            embed.set_footer(
                text=f"Requested by {user.name}",
                icon_url=user.display_avatar.url
            )

            await interaction.followup.send(embed=embed)

        except Exception:
            embed = discord.Embed(
                description=f"Could not found any anime with name '{name}' ;-;",
                color=discord.Color.orange()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(SpecificAnimeCog(bot))
