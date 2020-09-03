import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import youtube_dl
import os
import requests
import random
from random import randint, choice, choices
import io
import random as r




client = commands.Bot( command_prefix = '-')
client.remove_command('help')
bad_words = ['suka','brandon','дурак','дебил','дибил','tonto','brandon','mario jose','Brandon','Mario Jose','дурачок','таракан','сука','негр','ниггер','Таракан',]
num = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
link = ['https://youtu.be/XVMHRAUI-h0','https://youtu.be/S5WkBjiUQCs']
@client.event

async def on_redy():
    print( 'Bot connected')
    await client.change_presence( status = discord.Status.online, activity = discord.Game( '-help' ) )
    await ctx.send( f'Hello' )







#hello
@client.command( pass_context = True )

async def hello( ctx ):
    author = ctx.message.author
    
    await ctx.send( f' { author.mention } Hello' )

#info
@client.command( pass_context = True )

async def info( ctx ):
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = 'Welcome to our server, it is designed for communication, sharing memes and also supports the themes of games, youtube and everything related to it. There are currently six bots on our server, and the commands for them are listed below.                                                                                           :arrow_right:pls help:arrow_left: :arrow_right:_help:arrow_left::arrow_right:.help:arrow_left:                                                      :arrow_right:/help:arrow_left::arrow_right:!help:arrow_left:')
    await ctx.send( embed = emb )





#mute
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute')

    await member.add_roles( mute_role )
    await ctx.send( f'У {member.mention}, ограничение чата за нарушение прав!')


    
#clear
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
    await ctx.channel.purge( limit = amount)
    await ctx.send( f'Сообщения удалены')
    await ctx.channel.purge( limit = 2 )

#kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )

    emb.set_author( name = member.name, icon_url = member.avatar_url)
    emb.add_field( name = 'Kick user',value = 'Kick user : {}'.format( member.mention ) )
    await ctx.send( embed = emb )
    await ctx.send( f'kick user { member.mention}')
#ban

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )
    emb.set_author( name = member.name, icon_url = member.avatar_url)
    emb.add_field( name = 'Ban user',value = 'Banned user : {}'.format( member.mention ) )
    await ctx.send( embed = emb )
    await ctx.send( f'Ban user { member.mention}')

#unban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def unban( ctx, *, member ):
    emb.set_author( name = member.name, icon_url = member.avatar_url)
    emb = discord.Embed( title = 'unban', colour = discord.Color.red() )
    await ctx.channel.purge( limit = 1)

    banned_users = await ctx.guild.bans()
    emb.add_field( name = 'unban user',value = 'Unbaned user : {}'.format( member.mention ) )
    await ctx.send( embed = emb )
   

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban ( user)
       
        await ctx.send( f'Unbanned user {user.mention }' )

        return

#help
@client.command( pass_context = True )

async def help( ctx ):
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\nserverinfo- информация о сервере\nbotinfo- информация о боте\nuserinfo- информация о пользователе\nhello- Приветствие \navatar- фото профиля\ncovid\ntime- Время\n j- Добавить бота в голосовой канал\n l- Удалить бота из голового канала\nnum- рандомное число от 1-101\n \n Games\n\nугадайка- угадай число от 1 до 20\n sapper- сапер\nknb- камень, ножницы, бумага\nrps- камень, ножницы, бумага с ботом\ncoinflip- орел или решка?\n\n\nTEXT\n \nsend_m- отправить сообщение другому участнику через бота\nping\nmath- калькулятор\nslap- ударить рандомного участника\nunion- узнать ник\n slapperson- ударить определенного игрока\nroles- узнать роли игрока\nadd- суммировать числа\nwordnum- количество слов в тексте\ntext2- ???\nytn- рандомное видео с канала Nitagas\nyt,yt2,yt3...yt7- видео с канала nitagas\nemoji_random- рандомное эмоджи\nsearch- поиск\nyoutube_search- поиск в youtube\nwiki- поиск в википедия\nyandex- поиск в яндекс\ngoogle- поиск в гугл\nkill\n \n ')
    await ctx.send( embed = emb )

