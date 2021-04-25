import discord
from discord.ext import commands

# Create a bot instance and sets a command prefix
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases = ['test'])
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)} ms")


# Runs the client (bot)
client.run('ODM1NzUyNjU3MTM4MzUyMTM4.YIUBUA.w3xIDb4hOwOSpBbKOiJzs1-CMAo')