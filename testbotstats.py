import discord
from discord.ext import commands

 

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
token =('NzM2ODgxODY4MDQwODMxMDU2.Xx1Qtw.ei0TwK1eowlOTwID3u8WuupiU2A')
client.run( token )
