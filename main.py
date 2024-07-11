#Canal de logs : 1259584910365298719

# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
import json


LOGS_CHANNEL_ID = 1259584910365298719


class SimpleView(discord.ui.View):

    @discord.ui.button(label="SHOOOOT",style=discord.ButtonStyle.danger)
    async def shot(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.channel.send(interaction.user.mention + " was the fastest!!!")
        button.disabled=True
        await interaction.response.edit_message(view=self)
        self.stop()

#Load the Bot token

#Dont place the directly in the code!!!

with open("C:/Users/PC/Documents/BinBot/TOKEN.json","r") as file:
    info_json = json.load(file)
    BOT_TOKEN = info_json["token"]
    print(BOT_TOKEN)

list = []

bot = commands.Bot(command_prefix = "/", intents =  discord.Intents.all())


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
    

# This event is mainly used for logging:
# A user gets disconnected

@bot.event
async def on_voice_state_update(member,before,after):
    if before.channel is not None and after.channel is None:
        guild = member.guild
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.member_disconnect):
            
            if entry.user.id != member.id : 
                kicker = entry.user
                logs_channel = bot.get_channel(LOGS_CHANNEL_ID)
                if logs_channel:
                    await logs_channel.send(f'{kicker.mention} expulsou {member.mention} do canal de voz {before.channel.name}')
                break

@bot.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")


#This command is called to start the minigame duel 
#The minigame is based on the duel off old cowboys,
#It will create a separate text room for the two players and past a random time it will send an embed mensage with a button and the first person to click wins

@bot.command()
async def duel(ctx):
    view = SimpleView()
    await ctx.send(view=view)


bot.run(BOT_TOKEN)