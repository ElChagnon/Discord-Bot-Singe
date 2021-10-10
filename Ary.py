import discord
import time
import datetime
Client = discord.Client()
@Client.event   
async def on_ready():
    print("Connected")
    streaming=discord.Streaming(name="sinje qui tourne", url="https://www.sinje.com")
    await Client.change_presence(activity=streaming)
@Client.event
async def on_message(message):
    x=0
    if message.author == Client.user:   
        return
    if message.content == "<@413423609122390016>":
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""Sinje""")
        await Client.change_presence(activity=game)
        while x < 1:
            await message.channel.send("https://rule34.xxx/images/584/37f6b6c6c6cf359952a84576890d8f07105af560.jpg")
            x=x+1
        else:
            return
Client.run("Ton Token")
