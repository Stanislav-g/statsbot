import discord
from discord.ext import commands
import os
 

client = commands.Bot( command_prefix = '!!')
client.remove_command('help')


@client.event
async def on_redy():
    print( 'Bot connected')      


@client.command()
@commands.has_permissions(administrator = True)
async def send_m(ctx, *, arg):
    await ctx.channel.purge(limit = 1)
    await ctx.send('```' + arg + '```') 
 
 
# RUN
token= os.environ.get('BOT_TOKEN')
client.run( token )
