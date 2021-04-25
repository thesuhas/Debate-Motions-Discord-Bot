import discord
from discord.ext import commands

# Create a bot instance and sets a command prefix
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases = ['test'])
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)} ms")

@client.command()
async def help(ctx):
    embed=discord.Embed(title = 'Debate Motions Bot', description = 'A bot that gives the user Parliamentary Debate Motions')
    motions = 'List of motions, theme and number are optional parameters. Default is 5.'
    theme = 'List of available themes and the abbreviation to be used'
    random = 'List of motions, randomly chosen'
    embed.add_field(name = 'motions `theme` `number`', value = motions, inline = True)
    embed.add_field(name = 'themes', value = theme, inline = True)
    embed.add_field(name = 'random', value = random)
    await ctx.send(embed = embed)



# Runs the client (bot)
client.run('ODM1NzUyNjU3MTM4MzUyMTM4.YIUBUA.w3xIDb4hOwOSpBbKOiJzs1-CMAo')