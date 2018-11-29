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
tempList = []
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    elif message.content == "!survivor":
        a = choice(survivant)
        await client.send_file(message.channel,"Pour: "+message.author+("dea/"+a))      
    elif message.content == "!killer":
        b = choice(tueur)
        await client.send_file(message.channel,"Pour: "+message.author+("tueur/"+b))
    elif message.content == "!survivorperk":
        while 1:
            if len(tempList) < 4:
                x = cperks()
                if x in tempList:
                    pass
                else:
                    tempList.append(x)
                await client.send_message(message.channel,x)
        tempList = []
    elif message.content == "!killerperk":
        while 1:
            if len(tempList) < 4:
                x = cperkt()
                if x in tempList:
                    pass
                else:
                    tempList.append(x)
                await client.send_message(message.channel,x)
        tempList=[]
@client.event
async def on_ready():
    print('log:',client.user.name)
    await client.change_presence(game=discord.Game(name='Dead by Deadlight'))

client.run(os.getenv('TOKEN'))
