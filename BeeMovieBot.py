import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event #make first event
async def on_ready(): #when bot is ready
    beecount = 0
    print('im here beecase you need me')
@client.event
async def on_member_join(member):
    print(member + ' Beelieves!!')
@client.event
async def on_member_remove(member):
    print(member + ' does not Beelieve anymore')

@client.command()
async def beeHelp(ctx):
    await ctx.send('Bee has come to help you!\n List of commands:\n 1. bee\n2. sp33d \n3. beefortune')
@client.command()
async def beecount(ctx):
    await ctx.send('Bees: ' + str(beecount))
@client.command()
async def sp33d(ctx):
    await ctx.send(str(client.latency*1000) + 'ms')
@client.command(aliases = ['fortune', 'tarot'])
async def beefortune(ctx):
    resp = ['mayBee', 'Beecareful', 'No', 'Without a Bee!', 'Yes!', 'The Bee reckons it', 'Bee thinks yes', '\'Try again later\', says Bee']
    await ctx.send(random.choice(resp))

@client.event
async def on_message(message):
    words = message.content.split()
    if message.author == client.user:
        return
    
    #people mentions
    for word in words:
        if word.lower()=="child":
            await message.channel.send('<@NUMERIC_ID>')
   
    #bee spam
    if (message.content).lower() == 'bee': %could be changed to 'bee' in words
        aScript = open('script.txt')
        for x in aScript:
            try:
                await message.channel.send(x)
            except:
                continue
        beecount = beecount+1
        aScript.close()
       
    if (message.content).lower() == 'beee':
        aScript = open('script.txt')
        for x in aScript:
            a = x.split()
            for y in a:
                try:
                    await message.channel.send(y)
                except:
                    continue
        beecount = beecount+1
        aScript.close()
        
    if (message.content).lower() == 'b33':
        aScript = open('script.txt')
        for x in aScript:
            a = x.split()
            for y in a:
                try:
                    await message.channel.send(y.upper())
                except:
                    continue
        beecount = beecount+1
        aScript.close()
    
    #Bee QnA
    for i in message.content:
        if i == '?':
            resp = ['mayBee', 'Beecareful', 'No', 'Without a Bee!', 'Yes!', 'The Bee reckons it', 'Bee thinks yes', '\'Try again later\', says Bee']
            await message.channel.send(random.choice(resp))
            continue
        
            
client.run('NzA5NTAyNTUyNTI5NDM2NzQ0.XrnwrQ.RSRT4JZ8UF2g5fH0mUqC6gidl-g') #my bot ID is in the string