#help
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def helpadmin( ctx ):
    await ctx.channel.purge( limit = 1 )
    emb = discord.Embed( title = 'HELP', colour = discord.Color.red() )
    emb.add_field( name = 'Commands',value = ' info- Информация\n\n Для админов \n \n text- писать от бота\nclear\n ban\n unban\n kick\nrainbow\n youtube- видео с nitagas\n\nchanging_name- изменить ник\nevent_roles- розогрыш ролей\ntempban s m h d\ntmute- voice mute\ntemp_add_role +time @ role\nadd_role +@ +role\ntempmute +time @ arg\nchannel_create +name\nvoice_create +name\nemojie +id message + emoji\nsuggest +arg')
    await ctx.send( embed = emb )
#time
@client.command( pass_context = True )


async def time( ctx ):
    emb = discord.Embed( title = 'Time', colour = discord.Colour.red(), url = 'https://time100.ru/')

    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.set_footer( text = 'Спасибо за использование нашего бота!')
    emb.set_image( url = 'https://upload.wikimedia.org/wikipedia/ru/thumb/2/2a/Adventure_Time_with_Finn_%26_Jake.png/274px-Adventure_Time_with_Finn_%26_Jake.png')
    emb.set_thumbnail( url = 'https://png.pngtree.com/png-vector/20190119/ourlarge/pngtree-clock-line-filled-icon-png-image_325450.jpg')

    now_date = datetime.datetime.now()

    emb.add_field( name = 'Time', value = 'Time : {}'.format( now_date ) )

    await ctx.send( embed = emb )



#autorole
@client.event

async def on_member_join( member ):
    channel = client.get_channel( 705461507953262793 )

    role = discord.utils.get( member.guild.roles, id = 705364781753958450 )

    await member.add_roles( role )
    await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, присоеденился к нам!') )
    await member.send( f'{ member.name}, Добро пожаловать на наш сервер, ознакомьтесь с правилами нашего сервера\n\nБудьте дружелюбны к другим участникам\n\nМат запрещен\n\nЭтот сервер создан для общения\n\nПропиши команду -help что-бы узнать мои комманды')

@client.command()
async def send_a( ctx ):
    await ctx.autor.send('kj')
#отправка личных сообщений
@client.command()

async def send_m( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )
    await member.send( f'{ member.name}, Привет, от  { author.name }')







    
@clear.error
async def clear_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@ban.error    
async def ban_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@unban.error    
async def unban_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')
@kick.error    
async def kick_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

@send_m.error    
async def send_m_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

linkmusic = []
@client.command()
async def skip(ctx):
    global linkmusic
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        await ctx.send('⏭️ Следующий трек')
        voice.stop()
        song_there = os.path.isfile('song.mp3')

        try:
            if song_there:
                os.remove('song.mp3')
                print('[log] Старый файл удален')
        except PermissionError:
            print('[log] Не удалось удалить файл')

        await ctx.send('Пожалуйста ожидайте')

        voice = get(client.voice_clients, guild = ctx.guild)

        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('[log] Загружаю музыку...')
            ydl.download([linkmusic])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name = file
                print(f'[log] Переименовываю файл: {file}')
                os.rename(file, 'song.mp3')

        voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        song_name = name.rsplit('-', 2)
        await ctx.send(f'Сейчас проигрывает музыка: {song_name[0]}')
        linkmusic = []


@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_playing():
        await voice.stop()
        await ctx.send(f"⏹️ Mузыка остановлена")

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected():
        await ctx.send('⏸️ Музыка поставлена на паузу')
        voice.pause()

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected():
        if voice.is_playing():
            await ctx.send('⏯️ Музыка была возабновлена')
            voice.resume()
            
#filter
@client.event
async def on_message ( message ):
    await client.process_commands( message )

    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        await message.author.send( f'{ message.author.name}, Не надо писать плохие слова! ')

