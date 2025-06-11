import discord
from discord.ext import commands
import requests
import os

class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rank(self, ctx, roblox_user: str, rank_name: str):
        payload = {
            "username": roblox_user,
            "rank": rank_name
        }
        headers = {
            "Authorization": f"Bearer {os.getenv('RANK_API_KEY')}"
        }
        api_url = os.getenv("RANK_API_URL")

        try:
            response = requests.post(api_url, json=payload, headers=headers)
            if response.status_code == 200:
                await ctx.send(f"✅ {roblox_user} has been ranked to {rank_name}.")
            else:
                await ctx.send(f"❌ Failed to rank {roblox_user}. Error: {response.text}")
        except Exception as e:
            await ctx.send(f"⚠️ API error: {e}")

def setup(bot):
    bot.add_cog(Roblox(bot))
