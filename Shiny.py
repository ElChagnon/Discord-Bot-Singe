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
    if message.content == "shiny":
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""Sinje""")
        await Client.change_presence(activity=game)
        while x < 2:
            await message.channel.send("https://rule34.xxx/images/4318/a0d67fa191af4bb69489f35fb04d32d7b96c6952.jpg")
            x=x+1
        else:
            return
Client.run("ODc1ODUwOTIzNTAxNTYzOTA0.YRbhvA.M2FHOBt60ICTIZUWCH9qe3RFrBo")
