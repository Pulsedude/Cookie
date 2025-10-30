from discord.ext import commands
from discord.ui import View, Button
from command_logics.get_top_mangas import top_mangas
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


# ---------------------------
# 'topmangas' command
# ---------------------------

MAX_FIELD_LENGTH = 1024


def truncate(text, limit=MAX_FIELD_LENGTH):
    if not text:
        return "N/A"
    return text if len(text) <= limit else text[:limit-3] + f"..."


@bot.command(name='topmangas')
async def top_mangas_list(ctx: commands.Context):
    try:
        manga_list = await top_mangas()

        pages = []
        for i in range(len(manga_list["data"])):
            m = manga_list["data"][i]
            embed = discord.Embed(
                color=discord.Color.yellow()
            )

            # Manga banner
            embed.set_image(
                url=m['images']['jpg']['large_image_url'])

            # Name
            embed.add_field(
                name="Name", value=f"[{m['title']}]({m['url']})", inline=False)

            # Synopsis
            embed.add_field(name="Synopsis", value=truncate(
                m.get('synopsis')), inline=False)

            # Background
            embed.add_field(name="Background", value=truncate(
                m.get('background')), inline=False)

            # Season
            embed.add_field(name="Season", value=truncate(
                m.get('season')), inline=True)

            # Status
            embed.add_field(name="Status", value=m['status'], inline=True)

            # Score
            embed.add_field(name="Score", value=m['score'], inline=True)

            # Rank
            embed.add_field(name="Rank", value=m['rank'], inline=True)

            # Studios
            studios = ", ".join([s['name']
                                for s in m.get('studios', [])]) or "N/A"
            embed.add_field(
                name="Studios", value=truncate(studios), inline=True)

            # Genres
            genres = ", ".join([s['name']
                               for s in m.get('genres', [])]) or "N/A"
            embed.add_field(name="Genres", value=truncate(genres), inline=True)

            # Themes
            themes = ", ".join([s['name']
                               for s in m.get('themes', [])]) or "N/A"
            embed.add_field(name="Themes", value=truncate(themes), inline=True)

            embed.set_footer(text=f"Page {i+1} of 10")
            pages.append(embed)

        view = PaginatorView(pages, ctx.author)
        await ctx.send(embed=pages[0], view=view)

    except Exception:
        embed = discord.Embed(
            description="Oops! Something went wrong. Please try again in few moments." or "Cooldown! Try again in few seconds.",
            color=discord.Color.orange()
        )

        await ctx.reply(embed=embed)
