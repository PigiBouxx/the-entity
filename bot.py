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

with open('perks_killer.txt','r',encoding="ISO-8859-1") as fe:
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
    if message.author == client.user:
        return
        
    elif message.content == "!survivor":
        a = choice(survivant)
        await client.send_file(message.channel, ("dea/"+a))      
    elif message.content == "!killer":
        b = choice(tueur)
        await client.send_file(message.channel,("tueur/"+b))
        await client.change_presence(game=discord.Game(name='SALUT'))
    elif message.content == "!survivorperk":
        for i in range(4):
            x = cperks()
            await client.send_message(message.channel,x)
    elif message.content == "!killerperk":
        for i in range(4):
            x = cperkt()
            await client.send_message(message.channel,x)
@client.event
async def on_ready():
    print('log:',client.user.name)
    await client.change_presence(game=discord.Game(name='@zDeltas'))

client.run(os.getenv('TOKEN'))
