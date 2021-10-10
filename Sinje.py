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
    if message.content == "sinje":
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""Sinje""")
        await Client.change_presence(activity=game)
        while x < 1:
            await message.channel.send("https://cdn.discordapp.com/attachments/873547672328495215/877240044274999306/Je0eRnta.jpg")
            x=x+1
        else:
            return
Client.run("ODc1ODUwOTIzNTAxNTYzOTA0.YRbhvA.M2FHOBt60ICTIZUWCH9qe3RFrBo")
