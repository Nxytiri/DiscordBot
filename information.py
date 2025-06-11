from discord.ext import commands
import discord

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="Server Info", description="Details about this server.")
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=False)
        embed.add_field(name="Owner", value=str(ctx.guild.owner), inline=False)
        embed.add_field(name="Members", value=ctx.guild.member_count, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def rules(self, ctx):
        rules = (
            "**Server Rules:**\n"
            "1. Be respectful\n"
            "2. No spamming\n"
            "3. Use channels appropriately\n"
            "4. No NSFW content\n"
            "5. Follow Discord's ToS"
        )
        await ctx.send(rules)

def setup(bot):
    bot.add_cog(Information(bot))
