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
import ffmpeg
import PyNaCl


client = commands.Bot( command_prefix = '-')
client.remove_command('help')
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
#



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


 
token= os.environ.get('BOT_TOKEN')
client.run( token )
