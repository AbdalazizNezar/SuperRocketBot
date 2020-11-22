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
import random
from PIL import ImageFont, ImageDraw, Image
import requests
import datetime
import time
import re
from discord.utils import get
from discord.utils import find
from collections import OrderedDict
import sqlite3
import discord
from discord.ext import commands
import json
import atexit
import uuid




PREFIX = "r!"
OWNER_IDS = [715340764485517442]
# COGS = [path.split("\\")[-1][:-3] for path in glob(r"C:\Users\New uSer\Documents\GitHub\kSuperCarBot\lib\cogs\*.py")]


Value = False



ban_list = []
day_list = []
server_list = []
bot = commands.Bot(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=discord.Intents.all(
), activity=discord.Streaming(name="r!help | 16 Servers", url='https://www.twitch.tv/superbotseries'), help_command=None)
# with open(r"C:\Users\New uSer\Documents\GitHub\SuperCarBot\lib\bot\token.0", "r", encoding="utf-8") as tf:
#     TOKEN = tf.read() # Gets the bot token
TOKEN = '#token'

snipe_message_author = ""
snipe_message_content = ""

'''
@bot.command()
@commands.is_owner()
async def reload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"{cog} got reloaded")
    except Exception as e:
        print(f"{cog} got reloaded")
        raise e

bot.load_extension(f"cogs.mod")
bot.load_extension(f"cogs.rr")
bot.load_extension(f"cogs.welcome")
bot.load_extension(f"cogs.stat")
bot.load_extension(f"cogs.misc")
bot.load_extension(f"cogs.lockdown")
bot.load_extension(f"cogs.levelrewards")
bot.load_extension(f"cogs.google")
bot.load_extension(f"cogs.fun")
bot.load_extension(f"cogs.events")
bot.load_extension(f"cogs.currency")
'''

@bot.event
async def on_ready():
    print("Bot is online at {0.user}".format(bot))
   # guild = bot.get_guild(773961433188401183)
    # stdout = guild.get_channel(775112917229895731)
    # scheduler.add_job(rules_reminder, CronTrigger(minute=1, second=0)) # Calls "rule_reminder" every minute
    # scheduler.start()

# async def rules_reminder(self):
 #  guild = bot.get_guild(773961433188401183)
  # stdout = guild.get_channel(775112917229895731)
  # await stdout.send("Remember to adhere to the rules!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.json'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(774078494866407435)
    guild = bot.get_guild(773961433188401183)
    await channel.send(f'{member.mention}, welcome to **{guild.name}**! We hope you have a fun time!')


@bot.event
async def on_member_remove(ctx, member):
    channel = bot.get_channel(778834392104960002)
    guild = bot.get_guild(778834392104960000)
    fmt = f'{member.mention} has left {guild.name}'
    await ctx.send(member, fmt.format(member, member.server))


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(778850991922741259)
    await channel.send(f'I have been added to {guild.name}!')


@bot.event
async def on_raw_reaction_add(payload):
    with open('reactions.json', 'r') as f:
        reactions = json.load(f)
    for key, reaction in reactions["Reactions"].items():
        print(reaction)
        # replace with msg id and emoji name
        if payload.message_id == reaction["message_id"] and payload.emoji.id == reaction["emoji_id"]:
            guild = bot.get_guild(773961433188401183)
            role = guild.get_role(reaction["role_id"])  # replace with role id
            await payload.member.add_roles(role)


@bot.command()
async def levelenable(ctx):
    Value = True
    bot.remove_command(level)
    await ctx.send("Command Successfully Enabled")


@bot.command(pass_context=True)
async def servers(ctx):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers")

@bot.command()
@commands.has_permissions(administrator = True)
async def serverlock(ctx: commands.Context):
        """Lock a bot to its current servers only."""
        serverlocked = await serverlocked()
        await serverlocked.set(not serverlocked)

        if serverlocked:
            await ctx.send(_("The bot is no longer serverlocked."))
        else:
            await ctx.send(_("The bot is now serverlocked."))




@bot.command()
async def setwelcome(ctx, channel: discord.TextChannel):
    if ctx.message.author.guild_permissions.manage_messages:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT CHANNEL_id FROM main WHERE guild_id = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            await ctx.send(f"Channel has been set to {channel.mention}")
        elif result is not None:
            sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            await ctx.send(f"Channel has been updated to {channel.mention}")
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()


@bot.command()
async def about(ctx):
    embed = discord.Embed(title=":information_source: About Super Rocket Bot",
                          description="We have one of the best bots on the planet!", color=0xFF0000)
    embed.add_field(name="What about me?",
                    value='Super Rocket Bot, is made by `Audit Baansal#1234`, `Super#4060`, `Penguin Master#2263`. ')
    embed.add_field(name="What else?",
                    value="Super Rocket Bot is a bot currently still under development but has some epic commands. For more info, type `r!help`")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Super Rocket Bot Command List",
                          description="We have some epic commands!", color=0xFF0000)
    embed.add_field(name=':tools: Moderation', value='`r!moderation`')
    embed.add_field(name=':smiley: Fun', value='`r!fun`')
    embed.add_field(name=':file_folder: Miscellanious', value='`r!misc`')
    embed.add_field(name=":moneybag: Currency", value='`r!currency`')
    embed.add_field(name=":trophy: Leveling", value="`r!leveling`")
    embed.add_field(name=":wave: Welcome", value="`r!welcome`")
    embed.set_footer(text= "To learn about Super Rocket Bot, do `r!about`")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)

# ------------------------------Moderation-------------------------------------


@bot.command()
async def moderation(ctx):
    embed = discord.Embed(title="Moderation Commands",
                          description="These are the Moderation Commands of Super Rocket Bot", color=0xFF0000)
    embed.add_field(name="Moderation Commands", value="`r!ban <@member> [reason]` - Bans a member\n `r!kick <@member> [reason]` - Kicks a member\n `r!invite` - Shows the permamanent invite link to the server\n `r!emojis` - Spams all the emojis in the server\n `r!mute`  - Mutes a Member\n `r!unmute`  - Unmutes a member\n `r!delete[Messages]` - Deletes the amount of messages assigned\n  `r!warn[Member]`  - Warns A Member\n `r!addrole [Member][Role]`  - Adds a Role To A Member\n `r!removerole [Member][Role]`  - Removes a Role From A Member\n `r!tempban[Member][Duration]`  - Temporarily Bans A Member For A Chosen Time\n `r!setslowmode[time]`  - Set The Slowmode of a Channel\n `r!unban[Member]`  - Unbans a Member")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.command()
