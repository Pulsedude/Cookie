from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
from command_logics.get_top_animes import top_animes
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class PaginatorView(View):
    def __init__(self, pages, author):
        super().__init__(timeout=180)  # 3-minute timeout
        self.pages = pages
        self.page = 0
        self.author = author
        self.update_buttons()

    def update_buttons(self):
        # Enable/disable buttons depending on current page
        self.previous_button.disabled = self.page == 0
        self.next_button.disabled = self.page == len(self.pages) - 1
        self.page_button.label = f"Page {self.page + 1}/{len(self.pages)}"

    async def update_message(self, interaction):
        self.update_buttons()
        await interaction.response.edit_message(embed=self.pages[self.page], view=self)

    @discord.ui.button(label="◀️", style=discord.ButtonStyle.primary)
    async def previous_button(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.author:
            return await interaction.response.send_message(
                "You can’t control this paginator.", ephemeral=True
            )
        self.page -= 1
        await self.update_message(interaction)

    @discord.ui.button(label="Page 1/1", style=discord.ButtonStyle.secondary, disabled=True)
    async def page_button(self, interaction: discord.Interaction, button: Button):
        # This button just shows the current page — no action
        pass

    @discord.ui.button(label="▶️", style=discord.ButtonStyle.primary)
    async def next_button(self, interaction: discord.Interaction, button: Button):
        if interaction.user != self.author:
            return await interaction.response.send_message(
                "You can’t control this paginator.", ephemeral=True
            )
        self.page += 1
        await self.update_message(interaction)


class TopAnimesCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def truncate(self, text, limit=1024):
        if not text:
            return "N/A"
        return text if len(text) <= limit else text[:limit-3] + "..."

    @app_commands.command(name='topanimes', description='See list of top popular animes')
    async def GetTopAnimes(self, interaction: discord.Interaction):
        """Cog for getting top tier anime shows

        Args:
            interaction (discord.Interaction): _description_
            name (str): Anime name
        """
        await interaction.response.defer()
        try:
            animes_list = await top_animes()

            pages = []
            for i in range(len(animes_list["data"])):
                an = animes_list["data"][i]
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
                embed.add_field(name="Episodes",
                                value=an['episodes'], inline=True)

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

                embed.set_footer(text=f"Page {i+1} of 25")
                pages.append(embed)

            view = PaginatorView(pages, interaction.user)
            await interaction.followup.send(embed=pages[0], view=view)

        except Exception:
            embed = discord.Embed(
                description="Oops! Something went wrong. Please try again in few moments." or "Cooldown! Try again in few seconds.",
                color=discord.Color.orange()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(TopAnimesCog(bot))
