import discord
import os
import random
import time

client = discord.Client()
list =['ur name of people']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.content.startswith('!draw'):
      await message.channel.send("List of people on draw are : \n" )
      await message.channel.send('\n'.join(map(str, list)))
      await message.channel.send("Please wait draw is in process")
      time.sleep(10)
      await message.channel.send("######################Draw is over winner appear######################")
      Winner = random.choice(list)
      await message.channel.send("Congratulation you are the winner of the giveaway this month march <3, is Mr " + Winner)
      await message.channel.send("Can you provide us please your plateforme / Ios or Google? please " + Winner)

client.run(os.getenv('TOKEN'))