async def leveling(ctx):
    embed = discord.Embed(title=":trophy:  Leveling Commands",
                          description="This bot has his own leveling system! ", color=0xFF0000)
    embed.add_field(name="`r!level`", value="Find what level you are at.\n `r!levelenable`  - Enables the leveling system (Disabled by default)\n")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)

@bot.command()
async def welcome(ctx):
    embed = discord.Embed(title=":wave: Welcome Commands", description="This bot has its own welcome and leave messages!", color=0xFF0000)
    embed.add_field(name="`r!setwelcome [#channel]`", value="Enables the welcome system and sets a welcome channel.")
    await ctx.send(embed=embed)
@bot.command()  # nwhen creating a new command, this is what you use
@commands.has_permissions(administrator=True)  # checks if user has admin perms
# the name of the function is the name of the command. So the name of the command is "ban".
async def ban(ctx, member: discord.Member, *reason):
    # checks if the member you want to ban has admin perms
    if member.guild_permissions.administrator and ctx.author.id != 715340764485517442:
        return await ctx.send('<a:BONK:776844927371313183>''That member has the Administrator permission, and you know that. So no thank you.')
    shown_reason = ""
    for word in reason:
        # the reason will be multiple words, so it will be in a tuple. We don't want it to be in a tuple, but we want it to be in a sentence so thats what "shown_reason" is
        shown_reason += f'{word} '
    if len(reason) == 0:
        shown_reason = 'No reason provided'
    embed = discord.Embed(name="You Were Banned From Around The Globe",
                          description=f"You were banned from {ctx.guild.name} for {shown_reason}", color=0xFF0000, inline=True)
    embed.add_field(
        name="Appeal", value="If you would like to appeal, go to https://forms.gle/qABWJa3ijvQSc3aG8 .")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await member.send(embed=embed)
    await member.ban()  # Ultimatley Bans the Member
    await ctx.send(f'Successfully banned {member.mention} for {shown_reason}!')


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Successfully unbanned {user}")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    msg = await ctx.send(f"Successfully deleted {amount} messages.")
    await asyncio.sleep(2)
    await msg.delete()


@bot.command()
@commands.has_permissions(administrator=True)  # checks if user has admin perms
async def kick(ctx, member: discord.Member, *reason):
    # checks if the member you want to kick has admin perms
    if member.guild_permissions.administrator and ctx.author.id != 715340764485517442:
        return await ctx.send('<a:BONK:776844927371313183>''Sorry, that perms has the **ADMINISTRATOR** permissions, and you know that. No thank you.')
    shown_reason = ""
    for word in reason:
        # the reason will be multiple words, so it will be in a tuple. We don't want it to be in a tuple, but we want it to be in a sentence so thats what "shown_reason" is
        shown_reason += f'{word} '
    if len(reason) == 0:
        shown_reason = 'No reason provided'
    await member.kick()  # Ultimately Kicks the Member
    await ctx.send(f'Successfully kicked {member.mention} for {shown_reason}!')


@bot.command()
@commands.has_permissions(administrator=True)
async def emojis(ctx):
    for emoji in ctx.guild.emojis:
        await ctx.send(emoji)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Successfully gave role \"{role.name}\" to {user.name}")


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
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
async def tempban(ctx, member: discord.Member, days=1, *, reason):
    if not member.guild_permissions.manage_guild or ctx.author.id == 715340764485517442:
        await member.ban(delete_message_days=0)
        await ctx.send('User banned for **'+str(days)+' day(s)**')
        ban_list.append(member)
        day_list.append(days*24*60*60)
        server_list.append(ctx.guild)
        await member.send(f"You were banned from Around The Globe for {reason} for {days} day/s. Don't worry, you will be immediately unbanned from the server when {days} pass.")
    else:
        await ctx.send('<a:BONK:776844927371313183>''They have manage guild perms so you cant ban them')
    shown_reason = ""
    for word in reason:
        # the reason will be multiple words, so it will be in a tuple. We don't want it to be in a tuple, but we want it to be in a sentence so thats what "shown_reason" is
        shown_reason += f'{word} '
    if len(reason) == 0:
        shown_reason = 'No reason provided'

    await member.send(f"You were banned from Around The Globe for {reason} for {days} day/s. Don't worry, you will be immediately unbanned from the server when {days} pass.")


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
    with open('warns.json', 'w') as f:
        json.dump(warns, f)
    await ctx.send(f'{member.mention} was warned for {shown_reason}! ')


@bot.command()
@commands.has_permissions(manage_guild=True)
async def delwarn(ctx, member: discord.Member, id):
    if member.guild_permissions.manage_guild and ctx.author.guild_permissions.administrator:
        return await ctx.send('<a:BONK:776844927371313183>''That member has the Manage Server permission, so you can\'t delete their warn!')
    with open('warns.json', 'r') as f:
        warns = json.load(f) 
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


@commands.group(name='set', invoke_without_command=True)
@commands.has_permissions(manage_guild=True)
async def set(self, ctx):
    await ctx.send("You need to use a subcommand")


@bot.command()
async def currency(ctx):
    embed = discord.Embed(title="Currency Commands",
                          description="These are the Currency Commands in Super Rocket Bot", color=0xFF0000)
    embed.add_field(name="Currency Commands", value="`r!register`  - Registers you in the currency system\n `r!bal`  - View Your Balance\n `r!transfer[Amount][Member]`  - Give Your Super Coins to another person\n `r!daily`  - Earn Your Daily Super Coins\n `r!hourly`  - Earn Your Hourly Super Coins\n `r!work`  - Work Per Hour For 1000 Super Coins\n `r!beg`  - Recieve 350 Super Coins From Audit Baansal\n `r!search`  - Search For Super Coins lying on the ground!\n `r!hunt`  - Hunt in the forest and get some Super coins!\n `r!fish`  - Fish in a river filled with fish!\n `r!deposit[Amount]/[Max]`  - Deposits the chosen amount from your wallet to your bank\n `r!with[amount]/[all]`  - Withdraws the chosen amount from your bank to your wallet.\n `r!rob[amount][User]`  - Robs Money From A User")
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def register(ctx):
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    id = str(ctx.author.id)
    if id not in amounts:
        amounts[id]["wallet"] = 100
        amounts[id]["bank"] = 0
        await ctx.send("You are now registered")
        with open('bank.json', 'w') as f:
            amounts = json.dump(amounts, f)
    else:
        await ctx.send('<a:BONK:776844927371313183>'"You already have an account")


@bot.command()
async def google(ctx):
   await ctx.send("https://lmgtfy.app/#gsc.tab=0")

