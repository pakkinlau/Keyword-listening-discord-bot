import discord
from discord.ext import commands
import discord.state
import os


import _db

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!',intents=intents)

# Load assets from .env (currently not working)
"""
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
"""
TOKEN = "...."
GUILD = ....



def get_manual_url(syntax):
    value = _db.manual_db[syntax]
    url = "https://www.tradingview.com/pine-script-reference/v5/#"+value
    return url

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")    
    print(f"list of client guilds: {bot.guilds}")
    
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f"Guild name and ID are: {guild.name}, {guild.id}")

"""
@bot.event
async def on_message(message):
    
    (The following snippets forbid any extra commands from running)
    if message.content == '99!':
        response = 'ss (rerun)'
        await message.channel.send(response)

    if message.content == '99!':
        response = 'ss (rerun)'
        await message.channel.send(response)
    
    await bot.process_commands(message)
"""
@bot.listen('on_message')
async def on_message(message):

    if message.content == '99!':
        response = 'ss (rerun)'
        await message.channel.send(response)


@bot.command()
async def test(ctx):
    await ctx.send('test def')

@bot.command()
async def show(ctx, arg):
    "Return the variables value. Example: ctx.guild.id"
    output = eval(arg)
    await ctx.send(str(output))

@bot.command()
async def sym(ctx,arg):
    "Return the manual url that we recognize, if it is not registered, return that error message."
    "The case 2 and 3 are prepared for symbolic difference"
    echo_message =f"Checking reference manual for this syntax:`{arg}`"
    found_message = "Found. Here is the link."
    teach_message = f"And all available bot commands for this server could be found on: https://discord.com/channels/767442862865776660/915350446414110730/1006656013740548137"
    if arg in list(_db.manual_db):
        url = get_manual_url(arg)
        await ctx.send(str(echo_message))
        await ctx.send(str(found_message))
        await ctx.send(str(url))
        await ctx.send(str(teach_message))
    elif arg[:len(arg)-1] in list(_db.manual_db):
        url = get_manual_url(arg[:len(arg)-1])
        await ctx.send(str(echo_message))
        await ctx.send(str(found_message))
        await ctx.send(str(url))
        await ctx.send(str(teach_message))    
    elif arg[:len(arg)-2] in list(_db.manual_db):
        url = get_manual_url(arg[:len(arg)-2])
        await ctx.send(str(echo_message))
        await ctx.send(str(found_message))
        await ctx.send(str(url))
        await ctx.send(str(teach_message))
    else:
        error_message = "The syntax is not recognized."
        await ctx.send(str(echo_message))
        await ctx.send(str(error_message))
        await ctx.send(str(teach_message))
        

bot.run(TOKEN)
