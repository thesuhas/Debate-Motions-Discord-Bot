import discord
from discord.ext import commands
from web_scrape import motion_scrape
import csv

# Create a bot instance and sets a command prefix
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

# Initialising Keywords
keys = list()

@client.event
async def on_ready():
    # Creating csv file
    global keys
    with open("keywords.csv", "r") as inputfile:
        for row in csv.reader(inputfile):
            keys.append(row[0])

    print('Bot is ready')

@client.command(aliases = ['test'])
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)} ms")

@client.command()
async def help(ctx):
    embed=discord.Embed(title = 'Debate Motions Bot', description = 'A bot that gives the user Parliamentary Debate Motions')
    motions = 'List of motions, keywords and number are optional parameters. Default is 5.'
    keywords = 'List of available keywords'
    random = 'List of motions, randomly chosen'
    embed.add_field(name = 'motions `keywords` `number`', value = motions, inline = True)
    embed.add_field(name = 'Keywords', value = keywords, inline = True)
    embed.add_field(name = 'random', value = random)
    await ctx.send(embed = embed)

@client.command()
async def keywords(ctx):
    global keys
    s = '**Available Keywords:**\n'
    for i in keys:
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

@client.command(aliases=['add'])
async def key_append(ctx, keyword):
    global keys
    # To add a keyword to the list
    keys.append(keyword)
    # Updating csv file
    keyword += '\n'
    with open("keywords.csv", 'a') as inputfile:
        inputfile.write(keyword)

@client.command(aliases=['delete'])
async def key_delete(ctx, keyword):
    global keys
    # To delete a keyword from the list
    try:
        keys.remove(keyword)
        # Overwrite csv file
        with open('keywords.csv', 'w') as inputfile:
            writer = csv.writer(inputfile)
            for i in keys:
                writer.writerow(i)  
    except:
        await ctx.send("Keyword not in given list. Use `.keywords` to get the list of available keywords")


# Runs the client (bot)
client.run('ODM1NzUyNjU3MTM4MzUyMTM4.YIUBUA.w3xIDb4hOwOSpBbKOiJzs1-CMAo')