import discord
import asyncio
from random import choice
import os


client = discord.Client()

tueur = []
survivant = []
perks = []
perkt = []

with open('perks_survivants.txt','r',encoding="ISO-8859-1") as f:
    t = f.readlines()
for i in t:
    a = i.replace('\n','')
    perks.append(a)

with open('perks_killer.txt','r',encoding="utf-8") as fe:
    t = fe.readlines()
for i in t:
    a = i.replace('\n','')
    perkt.append(a)

def cperks(): 
    l = choice(perks)
    return l
    
def cperkt(): 
    l = choice(perkt)
    return l
    
for i in os.listdir("dea"):
    survivant.append(i)
for t in os.listdir("tueur"):
    tueur.append(t)

print("tueur:",tueur)
print("survivant:",survivant)   
@client.event
async def on_message(message):
    tempList = []
    if message.author == client.user:
        return
    elif message.content == "!survivor":
        a = choice(survivant)
        await client.send_message(message.channel,message.author.mention)
        await client.send_file(message.channel,("dea/"+a))
    elif message.content == "!killer":
        b = choice(tueur)
        await client.send_message(message.channel,message.author.mention)
        await client.send_file(message.channel,("tueur/"+b))
    elif message.content == "!survivorperk":
        await client.send_message(message.channel,message.author.mention)
        while 1:
            if len(tempList) < 4:
                x = cperks()
                if x in tempList:
                    pass
                else:
                    tempList.append(x)
            else:
                break
        msg = ""
        for i in tempList:
            msg = i + ", " + msg
        await client.send_message(message.channel,msg)
        tempList=[]
    elif message.content == "!killerperk":
        await client.send_message(message.channel,message.author.mention)
        while 1:
            if len(tempList) < 4:
                x = cperkt()
                if x in tempList:
                    pass
                else:
                    tempList.append(x)
            else:
                break
        msg = ""
        for i in tempList:
            msg = i + ", " + msg
        await client.send_message(message.channel,msg)
        tempList=[]
@client.event
async def on_ready():
    print('log:',client.user.name)
    await client.change_presence(game=discord.Game(name='Dead by Daylight'))


client.run("NTE2MzQwMjMxNTA3NjczMDg4.DuHW4Q.pnkV5rZmNiqQrPGxJe8EuzdWZE8")
