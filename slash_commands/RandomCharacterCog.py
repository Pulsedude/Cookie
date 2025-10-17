from discord.ext import commands
from discord import app_commands
from command_logics.get_random_characters import random_characters
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class RandomCharacterCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def truncate(self, text, limit=1024):
        if not text:
            return "N/A"
        return text if len(text) <= limit else text[:limit-3] + "..."

    @app_commands.command(name='rchar', description='Get random anime characters')
    async def GetRandomCharacter(self, interaction: discord.Interaction):
        """Cog for getting random anime character with their details

        Args:
            interaction (discord.Interaction): interaction between user and bot (slash commandd
        """
        user = interaction.user
        await interaction.response.defer()
        try:
            character = await random_characters()
            ch = character['data']

            embed = discord.Embed(
                color=discord.Color.yellow()
            )

            # Character image
            embed.set_image(
                url=ch['images']['jpg']['image_url'])

            # Name
            embed.add_field(
                name="Name", value=f"[{ch['name']}]({ch['url']})", inline=False)

            # About
            embed.add_field(name="About", value=self.truncate(
                ch.get('about')), inline=False)

            embed.set_footer(
                text=f"Requested by {user.name}",
                icon_url=user.display_avatar.url
            )

            await interaction.followup.send(embed=embed)

        except Exception:
            embed = discord.Embed(
                description="Cooldown! Try again in few seconds.",
                color=discord.Color.orange()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(RandomCharacterCog(bot))