#join to channel
@client.command()
async def join(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоеденился к каналу: {channel}')
        
#leave from channel
@client.command()
async def leave(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот отключился от канала: {channel}')
#youtube

@client.command( pass_context = True )

async def yt( ctx ):
    await ctx.send(f'https://www.youtube.com/channel/UCxgNsXB1YGiY3oW2pELE87Q')
    await ctx.send( embed = emb )
@client.command( pass_context = True )

async def yt2( ctx ):
    await ctx.send(f'https://youtu.be/T9u9nn0lscs')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt3( ctx ):
    await ctx.send(f'https://youtu.be/0CFby0bAsUI')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt4( ctx ):
    await ctx.send(f'https://youtu.be/S5WkBjiUQCs')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt5( ctx ):
    await ctx.send(f'https://youtu.be/p3-pF2ms9ag')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt6( ctx ):
    await ctx.send(f'https://youtu.be/FCMbQVa577o')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt7( ctx ):
    await ctx.send(f'https://youtu.be/oVMjZx2D4ZI')
    await ctx.send( embed = emb )

@client.command( pass_context = True )

async def yt8( ctx ):
    await ctx.send(f'https://youtu.be/3MsvbceklK8')
    await ctx.send( embed = emb )






@client.command()
async def add_music(ctx, url : str):
    global linkmusic
    linkmusic = url

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile('songg.mp3')

    try:
        if song_there:
            os.remove('songg.mp3')
            print('[log] Старый файл удален')
    except PermissionError:
        print('[log] Не удалось удалить файл')

    await ctx.send('Пожалуйста ожидайте')

    voice = get(client.voice_clients, guild = ctx.guild)

    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку...')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Переименовываю файл: {file}')
            os.rename(file, 'songg.mp3')

    voice.play(discord.FFmpegPCMAudio('songg.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send(f'Сейчас проигрывает музыка: {songg_name[0]}')


@client.command()
@commands.has_permissions( administrator = True )
async def playnonestop(ctx, url : str):
    song_there = os.path.isfile('song.mp3')
    while True:
        try:
            if song_there:
                os.remove('song.mp3')
                print('[log] Старый файл удален')
        except PermissionError:
            print('[log] Не удалось удалить файл')

        await ctx.send('Пожалуйста ожидайте')

        voice = get(client.voice_clients, guild = ctx.guild)

        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('[log] Загружаю музыку...')
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name = file
                print(f'[log] Переименовываю файл: {file}')
                os.rename(file, 'song.mp3')
        
        voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        song_name = name.rsplit('-', 2)
        await ctx.send(f'Сейчас проигрывает музыка: {song_name[0]}')







#num 
@client.command( pass_context = True )

async def num( ctx ):
    await ctx.send(random.randint(1,101))
  










        





#text
@client.command()
@commands.has_permissions( administrator = True )
async def text(ctx, arg):
    await ctx.channel.purge( limit = 1 )
    await ctx.send(arg)
#text2
@client.command()
async def text2(ctx, arg1, arg2):
    await ctx.channel.purge( limit = 1 )
    await ctx.send('You passed {} and {}'.format(arg1, arg2))
#wordnum
@client.command()
async def wordnum(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
#add
@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


#slap
class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@client.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

#roles
class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@client.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))

#union
import typing

@client.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
    await ctx.send(what)
#slapperson
@client.command()
async def slapperson(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@slap.error    
async def slap_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@union.error    
async def union_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

@slapperson.error    
async def slapperson_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@roles.error    
async def roles_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@add.error    
async def add_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@wordnum.error    
async def wordnum_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')


@text.error    
async def text_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

@text2.error    
async def text2_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')







#youtube
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def youtube( ctx,  ):
    await ctx.channel.purge( limit = 1 )

    while True:
        await ctx.send( f'Переходите на канал Nitagas\n https://www.youtube.com/channel/UCxgNsXB1YGiY3oW2pELE87Q')
        await asyncio.sleep(28800)
        await ctx.send( f'Переходите на канал Nitagas\n https://www.youtube.com/channel/UCxgNsXB1YGiY3oW2pELE87Q')
        await asyncio.sleep(28800)
        








r_words = ['stop']



@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def rainbow( ctx, member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    while True:
       
            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '1')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '1')
        await member.remove_roles( ppp_role )

      
            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '2')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '2')
        await member.remove_roles( ppp_role )

        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '3')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '3')
        await member.remove_roles( ppp_role )

        
            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '4')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '4')
        await member.remove_roles( ppp_role )

     
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '5')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '5')
        await member.remove_roles( ppp_role )

            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '6')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '6')
        await member.remove_roles( ppp_role )

            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '7')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '7')
        await member.remove_roles( ppp_role )

     
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '8')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '8')
        await member.remove_roles( ppp_role )

            
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '9')
        await member.add_roles( ppp_role )
        await asyncio.sleep(3)
        ppp_role = discord.utils.get( ctx.message.guild.roles, name = '9')
        await member.remove_roles( ppp_role )
       

       

            
@rainbow.error    
async def rainbow_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

