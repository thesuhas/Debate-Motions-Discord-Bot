import discord
from discord.ext import commands
from web_scrape import motion_scrape

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
    motions = 'List of motions, keywords and number are optional parameters. Default is 5.'
    keywords = 'List of available keywords and the abbreviation to be used'
    random = 'List of motions, randomly chosen'
    embed.add_field(name = 'motions `keywords` `number`', value = motions, inline = True)
    embed.add_field(name = 'Keywords', value = keywords, inline = True)
    embed.add_field(name = 'random', value = random)
    await ctx.send(embed = embed)

@client.command()
async def keywords(ctx):
    theme = ['International Relations',
            'Economics',
            'Feminism',
            'Narratives',
            'Policy',
            "United States",
            "India",
            "Criminal Justice"]
    
    s = '**Available Themes:**\n'
    for i in theme:
        s += i + '\n'

    await ctx.send(s)

    
@client.command()
async def motions(ctx, *, words):
    words = words.split(' ')
    
    # Num exists only if length of words > 1 and if last one is a number
    if len(words) > 1 and words[-1].isdigit():
        num = int(words[-1])
        words = words[:-1]
        await ctx.send(motion_scrape(words, num))
    else:
        await ctx.send(motion_scrape(words))

    

    


# Runs the client (bot)
client.run('ODM1NzUyNjU3MTM4MzUyMTM4.YIUBUA.w3xIDb4hOwOSpBbKOiJzs1-CMAo')