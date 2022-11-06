import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import datetime

load_dotenv()
intents = discord.Intents.all()
intents.members = True
#Set ur bot prefix
bot = commands.Bot(command_prefix='!', intents=intents)
#to remove by default help prefix from ur bot
bot.remove_command('help')

#getting date and month of the giveaway
x = datetime.datetime.now()
month = x.strftime("%B")
year = x.strftime("%Y")

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


 
@bot.command(pass_context=True)
async def lucky(ctx, rolename):
#getting participant on a rolename of ur actual server and choosing one of them randomly
	for guild in bot.guilds:
		for row in guild.roles:
			if row.name == rolename:
				roleid = row.id
				role = guild.get_role(roleid)
				participant = role.members
				guildname = role.guild.name
				names = []        
				for row in participant:
					names.append(row.name)    
        			Winner = random.choice(names)
				for row2 in participant:
					if row2.name == Winner:
						Wid = row2.id
						user = await ctx.bot.fetch_user(Wid)
						avatar = user.avatar_url
      
  #building discord core message
	embed = discord.Embed(color=0x5e0303)
	embed.set_author(
	    name="Monthly Giveaway of  " + guildname,
	    icon_url="Icon url"
	)
	embed.add_field(name="List of Participant:",
	                value=', '.join(names),
	                inline=True)
	embed.add_field(name="Winner of the Giveaway this month " + month + "/" +
	                year + " is : ",
	                value="🤴 " + "<@" + str(Wid) + ">",
	                inline=False)
	embed.add_field(name="Check here the winner ",
	                value="<@&" + str(roleid) + ">",
	                inline=False)
	embed.set_footer(text="🎉 😎 ✨🥳 We are pleased u won This Month  ",
	                 icon_url=avatar)
	await ctx.send(embed=embed)

#sending discord message to show help commands
@bot.command(pass_context=True)
async def lhelp(ctx):
	embed = discord.Embed(title="How to use little Lucky <3",
	                      description="Commands help",
	                      color=0x00ff00)
	embed.add_field(name="lhelp",
	                value="Show u available commands",
	                inline=False)
	embed.add_field(
	    name=
	    "lucky nameofrole, where namerole groupe that u want to do the giveaway in",
	    value="Launch the draw of the giveaway",
	    inline=True)
	await ctx.send(embed=embed)

#raise an exception if no rolename was given.
@lucky.error
async def tenor_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(
		    'Rolename missing, use command lhelp to get all available commands'
		)
	else:
		raise error

#change it with ur token discord, keep it secret :)
bot.run(os.getenv('DISCORD_TOKEN'))
