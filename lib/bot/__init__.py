from asyncio import sleep
import asyncio
from collections import UserString
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from discord import member
from discord.ext import commands
from glob import glob
import time
import json
import os
from discord.ext.commands.converter import EmojiConverter
from discord.ext.commands.cooldowns import BucketType
from datetime import datetime


PREFIX = "r!"
OWNER_IDS = [715340764485517442]
# COGS = [path.split("\\")[-1][:-3] for path in glob(r"C:\Users\New uSer\Documents\GitHub\Super Rocket Bot\lib\cogs\*.py")]


bot = commands.Bot(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=discord.Intents.all(), activity=discord.Game(name="CC Hackathon Final | r!help"), help_command=None)

# with open(r"C:\Users\New uSer\Documents\GitHub\Super Rocket Bot\lib\bot\token.0", "r", encoding="utf-8") as tf: 
#     TOKEN = tf.read() # Gets the bot token
TOKEN = '#TOKEN'

snipe_message_author = ""
snipe_message_content = ""



@bot.event 
async def on_ready(): # this function gets called when the bot is ready
    print('Up and Running!')
   # guild = bot.get_guild(773961433188401183) 
    #stdout = guild.get_channel(775112917229895731)
    #scheduler.add_job(rules_reminder, CronTrigger(minute=1, second=0)) # Calls "rule_reminder" every minute
    # scheduler.start()
    
#async def rules_reminder(self):
 #  guild = bot.get_guild(773961433188401183)
  # stdout = guild.get_channel(775112917229895731)
  # await stdout.send("Remember to adhere to the rules!")

@bot.command()
async def help(ctx):
    await ctx.send("Hello whoever run this command! To learn about the bot and commands, use `r!about`")

@bot.command()
async def about(ctx):
    embed = discord.Embed(title=":information_source: About Super Rocket Bot", description="We have one of the best bots on the planet!", color=0x0EBFE9)
    embed.add_field(name="What about me?", value= 'Super Rocket Bot, is made by `Audit Baansal#1234`, `Super Rocket.py#3804`, `Penguin Master#2263`. ')
    embed.add_field(name="What else?", value="Super Rocket Bot is a bot currently still under development but has some epic commands. For more info, type `r!chelp`")
    await ctx.send(embed=embed)

@bot.command()
async def chelp(ctx):
    embed = discord.Embed(title="Super Rocket Bot Command List", description="We have some epic commands!", color=0x0EBFE9)
    embed.add_field(name= ':tools: Moderation', value = '`r!modhelp`')
    embed.add_field(name= ':smiley: Fun', value = '`r!funhelp`')
    embed.add_field(name= ':laughing: Triggers', value = '`r!triggers`')
    embed.add_field(name= ':file_folder: Miscellanious', value= '`r!misc`')
    embed.add_field(name=":moneybag: Currency", value='`r!currency`')
    await ctx.send(embed=embed) 

#-------------------------------------------------------------------------------------Moderation------------------------------------------------------------------------------------

@bot.command()
async def modhelp(ctx):
    embed = discord.Embed(title="Moderation Commands", description="These are the Moderation Commands of Super Rocket Bot", color=0x0EBFE9)
    embed.add_field(name = "Moderation Commands", value="`r!ban <@member> [reason]` - Bans a member\n `r!kick <@member> [reason]` - Kicks a member\n `r!invite` - Shows the permamanent invite link to the server\n `r!emojis` - Spams all the emojis in the server\n `r!mute`  - Mutes a Member\n `r!unmute`  - Unmutes a member\n `r!delete[Messages]` - Deletes the amount of messages assigned\n  `r!warn[Member]`  - Warns A Member\n `r!addrole [Member][Role]`  - Adds a Role To A Member\n `r!removerole [Member][Role]`  - Removes a Role From A Member\n `r!tempban[Member][Duration]`  - Temporarily Bans A Member For A Chosen Time\n `r!setslowmode[time]`  - Set The Slowmode of a Channel")
    await ctx.send(embed=embed)

@bot.command() #nwhen creating a new command, this is what you use
@commands.has_permissions(administrator=True) # checks if user has admin perms
async def ban(ctx, member: discord.Member, *reason): # the name of the function is the name of the command. So the name of the command is "ban".
    if member.guild_permissions.administrator: #checks if the member you want to ban has admin perms
        return await ctx.send('<a:BONK:776844927371313183>''That member has the Administrator permission, and you know that. So no thank you.')
    shown_reason = ""
    for word in reason:
        shown_reason += f'{word} ' # the reason will be multiple words, so it will be in a tuple. We don't want it to be in a tuple, but we want it to be in a sentence so thats what "shown_reason" is
    if len(reason) == 0:
        shown_reason = 'No reason provided'
    embed = discord.Embed(name="You Were Banned From Around The Globe", description=f"You were banned from {ctx.guild.name} for {shown_reason}", color=0x0EBFE9, inline=True)
    embed.add_field(name="Appeal", description="If you would like to appeal, go to https://forms.gle/qABWJa3ijvQSc3aG8 .") 
    await member.ban() # Ultimatley Bans the Member
    await member.send(embed=embed)  
    await ctx.send(f'Successfully banned {member.mention} for {shown_reason}!')

