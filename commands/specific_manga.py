from discord.ext import commands
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

# ---------------------------
# 'manga' command
# ---------------------------


MAX_FIELD_LENGTH = 1024


def truncate(text, limit=MAX_FIELD_LENGTH):
    if not text:
        return "N/A"
    return text if len(text) <= limit else text[:limit-3] + f"..."


@bot.command(name="manga")
async def get_specific_manga(ctx: commands.Context, *, name: str):
    user = ctx.author
    try:
        manga = await specific_manga(manga=name)

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
        embed.add_field(name="Synopsis", value=truncate(
            m.get('synopsis')), inline=False)

        # Background
        embed.add_field(name="Background", value=truncate(
            m.get('background')), inline=False)

        # Authors
        authors = ", ".join([a['name'] for a in m.get('authors', [])]) or "N/A"
        embed.add_field(name="Authors", value=truncate(authors), inline=True)

        # Genres
        genres = ", ".join([g['name'] for g in m.get('genres', [])]) or "N/A"
        embed.add_field(name="Genres", value=truncate(genres), inline=True)

        # Themes
        themes = ", ".join([t['name'] for t in m.get('themes', [])]) or "N/A"
        embed.add_field(name="Themes", value=truncate(themes), inline=True)

        # Status
        embed.add_field(name="Status", value=truncate(
            m.get('status')), inline=True)

        # Published
        pub_date = m.get('published', {}).get('from')
        embed.add_field(name="Published",
                        value=truncate(pub_date), inline=True)

        # Chapters / Volumes
        embed.add_field(name="Chapters", value=truncate(
            str(m.get('chapters', 'N/A'))), inline=True)
        embed.add_field(name="Volumes", value=truncate(
            str(m.get('volumes', 'N/A'))), inline=True)

        embed.set_footer(
            text=f"Requested by {user.name}", icon_url=user.display_avatar.url)
        await ctx.send(embed=embed)

    except Exception:
        embed = discord.Embed(
            description="Cooldown! Try again in few seconds.",
            color=discord.Color.orange())
        await ctx.reply(embed=embed)
