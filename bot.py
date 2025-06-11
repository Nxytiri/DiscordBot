import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

initial_extensions = ['cogs.moderation', 'cogs.tickets', 'cogs.roblox', 'cogs.information']
for ext in initial_extensions:
    bot.load_extension(ext)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