@bot.command()
@commands.has_permissions(administrator=True) # checks if user has admin perms
async def kick(ctx, member: discord.Member, *reason): # the name of the function is the name of the command. So the name of the command is "kick".
    if member.guild_permissions.administrator: #checks if the member you want to kick has admin perms
        return await ctx.send('<a:BONK:776844927371313183>''Sorry, that perms has the **ADMINISTRATOR** permissions, and you know that. No thank you.')
    shown_reason = ""
    for word in reason:
        shown_reason += f'{word} ' # the reason will be multiple words, so it will be in a tuple. We don't want it to be in a tuple, but we want it to be in a sentence so thats what "shown_reason" is
    if len(reason) == 0:
        shown_reason = 'No reason provided'
        await member.kick() # Ultimately Kicks the Member
        await ctx.send(f'Successfully kicked {member.mention} for {shown_reason}!')

@bot.command() 
@commands.has_permissions(administrator = True)
async def emojis(ctx):
    for emoji in ctx.guild.emojis:
        await ctx.send(emoji) 

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Successfully gave role \"{role.name}\" to {user.name}")

@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"Successfully removed role \"{role.name}\" from {user.name}")

@bot.command()
@commands.has_permissions(manage_guild=True) 
async def mute(ctx, member: discord.Member):
    role = ctx.guild.get_role(773961433499172879)
    await member.add_roles(role)
    await ctx.send(f'I muted {member.mention}!')

@bot.command()
@commands.has_permissions(manage_guild=True)
async def unmute(ctx, member: discord.Member):
    role = ctx.guild.get_role(773961433499172879)
    await member.remove_roles(role)
    await ctx.send(f'I unmuted {member.mention}!')

@bot.command(pass_context=True)
@commands.has_permissions(manage_guild=True)
async def tempban(ctx,member:discord.Member,days=1):
    if not member.guild_permissions.manage_guild:
        await member.ban(delete_message_days=0)
        await ctx.send('User banned for **'+str(days)+' day(s)**') 
        ban_list.append(member)
        day_list.append(days*24*60*60)
        server_list.append(ctx.guild)
    else:
        await ctx.send('<a:BONK:776844927371313183>''They have manage guild perms so you cant ban them')

@bot.command() 
@commands.has_permissions(manage_guild=True)
async def warn(ctx, member: discord.Member, *reason):
    if member.guild_permissions.manage_guild and not ctx.author.guild_permissions.administrator:
        return await ctx.send('That member has the Manage Server permission, so you can\'t warn them!')
    with open('warns.json', 'r') as f:
        warns = json.load(f)
    user = member
    if not f'{user.id}' in warns:
        warns[f'{user.id}'] = {}
        warns[f'{user.id}']['warns'] = []
    shown_reason = ''
    for word in reason:
        shown_reason += f'{word} '
    if len(reason) == 0:
        shown_reason = 'No reason provided '
    while shown_reason in warns[f'{member.id}']['warns']:
        shown_reason += '.'
    warns[f'{user.id}']['warns'].append(shown_reason)
    await member.send(f'You were were warned in {ctx.guild.name} for {shown_reason}!')
    with open ('warns.json', 'w') as f:
        json.dump(warns, f)
    await ctx.send(f'{member.mention} was warned for {shown_reason}! ')

@bot.command()
@commands.has_permissions(manage_guild=True)
async def delwarn(ctx, member: discord.Member, id):
    if member.guild_permissions.manage_guild and ctx.author.guild_permissions.administrator:
        return await ctx.send('<a:BONK:776844927371313183>''That member has the Manage Server permission, so you can\'t delete their warn!')
    with open('warns.json', 'r') as f:
        warns = json.load(f) #hey Audit u here? or are you afk?
    if not f'{member.id}' in warns:
        warns[f'{member.id}'] = {}
        warns[f'{member.id}']['warns'] = []

    if warns[f'{member.id}']['warns'][id]:
        warns[f'{member.id}']['warns'].pop(id)
        with open('warns.json', 'w') as f:
            json.dump(warns, f)
        return await ctx.send(f'Succesfully deleted warn for {member.mention} with the id of `{id}`!')
    else:
        print('b')
        return await ctx.send(f'Warn doesn\'t exist for {member.mention} with the id of `{id}`')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def delete(ctx, messages):
    messages = int(messages)
    await ctx.channel.purge(limit=messages)
    msg = await ctx.send(f'I deleted {messages} messages!')
    time.sleep(5)
    await msg.delete()

