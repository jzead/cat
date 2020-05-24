import discord
import random
import os

client = discord.Client()
a = "반가워"
b = "반가워 아마도..."
c = "누구세요?"
A = "놀아줄까?"
B = "물고기 잡고있다냥"
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("온라인")
@client.event
async def on_message(message):

    if message.content.startswith(";;get up"):
        await client.change_presence(status=discord.Status.online)

    if message.content.startswith(";;sleep"):
        await client.change_presence(status=discord.Status.offline)

    if message.content.startswith("뭐해"):
        await message.channel.send(B)

    if message.content.startswith("심심해"):
        await message.channel.send(A)

    if message.content.startswith("안녕"):
        d = random.randint(1,3)
        if d == 1:
            await message.channel.send(a)
        if d == 2:
            await message.channel.send(b)
        if d == 3:
            await message.channel.send(c)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)