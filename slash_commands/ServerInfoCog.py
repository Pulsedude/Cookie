from discord.ext import commands
from discord import app_commands
import discord

# ----------------------------
# Basic Config
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.members = True

# Command prefix
bot = commands.Bot(command_prefix=",", intents=intents)


class ServerInfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='serverinfo', description='See server info')
    async def ServerInfo(self, interaction: discord.Interaction):
        user = interaction.user

        icon = interaction.guild.icon.with_size(64)
        name = interaction.guild.name

        guild_info = {
            "server": interaction.guild.name,
            "owner": interaction.guild.owner,
            "server id": interaction.guild.id,
            "description": interaction.guild.description,
            "members": interaction.guild._member_count,
            "created at": interaction.guild.created_at
        }

        await interaction.response.defer()
        try:
            embed = discord.Embed(
                title=f"{name}",
                color=discord.Color.yellow(),
            )

            embed.set_thumbnail(url=icon.url)  # server icon
            for key, val in guild_info.items():
                embed.add_field(name=key, value=val, inline=True)

            embed.set_footer(
                text=f"Requested by {user.name}",
                icon_url=user.display_avatar.url
            )
            await interaction.followup.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                description=e,
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(ServerInfoCog(bot))
