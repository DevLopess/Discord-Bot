#Canal de logs : 1259584910365298719

# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
import json


LOGS_CHANNEL_ID = 1259584910365298719

#Load the Bot token

#Dont place the directly in the code!!!

with open("C:/Users/PC/Documents/BinBot/TOKEN.json","r") as file:
    info_json = json.load(file)
    BOT_TOKEN = info_json["token"]
    print(BOT_TOKEN)

list = []

bot = commands.Bot(command_prefix = "!", intents =  discord.Intents.all())


@bot.event
async def on_ready():
    logs_channel = bot.get_channel(LOGS_CHANNEL_ID)
    print("Hello! BinBot ready!")
    await logs_channel.send("BinBot ready")
    

@bot.event
async def on_member_update(old,new):
    logs_channel = bot.get_channel(LOGS_CHANNEL_ID)
    print("Old name: " + old.display_name)
    print("New name: " + new.display_name)
    
    await logs_channel.send("O utilizador " + old.display_name + "alterou o seu nome para " + new.display_name)
    await logs_channel.send(new.display_avatar)
    
    

@bot.command()
async def add_list(ctx,x):
    list.append(x)

@bot.command()
async def show_list(ctx):
    
    await ctx.send(list)

@bot.command()
async def add(ctx,x,y):
    result = int(x) + int(y)
    await ctx.send(result)



bot.run(BOT_TOKEN)