@bot.command()
async def support(ctx):
    support_invite=discord.Embed(name="This is Super Rocket Bot's Support Server.",  color=0xFF0000)
    support_invite.add_field(name="Join Super Rocket Bot Support Server For 10K Super Coins!", value="https://discord.gg/Fqcjd9HkPs")
    support_invite.set_footer(text="JOIN NOW FOR 10K SUPER COINS")
    support_invite.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=support_invite)   



@bot.event
async def on_guild_join(guild):
        channel = discord.utils.get(bot.get_all_channels(), guild__name=guild.name, name='general')
        print(channel.id)
        embed = discord.Embed(title="Howdy Folks!", description="I am Super Rocket Bot, and you made the best decision ever when you added me!", color=0xFF0000)
        embed.add_field(name="I can do many things to make your server really, really great! To try me out, run the command `r!help`!")
        embed.add_field(name="Support Server", value="If you have any questions, suggestions, or you just want to win 10K Super Coins, join Super Rocket Bot Support Server now! https://discord.gg/Fqcjd9HkPs")
        await channel.send(embed=embed) 


@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    id = str(ctx.author.id)  
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id]["wallet"] += 5000
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    embed = discord.Embed(title=f"Here are is your daily award, {ctx.author.name}",
                          description="**5,000 Super coins** were placed in your balance!", color=0xFF0000)
    embed.set_footer(text='You can claim this reward again tomorrow!')
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, e):
    embed = discord.Embed(
        name="Error", description=f'There was an error: {e}', color=0xFF0000)
    embed.set_footer(text="Please Join The Support Server For Help. The Support Server Link Is Provided in the command r!support")
    
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    id = str(ctx.author.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id]["wallet"] += 1000
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("`LETS GOOO` You Worked Really Well! 1000 Super Coins Are In Your Balance!")


@bot.command()
async def rps(ctx, choice: str=None):
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)

    choice1 = choice.replace("r", "rock")
    choice2 = choice1.replace("p", "paper")
    final_choice = choice2.replace("s", "scissors")

    if final_choice == None:
        await ctx.send("Hello There! Thanks for choosing Super Rocket Bot to play Rock Paper Scissors. Please enter a choice!")

    elif final_choice == "rock" and bot_choice == "paper":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("I win!")

    elif final_choice == "paper" and bot_choice == "rock":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("You win!")

    elif final_choice == "scissors" and bot_choice == "rock":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("I win!")

    elif final_choice == "paper" and bot_choice == "scissors":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("I win!")

    elif final_choice == "scissors" and bot_choice == "paper":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("You win!")

    elif final_choice == "rock" and bot_choice == "paper":
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("I win!")

    elif final_choice == bot_choice:
        await ctx.send(f"We both chose {bot_choice}!")
        await ctx.send("It was a tie!")
        
    else:
        pass

@bot.command()
async def cal(ctx, problem):
    await ctx.send(str(eval(problem)))


@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def hourly(ctx):
    # with open('timer.json', 'r') as f:
    #   timer = json.load(f)
    # try:
    #   cooldown = timer["Hourly Cooldown"][ctx.author.id]
    #   return await ctx.send(f'You are on cooldown, and need to wait for {cooldown} seconds!')
    # except:
    #   pass
    id = str(ctx.author.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id]["wallet"] += 500
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    embed = discord.Embed(title=f"Here is your hourly award, {ctx.author.name}",
                          description="**500 Super coins** were placed in your balance!", color=0xFF0000)
    embed.set_footer(text='You can claim this reward again in an hour!')
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.command(aliases=["gimmenitro"])
async def nitro(ctx):
    await ctx.send("https://media.discordapp.net/attachments/758070571308417035/779925889881735178/oY2iuBIQPA.png")


