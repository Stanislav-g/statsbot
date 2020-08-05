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
    await ctx.author.send('```' + arg + '```') 
 
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 728658937905414234: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '📖': # Emoji для реакций
            role = guild.get_role(728659726870511677) # ID Ролей для выдачи 
 
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                channel = client.get_channel( 738779492339941537 )
                await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, поставил реакцию 📖 в канале правила') )
     
# RUN
token= os.environ.get('BOT_TOKEN')
client.run( token )
