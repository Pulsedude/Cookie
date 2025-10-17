from discord.ext import commands
from discord import app_commands
from command_logics.get_specific_manga import specific_manga
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class SpecificMangaCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def truncate(self, text, limit=1024):
        if not text:
            return "N/A"
        return text if len(text) <= limit else text[:limit-3] + "..."

    @app_commands.command(name='manga', description='See specific manga details')
    async def GetSpecificMangDetails(self, interaction: discord.Interaction, manga: str):
        user = interaction.user
        await interaction.response.defer()
        try:
            manga = await specific_manga(manga=manga)

            m = manga['data'][0]
            embed = discord.Embed(
                color=discord.Color.yellow()
            )

            # Image
            embed.set_image(url=m['images']['jpg']['large_image_url'])

            # Name
            embed.add_field(
                name="Name", value=f"[{m['title']}]({m['url']})", inline=False)

            # Synopsis
            embed.add_field(name="Synopsis", value=self.truncate(
                m.get('synopsis')), inline=False)

            # Background
            embed.add_field(name="Background", value=self.truncate(
                m.get('background')), inline=False)

            # Authors
            authors = ", ".join([a['name']
                                for a in m.get('authors', [])]) or "N/A"
            embed.add_field(
                name="Authors", value=self.truncate(authors), inline=True)

            # Genres
            genres = ", ".join([g['name']
                               for g in m.get('genres', [])]) or "N/A"
            embed.add_field(
                name="Genres", value=self.truncate(genres), inline=True)

            # Themes
            themes = ", ".join([t['name']
                               for t in m.get('themes', [])]) or "N/A"
            embed.add_field(
                name="Themes", value=self.truncate(themes), inline=True)

            # Status
            embed.add_field(name="Status", value=self.truncate(
                m.get('status')), inline=True)

            # Published
            pub_date = m.get('published', {}).get('from')
            embed.add_field(name="Published",
                            value=self.truncate(pub_date), inline=True)

            # Chapters / Volumes
            embed.add_field(name="Chapters", value=self.truncate(
                str(m.get('chapters', 'N/A'))), inline=True)
            embed.add_field(name="Volumes", value=self.truncate(
                str(m.get('volumes', 'N/A'))), inline=True)

            embed.set_footer(
                text=f"Requested by {user.name}",
                icon_url=user.display_avatar.url
            )

            await interaction.followup.send(embed=embed)

        except Exception:
            embed = discord.Embed(
                description=f"Could not found any manga with name '{manga}' ;-;",
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(SpecificMangaCog(bot))
