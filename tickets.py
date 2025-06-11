from discord.ext import commands
from discord import ui, ButtonStyle, Interaction, Embed, PermissionOverwrite
import discord

class TicketButton(ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @ui.button(label="Open Ticket", style=ButtonStyle.green)
    async def open_ticket(self, interaction: Interaction, button: ui.Button):
        guild = interaction.guild
        overwrites = {
            guild.default_role: PermissionOverwrite(read_messages=False),
            interaction.user: PermissionOverwrite(read_messages=True, send_messages=True)
        }
        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            overwrites=overwrites,
            topic=f"Ticket for {interaction.user.name}"
        )
        await ticket_channel.send(f"<@{interaction.user.id}> Please describe your issue.")
        log_channel = discord.utils.get(guild.text_channels, name="ticket-logs")
        if log_channel:
            await log_channel.send(f"Ticket created by {interaction.user.mention}: {ticket_channel.mention}")
        await interaction.response.send_message(f"Ticket created: {ticket_channel.mention}", ephemeral=True)

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx):
        embed = Embed(title="Support", description="Click below to open a ticket.")
        view = TicketButton(self.bot)
        await ctx.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Tickets(bot))