@bot.command(pass_context=True, aliases=["balance"])
async def bal(ctx, member: discord.Member = None):
    if not member:
        id = str(ctx.author.id)
    else:
        id = str(member.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    wallet = amounts[id]["wallet"]
    bank = amounts[id]["bank"]
    if id in amounts:
        if not member:
            own_balance = discord.Embed(
                name=f"Here is your balance {ctx.author.id}!", description=f"You have {wallet} Super coins in your wallet and {bank} in your bank :moneybag:", color=0xFF0000)
            own_balance.set_footer(
                text="Super Rocket Bot", icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
            await ctx.send(embed=own_balance)
        else:
            other_balance = discord.Embed(name=f"Here is {member.mention}'s balance!'",
                                          description=f"{member.mention} has {wallet} Super coins in their wallet and {bank} in their bank :moneybag:", color=0xFF0000)
            other_balance.set_footer(
                text="Super Rocket Bot", icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
            await ctx.send(embed=other_balance)
    else:
        await ctx.send("You do not have an account")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def search(ctx):
    with open("bank.json", "r") as f:
        amounts = json.load(f)
    earnings = random.randrange(2000)

    if earnings == 0:
        await ctx.send(f"How unlucky... You didn't find anything...")

    elif earnings > 50:
        await ctx.send(f"Nice you found {earnings} coins under your bed")

    elif earnings > 100:
        await ctx.send(f"You looked inside you backpack and found {earnings} coins")

    elif earnings > 500:
        await ctx.send(f"You found {earnings} coins in your coat. They're now in your balance")

    elif earnings > 800:
        await ctx.send(f"You looked inside a tree and found {earnings} coins. Why would you even look in a tree??")

    elif earnings > 1500:
        await ctx.send(f"You searched Area 51 and found {earnings} coins. RUNNNNNN")

    elif earnings > 2000:
        await ctx.send(f"**You went all the way to MARS*** and found {earnings} coins. Say hi to the aliens for me!")

    if id in amounts:
        amounts[id]["wallet"] += earnings

    with open('bank.json', 'w') as f:
        json.dump(amounts, f)


@bot.command()
async def say(ctx, *, quote: str=None):
  if quote == None:
    await ctx.send(f":woozy_face: I forgot what to say...\n**-{ctx.message.author}**")

  else:
    await ctx.send(f"{quote}\n**-{ctx.message.author}**")


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def hunt(ctx):
    id = str(ctx.author.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id]["wallet"] += 250
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("You shot a deer's wallet and found 250 Super Coins!")


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def fish(ctx):
    id = str(ctx.author.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if id in amounts:
        amounts[id]["wallet"] += 300
    else:
        return await ctx.send('<a:BONK:776844927371313183>''You do not have an account')
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("You dropped down your fishing rod into a river and found 300 Super coins in the river bed! They're now in your balance!")


@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    with open("bank.json", "r") as f:
        amounts = json.load(f)
    earnings = random.randrange(2000)
    id = str(ctx.author.id)
    if id not in amounts:
        return await ctx.send('You do not have an account')
    if earnings == 0:
        await ctx.send(f"How unlucky... You didn't get anything...")

    elif earnings > 50:
        await ctx.send(f"Nice you got ${earnings} from a cool dude")

    elif earnings > 100:
        await ctx.send(f"Someone felt nice and gave you ${earnings}")

    elif earnings > 500:
        await ctx.send(f"You seem to have a way with people! Someone gave you ${earnings}")

    elif earnings > 800:
        await ctx.send(f"What a lucky day!! Someone gave you ${earnings}")

    elif earnings > 1500:
        await ctx.send(f"A rich man passed by you and felt bad. So ha gave you ${earnings}")

    elif earnings > 2000:
        await ctx.send(f"A shady man walked up to you and said 'I know how tough it can be out here' before giving you ${earnings}")
    amounts[id]["wallet"] += earnings

    with open('bank.json', 'w') as f:
        json.dump(amounts, f)


@bot.command(pass_context=True)
@commands.cooldown(1, 45, commands.BucketType.user)
async def rob(ctx, other: discord.Member):
    primary_id = str(ctx.author.id)
    other_id = str(other.id)
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    if primary_id not in amounts:
        return await ctx.send("You do not have an account")
    elif other_id not in amounts:
        return await ctx.send("The other person does not have an account")
    if amounts[primary_id]["wallet"] < 500:
        return await ctx.send('You need at least 500 coins to rob!')  # k thx
    elif amounts[other_id]["wallet"] == 0:
        return await ctx.send("The other person does not have anything in his wallet. Leave him live his life!")
    chance = random.randrange(3)
    earnings = random.randrange(2000)
    if chance == 3:
        amounts[primary_id]["wallet"] -= 500
        amounts[other_id]["wallet"] += 500
        # ye
        return await ctx.send(f'HAHAHAHA You got cought! You pay 500 Coins to {other.mention}')
    while amounts[primary_id]["wallet"] < earnings or amounts[other_id]["wallet"] < earnings:
        earnings = random.randrange(2000)

    if earnings > 50:
        await ctx.send(f"Nice you robbed {earnings} super coins from {other.mention}")

    elif earnings > 100:
        await ctx.send(f"You robbed ${earnings} from a {other.mention} who turns out to be a poor dude. You should be ashamed from yourself")

    elif earnings > 500:
        await ctx.send(f"People nowadays don't secure their money, so you robbed {earnings} super coins from {other.mention}")

    elif earnings > 800:
        await ctx.send(f"What a lucky day!! You found {other.mention}'s wallet with {earnings} super coins")

    elif earnings > 1500:
        await ctx.send(f"You found someone's house door open and a box filled with money right behind it. You robbed {earnings} super coins")

    elif earnings > 2000:
        await ctx.send(f"You robbed {other.mention}'s car and stole' {earnings} super coins inside it")

    amounts[primary_id]["wallet"] += earnings
    amounts[other_id]["wallet"] -= earnings

    with open('bank.json', 'w') as f:
        json.dump(amounts, f)


# @bot.event
# async def on_member_join(member):
#     with open('users.json', 'r') as f:
#         users = json.load(f)

#     await update_data(users, member)

#     with open('users.json', 'w') as f:
#         json.dump(users, f)

@bot.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break




@bot.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 15)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await bot.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    if Value == False:
        return
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        channel = bot.get_channel(774078494866407435)
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end


@bot.command()
async def level(ctx, member: discord.Member = None):
    if Value == False:
        return
    if Value == True:
        with open('users.json', 'r') as f:
            users = json.load(f)
    # rank_card = Image.new('RGB', (934, 282), color=0xafb6b8)
    # rank_card_font = ImageFont.truetype('Font/01_APompadourTextSample.ttf', 50)

#    rank_card_font2 = ImageFont.truetype('Font/02_APompadourTextSample.ttf', 100)

 #   rank_card_font3 = ImageFont.truetype('Font/03_APompadourTextSample.ttf', 30)


#    draw_rank_card = ImageDraw.Draw(rank_card)

        if not member:
            id = str(ctx.author.id)
            lvl = users[str(id)]['level']
            await ctx.send(f'You are at level {lvl}!')

            experience = users[id]['experience']
            lvl_start = users[id]['level']
            lvl_end = int(experience ** (1 / 4))

 #           draw_rank_card.text((450, 50), "Rank", fill="white", font=rank_card_font)
#          draw_rank_card.text((575, 14), "N", fill="white", font=rank_card_font2)
 # draw_rank_card.text((675, 50), "Level", fill="blue", font=rank_card_font)
 #           draw_rank_card.text((810, 14), str(users[id]['level']), fill="blue", font=rank_card_font2)
    #          draw_rank_card.text((50, 125), f"{ctx.author.mention} # {ctx.author.discriminator}", fill="white", font=rank_card_font)
   #         draw_rank_card.text((700, 140), f"{experience}", fill="white", font=rank_card_font3)
   #         draw_rank_card.text((750, 140), f" / {lvl_end} XP", fill=0x333434, font=rank_card_font3)

 #           rank_card.save('card.png')

         #       await ctx.send(file=discord.File('card.png'))
        else:
            if member.bot:
                return await ctx.send("Bots can't have a rank card!")
            id = str(member.id)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member.mention} is at level {lvl}!')

    #        draw_rank_card.text((450, 50), "Rank", fill="white", font=rank_card_font)
        #          draw_rank_card.text((575, 14), "N", fill="white", font=rank_card_font2)
    #            draw_rank_card.text((675, 50), "Level", fill="blue", font=rank_card_font)
     #           draw_rank_card.text((810, 14), str(users[member.id]['level']), fill="blue", font=rank_card_font2)
     #           draw_rank_card.text((50, 125), f"{member.name} # {member.discriminator}", fill="white",
     #                                   font=rank_card_font)
     #           draw_rank_card.text((700, 140), f"{experience}", fill="white", font=rank_card_font3)
        #        draw_rank_card.text((750, 140), f" / {lvl_end} XP", fill=0x333434, font=rank_card_font3)

        #      await ctx.send(file=discord.File('card.png'))

    #    except KeyError: #hey dude what is this
    #        await ctx.send("The user you specified doesn't have a rank card!")


@bot.command()
async def leaderboard(ctx):
    with open('users.json', 'r') as f:
        users = json.load(f)
    lb = {}
    for id in users:
        lb[users[str(id)]["level"]] = id
    leaderboards = []
    print(lb)
    for key, value in lb.items():
        leaderboards.append(value)

    top = sorted(leaderboards, key=lambda x: lb[x], reverse=True)

    await ctx.send(f'**<< 1 >>** <@{lb[top[0]]}> in level {top[0]} ')
    try:
        await ctx.send(f'**<< 2 >>** <@{lb[top[1]]}> in level {top[1]} ')
        try:
            await ctx.send(f'**<< 3 >>** <@{lb[top[2]]}> in level{top[2]} ')
        except:
            await ctx.send('There is no 3rd place yet.')
    except:
        await ctx.send('There is no 2nd place yet.')


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    with requests.get(ctx.message.author.avatar_url) as r:
        img_data = r.content
    with open('pfpimg.png', 'wb') as handler:
        handler.write(img_data)
    welcome = Image.open("welcom.png")
    pfpimg = Image.open(f"{user.profile}")
    pfpbg = Image.open("pfpbg.png")
    mask_im = Image.new("L", (500, 500), 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((140, 50, 260, 170), fill=255)
    mask_im.save('mask_circle.jpg', quality=95)
    pfp = welcome.copy()
    pfp.paste(pfpimg, (0, 0))
    pfp.save('test.png', quality=1024)
    testimg = Image.open("test.png")
    testimg.save("pop.png")
    await ctx.send(file=discord.File("pop.png"))


@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    elif other_id not in amounts:
        await ctx.send("The other person does not have an account")
    elif amounts[primary_id]["wallet"] < amount:
        await ctx.send("You cannot afford this transaction")
    else:
        amounts[primary_id]["wallet"] -= amount
        amounts[other_id]["wallet"] += amount
        await ctx.send("Transaction complete")
    with open('bank.json', 'w') as f:
        amounts = json.dump(amounts, f)


@bot.command()
async def fun(ctx):
    embed = discord.Embed(title="Fun Commands", description="These are the Fun Commands of Super Rocket Bot", color=0xFF0000)
    embed.add_field(name="Fun Commands",value='`r!distract`  - Makes you distracted by Henry Stickmin\n `r!ping`  - Shows the ping/latency of the bot\n `r!logo`  - Shows Super Rocket Bot\'s Logo\n `r!snipe`  - Snipes the most recent deleted message\n `r!coinflip`  - Flips A Coin, you either get heads or tails\n `r!kill[user]`  - Kills a User\n `r!google`  - Google Search From Discord\n `r!amimod`  - Asks the bot if you\'re a moderator.\n `r!nitro`  - Makes the bot give you free nitro\n `r!say[Something]` - Makes the bot say something\n `r!rps[choice]` - Play RPS')
    embed.set_footer(text="Super Rocket Bot", icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)


@bot.command()
async def snipe(ctx):
    if snipe_message_content == "":  # yeah
        await ctx.send("There\'s nothing to snipe.")
    else:
        embed = discord.Embed(
            description=f"{snipe_message_content}", color=0xFF0000)
        embed.set_footer(
            text=f"Sniped by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url, )
        embed.set_footer(text="Super Rocket Bot",
                         icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
        embed.set_author(name=f"")
        await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    ping = round(bot.latency*1000)
    await ctx.send(f':ping_pong:' f"Pong! {str(ping)}ms")


@bot.command()
async def party(ctx):
    await ctx.send('<a:kirby_party:778705947719761970>')


@bot.command(pass_context=True)
async def emoji(ctx):
    msg = await bot.say("working")
    reactions = ['dart']
    for emoji in reactions:
        await bot.add_reaction(msg, emoji)


@bot.command()
async def getpfp(ctx, member: discord.Member):
    if not member:
        member = ctx.message.author
    await ctx.send(member.avatar_url)


async def countdown():
    await bot.wait_until_ready()
    while not bot.is_closed:
        await asyncio.sleep(1)
        day_list[:] = [x-1 for x in day_list]
        for day in day_list:
            if day <= 0:
                try:
                    await bot.unban(server_list[day_list.index(day)], ban_list[day_list.index(day)])
                except:
                    print('Error! User already unbanned!')
                del ban_list[day_list.index(day)]
                del server_list[day_list.index(day)]
                del day_list[day_list.index(day)]


@bot.command()
async def distract(ctx):
    # always have an a after the < (for custom emojis), and make sure you have the right ID
    await ctx.send('<a:HenryStickminDance:774347966395318303>')


@bot.command()
async def logo(ctx):
    await ctx.send('https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')


@bot.command()
async def misc(ctx):
    embed = discord.Embed(title="Miscellanious Commands",
                          description="These are some miscellanious commands of Super Rocket Bot", color=0xFF0000)
    embed.add_field(name="Miscellanious Commands",
                    value='`r!dev`  - Shows The Owners/Developers Of Super Rocket Bot\n `r!owner`  - Shows The Owner Of The Server\n `r!invites`  - Shows How Many Invites Have\n `r!dev`  - Shows The Developers Of Super Rocket Bot\n `r!timer[Seconds]`  - Starts a timer!\n `r!serverinfo`  - Shows This Server\'s Info\n `r!warnings`  - Shows How Many Warnings You Have\n `r!gstart [minutes][Prize]`  - Creates a Giveaway\n `r!getpfp[user]`  - Shows The Profile Picture Of The Selected User\n `r!rr [Message ID][Emoji][Role ID]`  - Creates a Reaction Role.\n `r!userinfo[User]`  - Find Info About A Specific User\n `r!afk [minutes]`  - Adds `[AFK]` to your nickname for the chosen amount of time to show that you\'re afk.\n `r!servers`  - Shows how many servers Abdul\'s bot is currently in\n `r!cal[problem]`  - Makes the bot calculate a problem')
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)








# @bot.command()
# async def serverinfo(ctx):
#     guild = {guild.name}
#     embed = discord.Embed(
#         name="Server Info", description=f"**{guild.name}** Information", color=0xFF0000, inline=True)
#     embed.add_field(
#         name="Owner", value=f"The Owner Of {server.name} is **{server.owner}**")
#     embed.add_field(name="Member, Emoji, and Roles Count",
#                     value=f"This server has '**{ctx.guild.members}**'' Members, **100** emojis and **{ctx.guild.roles}** Roles")
#     embed.set_footer(text="Super Rocket Bot",
#                      icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
#     await ctx.send(embed=embed)


# @bot.command()
# async def triggers(ctx):
#     embed = discord.Embed(
#         title="Triggers", decription="These are the Triggers of Super Rocket Bot", color=0xFF0000)
#     embed.add_field(
#         name="Triggers", value='`yikes`\n`homework`\n`school`\n `blablabla`\n `abc`\n `audit`\n `lol`\n `triple lol`\n `bruh`\n `bye`\n `vs code`\n ')
#     embed.set_footer(text="Super Rocket Bot",
#                      icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
#     await ctx.send(embed=embed)


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

@bot.event
async def on_server_join(server):
    print(f"I have been added to {server.name}!")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def setslowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

@bot.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx):
    slowmode_delay = seconds
    await ctx.channel.send(f"The Slowmode in this channel is {seconds} seconds!")


def convert_time_to_seconds(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time

# member_pfp = member.avatar_url_as(format='png', size=128)
# guild = member.guild_name
# with requests.get(member_pfp) as r:
#         img_data = r.content
                
#         with open("pfpimg.png", "wb") as handler:
#             handler.write(img_data)
#         welcome = Image.open("welcom.png").convert("RGBA")
#         mask = Image.open("lolidk.png").convert("L")
#         pfpmask = Image.open("pfpmask.png").convert("L")
#         pfpimg = Image.open("pfpimg.png").convert("RGBA")
#         font = ImageFont.truetype("Poppins-Black.ttf", 25)
#         hfont = ImageFont.truetype("Poppins-Black.ttf", 30)
#         sfont = ImageFont.truetype("Poppins-Black.ttf", 20)
#         pfpimg.putalpha(pfpmask)
#         pfpimg.save("test1.png")
#         pic = Image.open("test1.png")
#         pic1 = welcome.copy()
#         welcome.putalpha(mask)
#         pic1.paste(pic, (20, 60), pfpmask)
#         pic1.save("test2.png")
#         welcomeimg = Image.open("test2.png")
#         draw = ImageDraw.Draw(welcomeimg)
#         draw.text((160, 90), f"Welcome to {guild.name},", (255, 255, 255), font=font)
#         draw.text((160, 115), f"{member}!", (255, 255, 255), font=hfont)
#         draw.text((160, 145), f"Member #{guild.member_count}", (211, 211, 211), font=sfont)
#         welcomeimg.save("finaltest.png")

@bot.command()
async def gstart(ctx, time=None, *prize: str):
    await ctx.message.delete()
    host = ctx.message.author
    embed = discord.Embed(title="🎉Giveaway!🎉",
                          description=f"Prize: {prize}", color=0xFF0000)

    embed.add_field(name=f"React with 🎉 to enter!",
                    value=f"Time remaining: **Starting timer...**\nHosted by: {host.mention}")
    embed.set_footer(text=f"Good luck!")
    time_int = convert_time_to_seconds(time)
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("🎉")

    while time_int > 0:
        await asyncio.sleep(5)
        time_int -= 5

        if time_int > 86400:
            format = "days"
            formatted_int = time_int / 86400
            display_int = round(formatted_int)

        elif time_int > 3600:
            format = "hours"
            formatted_int = time_int / 3600
            display_int = round(formatted_int)

        elif time_int > 60:
            format = "minutes"
            formatted_int = time_int / 60
            display_int = round(formatted_int)

        else:
            format = "seconds"
            display_int = round(time_int)

        new_embed = discord.Embed(
            title="🎉Giveaway!🎉", description=f"Prize: {prize}", color=0xFF0000)

        new_embed.add_field(name=f"React with 🎉 to enter!",
                            value=f"Time remaining: **{int(display_int)} {format}**\nHosted by: {host.mention}")
        new_embed.set_footer(text=f"Good luck!")
        new_embed.set_footer(
            text="Super Rocket Bot", icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')

        await msg.edit(embed=new_embed)

    win_msg = await ctx.channel.fetch_message(msg.id)

    entry = await win_msg.reactions[0].users().flatten()
    entry.pop(entry.index(bot.user))

    winner = random.choice(entry)

    win_embed = discord.Embed(title="🎉Giveaway Ended!🎉", color=0xFF0000)

    win_embed.add_field(name=f"Congratulations!",
                        value=f"{winner.mention} won the giveaway for {prize}!")
    win_embed.set_footer(text=f"Giveaway ended!")
    win_embed.set_footer(
        text="Super Rocket Bot", icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')

    await ctx.send(embed=win_embed)

    await ctx.send(f"Congratulations, {winner.mention}! You won the giveaway for {prize}!")


@bot.command(pass_context=True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command(pass_context=True, no_pm=True)
@commands.has_permissions(manage_roles=True)
async def botpermissions(ctx, self):
    """Shows the bot's permissions.
    This is a good way of checking if the bot has the permissions needed
    to execute the commands it wants to execute.
    To execute this command you must have Manage Roles permissions or
    have the Bot Admin role. You cannot use this in private messages.
    """
    channel = ctx.channel
    member = ctx.message.guild.me
    await self.say_permissions(ctx, member, channel)


@bot.command(pass_context=True)
async def coinflip(ctx):
    variable = [
        "Heads",
        "Tails", ]
    await ctx.send("{}".format(random.choice(variable)))


@bot.command(pass_context=True)
async def kill(ctx, other: discord.Member):
    primary_id = str(ctx.author.id)
    other_id = str(other.id)
    variable = [
        f"{other.mention} died after telling {ctx.author.mention} not to tell anyone that they were going to kill them.",
        f"{ctx.author.mention} pushed {other.mention} down Mt.Everest and died.",
        f"{ctx.author.mention} hit {other.mention} with a bowling ball and died.", ]
    await ctx.send("{}".format(random.choice(variable)))


@bot.command()
async def userinfo(ctx, other: discord.Member):
    embed = discord.Embed(title="User information",
                          colour=0x0EBFE9, )
    embed.add_field(name="Name", value=f"{other.mention}", inline=False)
    embed.add_field(name="ID", value=f"`{other.id}`", inline=False)
    embed.add_field(name="Status", value=f"`{other.status}`", inline=False)
    embed.add_field(name="Created At",
                    value=f"`{other.created_at.strftime('%D %H:%M')}`", inline=False)
    # k just ping me on discord when ur done
    embed.add_field(name="Joined server at",
                    value=f"`{other.joined_at.strftime('%D %H:%M')}`", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def numgame(self, ctx):
    number = random.randint(0, 100)
    for i in range(0, 5):
        await ctx.send('guess')
        response = await self.bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            await ctx.send('bigger')
        elif guess < number:
            await ctx.send('smaller')
        else:
            await ctx.send('true')


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
            warnings += f'{warn} (id = {warnings_list.index(warn)}) \n'  # ok
    else:
        warnings = "None"
    embed = discord.Embed(title=f'Warnings for {member.name}', color=0xFF0000)
    embed.add_field(name='Warnings:', value=f'{warnings}')
    embed.set_footer(text="Super Rocket Bot",
                     icon_url='https://cdn.discordapp.com/avatars/770406704642523161/928c55238c5b35b4afaf3c949719d971.webp?size=1024')
    await ctx.send(embed=embed)

    @bot.command(name='config')
    @commands.has_permissions(manage_guild=True)
    async def cfg(self, ctx):
        enu = {
            "Message edits": 1,
            "Message deletions": 2,
            "Role updates": 3,
            "Name changes": 4,
            "Join/Leave": 5,
            "Avatar updates": 6,
            "Bans/Unbans": 7
        }
        bot.c.execute('SELECT * FROM logging WHERE server=?', (ctx.guild.id,))
        logging_table = bot.c.fetchone()
        bot.c.execute('SELECT * FROM config WHERE guild_id=?',
                       (ctx.guild.id,))
        config = bot.c.fetchone()
        bot.c.execute(
            'SELECT user_id, plonked FROM userconfig WHERE guild_id=?', (ctx.guild.id,))
        id_and_plonk = bot.c.fetchall()
        print(id_and_plonk)
        bot.c.execute('''SELECT log_channel, twitch_channel, prefix
                          FROM servers WHERE id=?''',
                       (ctx.guild.id,))
        cfg = bot.c.fetchone()

        e = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"Bot config for {ctx.guild.name}")
        enabled, disabled = [], []
        for k, v in enu.items():
            if logging_table[v]:
                enabled.append(k.capitalize())
            else:
                disabled.append(k.capitalize())
        ena = '\n'.join(enabled) or "None"
        dis = '\n'.join(disabled) or "None"
        cmd_ignore = config[1]
        if cmd_ignore is None:
            cmd_ignore = "None"
        elif cmd_ignore == "":
            cmd_ignore = "None"
        else:
            cmd_ignore = '\n'.join("<#{}>".format(x)
                                   for x in config[1].split(',') if x != "")
        ignore = logging_table[8] or "None"
        if ignore != "None":
            ignore = '\n'.join("<#{}>".format(x)
                               for x in ignore.split(',') if x != "")
        if config[2] is None:
            cmd_disabled = "None"
        elif config[2] == "":
            cmd_disabled = "None"
        else:
            cmd_disabled = config[2].split(',')
            cmd_disabled = ', '.join(cmd_disabled) or None
        log_chan = f'<#{cfg[0]}>' if cfg[0] is not None else "None"
        twtch_chan = f'<#{cfg[1]}>' if cfg[1] is not None else "None"
        bot.c.execute('''SELECT *
                          FROM greetings
                          WHERE guild_id=?''',
                       (ctx.guild.id,))
        greet = bot.c.fetchone()
        try:
            _, greet_chn, gre_msg, far_msg, ban_msg = greet
        except:
            greet_chn = "None"
        else:
            greet_chn = f"<#{greet_chn}>"

        if greet_chn == "None":
            gre_msg = far_msg = ban_msg = "<:redtick:318044813444251649>"
        else:
            gre_msg = "<:greentick:318044721807360010>" if gre_msg is not None else "<:redtick:318044813444251649>"
            far_msg = "<:greentick:318044721807360010>" if gre_msg is not None else "<:redtick:318044813444251649>"
            ban_msg = "<:greentick:318044721807360010>" if gre_msg is not None else "<:redtick:318044813444251649>"

        plonks = '\n'.join(
            [f"<@{x[0]}>" for x in id_and_plonk if x[1]]) or "None"
        server_prefixes = cfg[2].split(',')
        server_prefixes = '\n'.join(server_prefixes)
        e.add_field(name='Enabled (log)', value=ena)
        e.add_field(name='Disabled (log)', value=dis)
        e.add_field(name='Ignored Channels (log)', value=ignore)
        e.add_field(name="Ignored Channels", value=cmd_ignore)
        e.add_field(name="Disabled Commands", value=cmd_disabled)
        e.add_field(name="Plonks", value=plonks)
        e.add_field(name="Logging Channel", value=log_chan)
        e.add_field(name="Twitch Channel", value=twtch_chan)
        e.add_field(name="Greet Channel", value=greet_chn)
        e.add_field(
            name="Greets?", value=f"{gre_msg} Greet msg\n{far_msg} Farewell msg\n{ban_msg} Ban msg")
        e.add_field(name="Prefixes", value=server_prefixes)
        await ctx.send(embed=e)


@bot.command(no_pm=True)
async def poll(ctx, *, question: str):
    msg = await ctx.send("**{}** asks: {}".format(ctx.author, question.replace("@", "@\u200b")))
    try:
        await ctx.message.delete()
    except:
        pass
    yes_thumb = "👍"
    no_thumb = "👎"
    await msg.add_reaction(yes_thumb)
    await msg.add_reaction(no_thumb)


@bot.command()
@commands.has_permissions(manage_guild=True)
async def amimod(ctx):
    await ctx.send("Yes, you're a mod as far as I can tell.")


@bot.event
async def on_member_join(member):
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT CHANNEL_id FROM main WHERE guild_id = {member.guild.id}")
    result = cursor.fetchone()
    if result is None:
        return
    else:
        cursor.execute(f"SELECT msg FROM main WHERE guild_id = {member.guild.id}")
        result1 = cursor.fetchone()
        members = {len(list(member.guild.members))}
        mention = member.mention
        user = member.name
        guild = member.guild
        embed = discord.Embed(color=0xFF0000, description=f"Welcome to {guild} {member.mention}! Enjoy your time!")
        # embed.set_thumbnail(icon_url=f"{member.avatar.url}")
        # embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar.url}")
        embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        

        channel = bot.get_channel(id=int(result[0]))

        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT CHANNEL_id FROM main WHERE guild_id = {member.guild.id}")
    result = cursor.fetchone()
    if result is None:
        return
    else:
        cursor.execute(f"SELECT msg FROM main WHERE guild_id = {member.guild.id}")
        result1 = cursor.fetchone()
        members = {len(list(member.guild.members))}
        mention = member.mention
        user = member.name
        guild = member.guild
        embed = discord.Embed(color=0xFF0000, description=f"{member.mention} has left {guild}. :disappointed: See you when you come back!")
        # embed.set_thumbnail(icon_url=f"{member.avatar.url}")
        # embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar.url}")
        embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        

        channel = bot.get_channel(id=int(result[0]))

        await channel.send(embed=embed)

@commands.group(invoke_without_command=True)
async def welcome(self, ctx):
    
    await ctx.send('Avaliable Setup Commands: \n welcome channel <#channel>\n welcome text <messages>')


@welcome.command()
async def channel(ctx, channel: discord.TextChannel):
    if ctx.message.author.guild_permissions.manage_messages:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT CHANNEL_id FROM main WHERE guild_id = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            await ctx.send(f"Channel has been set to {channel.mention}")
        elif result is not None:
            sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            await ctx.send(f"Channel has been updated to {channel.mention}")
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()




reaction_roles_data = {}

try:
    with open("reactions.json") as file:
        reaction_roles_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    with open("reaction_roles.json", "w") as file:
        json.dump({}, file)


@atexit.register
def store_reaction_roles():
    with open("reactions.json", "w") as file:
        json.dump(reaction_roles_data, file)




# @bot.event
# async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
#         def parse_reaction_payload
#         role, user = bot.parse_reaction_payload(payload)
        
#         if role is not None and user is not None:
#             await user.add_roles(role, reason="ReactionRole")

@bot.event
async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        role, user = bot.parse_reaction_payload(payload)
        if role is not None and user is not None:
            await user.remove_roles(role, reason="ReactionRole")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def reaction(
        ctx,
        emote,
        role: discord.Role,
        channel: discord.TextChannel,
        title,
        message,
    ):
        embed = discord.Embed(title=title, description=message)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(emote)
        bot.add_reaction(ctx.guild.id, emote, role.id, channel.id, msg.id)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def reaction_add(
        ctx, emote, role: discord.Role, channel: discord.TextChannel, message_id
    ):
        bot.http.add_reaction(channel, message_id, emoji)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def reactions(ctx):
        guild_id = ctx.guild.id
        data = reaction_roles_data.get(str(guild_id), None)
        embed = discord.Embed(title="Reaction Roles")
        if data is None:
            embed.description = "There are no reaction roles set up right now."
        else:
            for index, rr in enumerate(data):
                emote = rr.get("emote")
                role_id = rr.get("roleID")
                role = ctx.guild.get_role(role_id)
                channel_id = rr.get("channelID")
                message_id = rr.get("messageID")
                embed.add_field(
                    name=index,
                    value=f"{emote} - @{role} - [message](https://www.discordapp.com/channels/{guild_id}/{channel_id}/{message_id})",
                    inline=False,
                )
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def reaction_remove(ctx, index: int):
        guild_id = ctx.guild.id
        data = reaction_roles_data.get(str(guild_id), None)
        embed = discord.Embed(title=f"Remove Reaction Role {index}")
        rr = None
        if data is None:
            embed.description = "Given Reaction Role was not found."
        else:
            embed.description = (
                "Do you wish to remove the reaction role below? Please react with 🗑️."
            )
            rr = data[index]
            emote = rr.get("emote")
            role_id = rr.get("roleID")
            role = ctx.guild.get_role(role_id)
            channel_id = rr.get("channelID")
            message_id = rr.get("messageID")
            _id = rr.get("id")
            embed.set_footer(text=_id)
            embed.add_field(
                name=index,
                value=f"{emote} - @{role} - [message](https://www.discordapp.com/channels/{guild_id}/{channel_id}/{message_id})",
                inline=False,
            )
        msg = await ctx.send(embed=embed)
        if rr is not None:
            await msg.add_reaction("🗑️")

            def check(reaction, user):
                return (
                    reaction.message.id == msg.id
                    and user == ctx.message.author
                    and str(reaction.emoji) == "🗑️"
                )

            reaction, user = await bot.wait_for("reaction_add", check=check)
            data.remove(rr)
            reaction_roles_data[str(guild_id)] = data
            store_reaction_roles()

def add_reaction(guild_id, emote, role_id, channel_id, message_id):
        if not str(guild_id) in reaction_roles_data:
            reaction_roles_data[str(guild_id)] = []
        reaction_roles_data[str(guild_id)].append(
            {
                "id": str(uuid.uuid4()),
                "emote": emote,
                "roleID": role_id,
                "channelID": channel_id,
                "messageID": message_id,
            }
        )
        store_reaction_roles()

def parse_reaction_payload(payload: discord.RawReactionActionEvent):
        guild_id = payload.guild_id
        data = reaction_roles_data.get(str(guild_id), None)
        if data is not None:
            for rr in data:
                emote = rr.get("emote")
                if payload.message_id == rr.get("messageID"):
                    if payload.channel_id == rr.get("channelID"):
                        if str(payload.emoji) == emote:
                            guild = bot.get_guild(guild_id)
                            role = guild.get_role(rr.get("roleID"))
                            user = guild.get_member(payload.user_id)
                            return role, user
        return None, None
    



@bot.command()
async def fortnite(ctx):
    with open('bank.json', 'r') as f:
        amounts = json.load(f)
    id = str(ctx.author.id)
    if id not in amounts:
        return await ctx.send("You do not have an account")
    if amounts[id]["wallet"] < 350:
        return await ctx.send("You need to have 350 coins in your wallet in order to run this command")

    elif amounts[id]["wallet"] > 350 or amounts[id]["wallet"] == 350:
        amounts[id]["wallet"] -= 350
        with open('bank.json', 'w') as f:
            json.dump(amounts, f)
        await ctx.send("Fortnite Sucks. You lose 350 Coins.")


@bot.command(aliases=["dep"])
async def deposit(ctx, amount):
    with open('bank.json') as f:
        amounts = json.load(f)
    id = str(ctx.author.id)
    if amount == "all":
        amount = amounts[id]["wallet"]
    else:
        amount = int(amount)
    if amounts[id]["wallet"] < amount:
        return await ctx.send("You don\'t have that much in your wallet'")
    amounts[id]["wallet"] -= amount
    amounts[id]["bank"] += amount
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("Done")


@bot.command(aliases=["with"])
async def withdraw(ctx, amount):
    with open('bank.json') as f:
        amounts = json.load(f)
    id = str(ctx.author.id)
    if amount == "all":
        amount = amounts[id]["bank"]
    else:
        amount = int(amount)
    if amounts[id]["bank"] < amount:
        return await ctx.send("You don\'t have that much in your bank'")
    amounts[id]["wallet"] += amount
    amounts[id]["bank"] -= amount
    with open('bank.json', 'w') as f:
        json.dump(amounts, f)
    await ctx.send("Done")


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
    if message.author.bot:
        return
    message_content = message.content.strip().lower()
    for bad_word in bad_words:
        bad_word = bad_word.replace('\n', '')
        if bad_word in message_content:
            await message.channel.send('<a:BONK:776844927371313183>'"{}, No bad words are allowed in Around The Globe. Next time it's a mute!  ".format(message.author.mention))
            

    await bot.process_commands(message)

bot.run(TOKEN)