#ytn
@client.command()
async def ytn(ctx ):
    a = random.choice(['https://youtu.be/oVMjZx2D4ZI', 'https://youtu.be/T9u9nn0lscs', 'https://youtu.be/3MsvbceklK8','https://youtu.be/FCMbQVa577o','https://youtu.be/p3-pF2ms9ag','https://youtu.be/S5WkBjiUQCs','https://youtu.be/0CFby0bAsUI'])
    await ctx.send( a )
    


#emoji
@client.command()
async def emoji_random(ctx ):
    a = random.choice([':ghost:',':skull_crossbones:',':poop: ',':upside_down: ',':face_with_raised_eyebrow:',':nerd:',':face_with_monocle:',':tired_face:',':confounded:',':exploding_head:',':face_with_symbols_over_mouth:',':hot_face:',':cold_face:',':rage:',':cowboy:',':clown:',':space_invader:',':fox:',':chicken:',':penguin:',':comet:',':bow_and_arrow:',':tv:',':money_with_wings:',':gem:',':gun:',':bomb:',':firecracker:',':knife:',':toilet:',':test_tube:',':microbe:'])
    await ctx.send( a )


#coinflip
@client.command()
async def coinflip(ctx ):
    a = random.choice(['орел','решка','орел','решка','орел'])
    await ctx.send( a )




#knb
@client.command()
async def knb(ctx, member: discord.Member ):
    a = random.choice(['камень','ножницы','бумага'])
    v = random.choice(['камень','ножницы','бумага'])

    emb = discord.Embed( title = 'Камень, ножницы, бумага', colour = discord.Color.blue() )
    
    await ctx.send( embed = emb )

    emg = discord.Embed( title = f'{ member.name}', colour = discord.Color.red() )
    await ctx.send( embed = emg )

    emw = discord.Embed( title = a, colour = discord.Color.blue() )
    await ctx.send( embed = emw )

    emd = discord.Embed( title = f'{ ctx.author.name}', colour = discord.Color.red() )
    await ctx.send( embed = emd )

    emx = discord.Embed( title = v, colour = discord.Color.blue() )
    await ctx.send( embed = emx )


 
@knb.error    
async def knb_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')




#sapper
@client.command()
async def sapper(ctx):
  
    emg = discord.Embed( title = f'Game sapper\n Rules you must select a number and enter it as shown in the table below\n 1- first \n2- second\n3- third\n4- fouth\n5- fifth\n6- sixth\n7- seventh\n8- eighth\n9- ninth \ndo not forget about the prefix (-)\n\n1      2     3\n4     5     6     \n7     8     9', colour = discord.Color.red() )
    await ctx.send( embed = emg )
    

