import discord
import time
import datetime
Client = discord.Client()
@Client.event   
async def on_ready():
    print("Connected")
    streaming=discord.Streaming(name="Sinje qui tourne by Elchagnon", url="https://www.sinje.com")
    await Client.change_presence(activity=streaming)
@Client.event
async def on_message(message):
    x=0
    if message.author == Client.user:   
        return
    if message.content == "monkey":
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""Sinje""")
        await Client.change_presence(activity=game)
        while x < 1:
            await message.channel.send("https://tenor.com/view/look-back-monkey-mask-monkey-busted-blake-webber-gif-11941099")
            x=x+1
        else:
            return
Client.run("Ton Token")