@bot.command()
async def currency(ctx):
    embed = discord.Embed(title="Currency Commands", description="These are the Currency Commands in Super Rocket Bot", color=0x0EBFE9)
    embed.add_field(name="Currency Commands", value="`r!register`  - Registers you in the currency system\n `r!bal`  - View Your Balance\n `r!transfer[Amount][Member]`  - Give Your Coins to another person\n `r!daily`  - Earn Your Daily Coins\n `r!hourly`  - Earn Your Hourly Coins\n `r!work`  - Work Per Hour For 1000 Coins\n `r!beg`  - Recieve 350 Coins From Audit Baansal\n `r!search`  - Search For Coins lying on the ground!\n `r!hunt`  - Hunt in the forest and get some coins!\n `r!fish`  - Fish in a river filled with fish!") 
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def register(ctx):
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    id = str(ctx.author.id)
    if id not in amounts:
        amounts[id] = 100
        await ctx.send("You are now registered")
        with open('amounts.json', 'w') as f:
            amounts = json.dump(amounts, f)
    else:
        await ctx.send("You already have an account")

@bot.command(pass_context=True)
async def bal (ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        await ctx.send("You have {} coins in the bank :moneybag:".format(amounts[id]))
    else:
        await ctx.send("You do not have an account")

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    id = str(ctx.author.id) #ok
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 5000
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    embed = discord.Embed(title=f"Here are is your daily award, {ctx.author.name}", description="**5,000 coins** were placed in your balance!")
    embed.set_footer(text='You can claim this reward again tomorrow!')
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, e):
    embed = discord.Embed(name="Error", description=f'There was an error: {e}', color=0x0EBFE9)
    embed.set_footer(text="Please Notify A Developer For Help")
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 1000
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("`LETS GOOO` You Worked Really Well! 1000 Coins Are In Your Balance!")

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def hourly(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 500
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    embed = discord.Embed(title=f"Here is your hourly award, {ctx.author.name}", description="**500 coins** were placed in your balance!")
    embed.set_footer(text='You can claim this reward again in an hour!')
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 350
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("Audit Baansal Donated 350 Coins!")

@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def search(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 400
    else: 
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("You searched around and found 400 Coins lying on the ground! They're now in your balance!")


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def hunt(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 250
    else: 
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("You shot a deer's wallet and found 250 Coins!")


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def fish(ctx):
    id = str(ctx.author.id)
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id] += 300
    else: 
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('amounts.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("You dropped down your fishing rod into a river and found 300 coins in the river bed! They're now in your balance!")



@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    with open('amounts.json', 'r') as f:
        amounts = json.load(f)
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.send("The other person does not have an account")
    elif amounts[primary_id] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("Transaction complete")
    with open('amounts.json', 'w') as f:
        amounts = json.dump(amounts, f)

@bot.command()
async def funhelp(ctx):
    embed = discord.Embed(title="Fun Commands", description="These are the Fun Commands of Super Rocket Bot", color=0x0EBFE9)
    embed.add_field(name = "Fun Commands", value = '`r!distract`  - Makes you distracted by Henry Stickmin\n `r!ping`  - Shows the ping/latency of the bot\n `r!logo`  - Shows the ATG Logo\n `r!snipe`  - Snipes the most recent deleted message\n ')
    await ctx.send(embed=embed)

@bot.command()
async def snipe(ctx):
    if snipe_message_content=="": #yeah
       await ctx.send("There\'s nothing to snipe.")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}", color=0x0EBFE9)
        embed.set_footer(text=f"Sniped by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url, )
        embed.set_author(name= f"")
        await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    ping = round(bot.latency*1000)
    await ctx.send(f':ping_pong:' f"Pong! {str(ping)}ms") 

async def countdown():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await asyncio.sleep(1)
        day_list[:]=[x-1 for x in day_list]
        for day in day_list:
            if day<=0:
                try:
                    await bot.unban(server_list[day_list.index(day)],ban_list[day_list.index(day)])
                except:
                    print('Error! User already unbanned!')
                del ban_list[day_list.index(day)]
                del server_list[day_list.index(day)]
                del day_list[day_list.index(day)]
@bot.command()
async def distract(ctx):
    await ctx.send('<a:HenryStickminDance:774347966395318303>') #always have an a after the < (for custom emojis), and make sure you have the right ID

@bot.command()
async def logo(ctx):
    await ctx.send('<a:ATGLogo:774075081554133022>')

@bot.command()
async def misc(ctx):
    embed = discord.Embed(title="Miscellanious Commands", description="These are some miscellanious commands of Super Rocket Bot", color=0x0EBFE9)
    embed.add_field(name="Miscellanious Commands", value='`r!dev`  - Shows The Owners/Developers Of Super Rocket Bot\n `r!owner`  - Shows The Owner Of The Server\n `r!invite`  - Shows The Permanent Server Invite\n `r!invites`  - Shows How Many Invites Have\n `r!dev`  - Shows The Developers Of Super Rocket Bot\n `r!timer[Seconds]`  - Starts a timer!\n `r!serverinfo`  - Shows This Server\'s Info\n `r!warnings`  - Shows How Many Warnings You Have')
    await ctx.send(embed=embed)

@bot.command() #nwhen creating a new command, this is what you use
async def invite(ctx): # the name of the function is the name of the command. So the name of the command is "ban".
    await ctx.send(f'This is Around The Globe permenant server invite: https://discord.gg/CzHeC7Yswy')

@bot.command()
async def dev(ctx):
    await ctx.send("The developers of Super Rocket Bot are `Audit Baansal#1234` and `Super Rocket.py#3804`, and `Penguin Master#2263` ")

@bot.command()
async def owner(ctx):
    await ctx.send("The Owner Of This Server is Super Rocket.py")

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(name="Server Info", description="**Around the Globe's** Information", color=0x0EBFE9, inline=True)
    embed.add_field(name="Owner", value="The Owner Of Around The Globe is **Super Rocket.py**", inline=False)
    embed.add_field(name="Member Count", value="This server has **41** Members", inline=False)
    embed.add_field(name="Emoji Count", value="This server has **100** emojis", inline=False)
    embed.add_field(name="Roles Count", value="This server had **83** Roles", inline = False)
    await ctx.send(embed=embed)

@bot.command()
async def triggers(ctx):
    embed = discord.Embed(title="Triggers", decription="These are the Triggers of Super Rocket Bot", color=0x0EBFE9)
    embed.add_field(name="Triggers", value='`yikes`\n`homework`\n`school`\n `blablabla`\n `abc`\n `audit`\n `lol`\n `triple lol`\n `bruh`\n `bye`\n `vs code`\n ' )
    await ctx.send(embed=embed)

@bot.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send("I dont think im allowed to do go above 300 seconds.")
            raise BaseException
        if secondint <= 0:
            await ctx.send("I dont think im allowed to do negatives")
            raise BaseException
        message = await ctx.send("Timer: {seconds}")
        while True:
            secondint -= 1
            if secondint == 0:
                await ctx.message.edit(content="Ended!")
                break
            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
    except ValueError:
        await ctx.send("Must be a number!")
        await ctx.message.delete()

@bot.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

@bot.command()
@commands.has_permissions(manage_channels = True)
async def setslowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")


@bot.command(pass_context=True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@bot.command()
async def warnings(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    with open('warns.json', 'r') as f:
        warns = json.load(f)
    try:
        warnings_list = warns[f'{member.id}']['warns']
    except Exception as e:
        pass
    warnings = ""
    if not f'{member.id}' in warns:
        warnings = 'None'
        warns[f'{member.id}'] = {}
        warns[f'{member.id}']['warns'] = []
    elif len(warnings_list):
        for warn in warnings_list:
            warnings += f'{warn} (id = {warnings_list.index(warn)}) \n' # ok
    else:
        warnings = "None"
    embed = discord.Embed(title=f'Warnings for {member.name}', color=0x0EBFE9)
    embed.add_field(name='Warnings:', value=f'{warnings}')
    await ctx.send(embed=embed)
    
@bot.event
async def on_guild_join(guild):
    guild_name = guild.name
    channel = bot.get_channel(774078494866407435)
    member_count = guild.member_count


@bot.event
async def on_message_delete(message):
    global snipe_message_author, snipe_message_content
    snipe_message_author = message.author.name
    snipe_message_content = message.content
    print('I got a deleted message!')

    bad_words = open('bad-words.txt').readlines()
    message_content = message.content.strip().lower()
    for bad_word in bad_words:
        bad_word = bad_word.replace('\n', '')
        if bad_word in message_content:
            await message.channel.send('<a:BONK:776844927371313183>'"{}, No bad words are allowed in Around The Globe. Next time it's a mute!  ".format(message.author.mention))
            await message.delete

    await bot.process_commands(message)

bot.run(TOKEN)