@client.command()    
async def first(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def second(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def third(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )


@client.command()    
async def fouth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def fifth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def sixth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )

@client.command()    
async def seventh(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def eighth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

@client.command()    
async def ninth(ctx ):
    a = random.choice(['win','lose','win','lose'])
    await ctx.send( a )
    if a == 'win':
        await ctx.send( "if you want continue, write -nextlvls")
    if a == 'lose':
        await ctx.send( "Game over" )
        fin = random.choice(['lucky next time','try again','loser','hahaha'])
        await ctx.send( fin )

 
        
        
@client.command()
async def nextlvls(ctx ):
  
    emg = discord.Embed( title = f'1      2     3\n4     5     6     \n7     8     9', colour = discord.Color.red() )
    await ctx.send( embed = emg )  


#reactions
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 707908027524841522: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '1️⃣': # Emoji для реакций
            role = guild.get_role(707872645856755752) # ID Ролей для выдачи
        elif str(payload.emoji) == '2️⃣':
            role = guild.get_role(707912296328069130)
        
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)


@client.command() # Попытки 5
async def угадайка(ctx):
    await ctx.message.delete()
    num = random.randint(1, 20)
    attems = 1
    msg = await ctx.send('Подождите...')
    while attems < 6:
        emb = discord.Embed(
            title = f'Попытка №{attems}',
            description= 'Угадайте число от 1 до 20'
        )
        await msg.edit(content= None, embed=emb)
        try:
            msg_o = await  client.wait_for('message', timeout= 30.0, check= lambda msg_o: msg_o.author == ctx.author)
        except asyncio.TimeoutError:
            await msg.edit(content= 'Время вышло!', embed=None)
            break
        else:
            if num == int(msg_o.content):
                emb1 = discord.Embed(
                    title= 'Вы победили!',
                    description= 'Вы угадали число!'
                )
                await msg_o.delete()
                await msg.edit(content= None, embed=emb1)
                break
            else:
                attems_h = 5 - attems
                attems = attems + 1
                if attems == 6:
                    emb2 = discord.Embed(
                        title= 'Вы проиграли!',
                        description= f'Загаданое число было : {num}'
                    )
                    await msg_o.delete()
                    await msg.edit(embed=emb2)
                    break

                emb2 = discord.Embed(
                    title= 'Неудачная попытка!',
                    description= f'Вы не угадали число у вас осталось {attems_h} попыток'
                )
                await msg.edit(content= None, embed=emb2)
                await msg_o.delete() 
                await asyncio.sleep(2)






#search
@client.command()
async def search(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://www.bing.com/search?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Кое кто не умеет пользоваться поисковиками , я сделал это за него.\n{url}')

#youtube_search
@client.command()
async def youtube_search(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://www.youtube.com/results?search_query=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет ютубить , я сделал это за него.\n{url}')
#yandex
@client.command()
async def yandex(ctx, *, question):  # пояндексить
    # сам сайт
    url = 'https://yandex.ua/search/?lr=142&text=' + str(question).replace(' ', '%20')
    await ctx.send(f'Так как кое кто не умеет яндексить , я сделал это за него.\n{url}')
#wiki
@client.command(pass_context = True,aliases=['вики']) #!!wiki  !!вики
async def wiki( ctx,*, amount: str):

    if not amount:
        await ctx.send("Пожалуйста, используйте такую кострукцию: `!!wiki [вики запрос]`")
    a = '_'.join(amount.split())
    await ctx.send(f'https://ru.wikipedia.org/wiki/{a}')

#google
@client.command()
async def google(ctx, *, question):  # погуглить
    # сам сайт
    url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет гуглить , я сделал это за него.\n{url}')

#rps
@client.command()
async def rps(ctx, *, mess):
    robot = ['Камень', 'Ножницы', 'Бумага']
    if mess == "Камень" or mess == "К" or mess == "камень" or mess == "к":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Ножницы':
            emb.add_field(name = ':scroll:', value = 'Вы выиграли!')
        elif robot_choice == 'Бумага':
            emb.add_field(name = ':scissors:', value = 'Вы проиграли :с')
        else:
            emb.add_field(name = ':moyai:', value = 'Ничья!')
        await ctx.send(embed = emb)

    elif mess == "Бумага" or mess == "Б" or mess == "бумага" or mess == "б":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Ножницы':
            emb.add_field(name = ':scroll:', value = 'Вы проиграли :с')
        elif robot_choice == 'Камень':
            emb.add_field(name = ':moyai:', value = 'Вы выиграли!')
        else:
            emb.add_field(name = ':scissors:', value = 'Ничья!')
        await ctx.send(embed = emb)
            
    elif mess == "Ножницы" or mess == "Н" or mess == "ножницы" or mess == "н":
        robot_choice = random.choice(robot)
        emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
        if robot_choice == 'Бумага':
            emb.add_field(name = ':scissors:', value = 'Вы выиграли!')
        elif robot_choice == 'Камень':
            emb.add_field(name = ':moyai:', value = 'Вы проиграли :с')
        else:
            emb.add_field(name = ':scroll:', value = 'Ничья!')
        await ctx.send(embed = emb)









#botinfo
@client.command( pass_context = True )


async def botinfo( ctx ):
    await ctx.channel.purge( limit = 1 )
    emt = discord.Embed(title=f"{ctx.guild.name}", description="Информация о боте **NITAGAS bot**.\n Бот был написан специально для проекта Nitagas,\n подробнее о командах  -help", color = 000000)
    emt.add_field(name=f'**Меня создал:**', value="Stanislav", inline=True)  # Создает строку
    emt.add_field(name=f'**Помощь в создании:**', value="---", inline=True)  # Создает строку
    emt.add_field(name=f'**Лицензия:**', value="Nitagas", inline=True)  # Создает строку
    emt.add_field(name=f'**Я написан на:**', value="Discord.py", inline=True)  # Создает строку
    emt.add_field(name=f'**Версия:**', value="1.0", inline=True)  # Создает строку
    emt.add_field(name=f'**Патч:**', value="1.0", inline=True)  # Создает строку
    emt.set_footer(text=f"© Copyright 2020 Stanislav | Все права защищены")  # создаение футера
    await ctx.send(embed=emt)


#tmute
@client.command()
@commands.has_permissions( administrator = True )
async def tmute(ctx, member: discord.Member):
    await member.edit(mute=True)



ev_player = [''] #игроки в розыгрыше
start_ev = 0 #перемычка



#event roles
@client.command()
@commands.has_permissions( administrator = True )
async def event_roles(сtx, role: discord.Role = None, member: discord.Member = None):
    global ev_player
    global start_ev
    general = client.get_channel(705461507953262793)
    if role is None:
        await ctx.send('**Упомяните роль для розыгрыша.**' '\n' '`-event_roles [role]`')
        return
    ev_role = role
    start_ev = 1
    await general.send(f'Технический администратор запустил розыгрыш роли {role.mention}. Для участия пропишите `-участвую`.' '\n' f'**Розыгрыш состоится через 2 минуты.**')
    await asyncio.sleep(120)
    ev_win = r.choice(ev_player)
    member = ev_win
    await general.send(f'**Поздравляем {ev_win.mention}! Он выигрывает в розыгрыше и получает роль {role.mention}.**')
    await ev_win.add_roles(role)
    ev_player = ['']
    start_ev = 0


@client.command( pass_context = True )


async def участвую( ctx ):
    global ev_player
    global start_ev
    author = ctx.message.author
    if start_ev == 0:
        await ctx.send('**Сейчас нету розыгрыша ролей!**')
        return
    if author in ev_player:
        await ctx.send('Вы уже приняли участие в этом розыгрыше!')
        return
    else:
        ev_player.append(author)
        print(f'Игрок {author} принял участие в розыгрыши роли.')
        await сtx.send(embed = discord.Embed(description = f'**{author.mention}, Вы успешно приняли участие в розыгрыши роли!**', color = 0xee3131))
        print('Розыгрыш роли завершен.')



       
@client.command()

async def emoji(ctx,id:int,reaction:str):
        await ctx.message.delete()
        message = await ctx.message.channel.fetch_message(id)
        await message.add_reaction(reaction)



@client.command()
async def kill(  ctx, member: discord.Member ):
    await ctx.send( f"{ctx.author.mention} Достает дробовик... \n https://tenor.com/view/eyebrow-raise-smile-prepared-ready-loaded-gif-15793001" )
    await asyncio.sleep( 3 )
    await ctx.send( f"{ctx.author.mention} Направляет дробовик на {member.mention}... \n https://tenor.com/view/aim-point-gun-prepared-locked-and-loaded-gif-15793489" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{ctx.author.mention} Стреляет в {member.mention}... \n https://media.discordapp.net/attachments/690222948283580435/701494203607416943/tenor_3.gif" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{member.mention} истекает кровью..." )
    await asyncio.sleep( 3 )
    await ctx.send( f"{member.mention} погиб..." )




#tempban
@client.command()
@commands.has_permissions( administrator = True )
async def tempban(ctx, member : discord.Member, time:int, arg:str, *, reason=None):
    if member == ctx.message.author:
        return await ctx.send("Ты не можешь забанить сам себя.")
    msgg =  f'Пользователь : {member}, забанен по причине : {reason}.'
    msgdm = f'Вы были забанены на сервере {ctx.guild.name}, по причине : {reason}.'
    if reason == None:
        msgdm = f'Вы были забанены на сервере : {ctx.guild.name}.'
    if reason == None:
        msgg =  f'Пользователь : {member}, забанен.'
    await ctx.send(msgg)  
    await member.send(msgdm)
    await ctx.guild.ban(member, reason=reason)
    if arg == "s":
        await asyncio.sleep(time)          
    elif arg == "m":
        await asyncio.sleep(time * 60)
    elif arg == "h":
        await asyncio.sleep(time * 60 * 60)
    elif arg == "d":
        await asyncio.sleep(time * 60 * 60 * 24)
    await member.unban()
    await ctx.send(f'Пользователь : {member}, разбанен.')
    await member.send(f'Вы были разбанены на сервере : {ctx.guild.name}')




#temp_add_role
@client.command()
@commands.has_permissions(administrator = True)
async def temp_add_role(ctx, amount : int, member: discord.Member = None, role: discord.Role = None):

    try:

        if member is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

        elif role is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: роль!**'))

        else:

            await discord.Member.add_roles(member, role)
            await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана на {amount} секунд!**'))
            await asyncio.sleep(amount)
            await discord.Member.remove_roles(member, role)

    except:
        
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: Не удалось выдать роль.**', color=0x0c0c0c))

@client.command()
@commands.has_permissions(administrator = True)
async def add_role(ctx, member: discord.Member = None, role: discord.Role = None):

    try:

        if member is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

        elif role is None:

            await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: роль!**'))

        else:

            await discord.Member.add_roles(member, role)
            await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана**'))

    except:
        
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: Не удалось выдать роль.**', color=0x0c0c0c))

#tempmute
@client.command()
@commands.has_permissions( administrator = True )
async def tempmute(ctx,amount : int,member: discord.Member = None, reason = None):
    mutee_role = discord.utils.get(member.guild.roles, id = 705745998550401054) #Айди роли
    channel_log = client.get_channel(705461507953262793) #Айди канала логов

    await member.add_roles( mutee_role )
    await ctx.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был ограничен доступ к чатам.\n:book: По причине: {reason}**', color=0x0c0c0c)) 
    await channel_log.send(embed = discord.Embed(description = f'**:shield: Пользователю {member.mention} был ограничен доступ к чатам.\n:book: По причине: {reason}**', color=0x0c0c0c))
    await asyncio.sleep(amount)
    await member.remove_roles( mutee_role )   

# Работа с ошибками мута на время

@tempmute.error 
async def tempmute_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**', color=0x0c0c0c))


#ping
@client.command() 
async def ping(ctx):
    await ctx.send(embed = discord.Embed(description = f'**:gear: Ваш пинг:** { randint( 15, 200 ) }', color=0x0c0c0c))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))




@client.command()
async def math( ctx, a : int, arg, b : int ):

    try:

        if arg == '+':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a + b }', color=0x0c0c0c))  

        elif arg == '-':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a - b }', color=0x0c0c0c))  

        elif arg == '/':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a / b }', color=0x0c0c0c))

        elif arg == '*':
            await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a * b }', color=0x0c0c0c))      

    except:
        
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: Произошла ошибка.**', color=0x0c0c0c))






