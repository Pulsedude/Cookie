from discord.ext import commands
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
# 'serverinfo' command
# ---------------------------


@bot.command(name="serverinfo")
async def server_info(ctx: commands.Context):
    user = ctx.author

    icon = ctx.guild.icon.with_size(64)
    name = ctx.guild.name

    guild_info = {
        "server": ctx.guild.name,
        "owner": ctx.guild.owner,
        "server id": ctx.guild.id,
        "description": ctx.guild.description,
        "members": ctx.guild._member_count,
        "created at": ctx.guild.created_at
    }

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
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            description=e,
            color=discord.Color.red()
        )
        await ctx.reply(embed=embed)