@client.command()
@commands.has_permissions(administrator = True)
async def voice_create(ctx, *, arg): 
    guild = ctx.guild
    channel = await guild.create_voice_channel(f'{arg}')
    await ctx.send(embed = discord.Embed(description = f'**:microphone2: Голосовой канал "{arg}" успешно создан!**', color=0x0c0c0c))

@client.command()
@commands.has_permissions(administrator = True)
async def channel_create(ctx, *, arg): 
    guild = ctx.guild
    channel = await guild.create_text_channel(f'{arg}')
    await ctx.send(embed = discord.Embed(description = f'**:keyboard: Текстовый канал "{arg}" успешно создан!**', color=0x0c0c0c))



@client.command()
async def avatar(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

# userinfo
@client.command()
async def userinfo(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"Имя: {Member.name}\n\n"
                                                                                      f"Никнейм: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Высшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command()
@commands.has_permissions(administrator = True)
async def changing_name(ctx, member: discord.Member = None, nickname: str = None):
    await ctx.send('Info')
    try:
        if member is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите **пользователя**!"))
        elif nickname is None:
            await ctx.send(embed = discord.Embed(description = "Обязательно укажите ник!"))
        else:
            await member.edit(nick = nickname)
            await ctx.send(embed = discord.Embed(description = f"У пользователя **{member.name}** был изменен ник на **{nickname}**"))
    except:
        await ctx.send(embed = discord.Embed(description = f"Я не могу изменить ник пользователя **{member.name}**!"))

#suggest
@client.command( pass_context = True, aliases = [ "Предложить", "предложить", "предложка", "Предложка", "Suggest" ])

async def suggest( ctx , * , agr ):
    suggest_chanell = client.get_channel( 705461507953262793 ) #Айди канала предложки
    embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {agr} \n\n")

    embed.set_thumbnail(url=ctx.guild.icon_url)

    message = await suggest_chanell.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@client.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":black_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)


@client.command()
async def covid(ctx):   
    await ctx.send(f'https://www.worldometers.info/coronavirus/') 
   
   
token= os.environ.get('BOT_TOKEN')
client.run( token )
