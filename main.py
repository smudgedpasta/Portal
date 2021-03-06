#!/usr/bin/python3

import discord
import json
import asyncio
import random
import os
import psutil
import traceback
import time
import datetime
import re

intents = discord.Intents.default()
intents.members = True
portal = discord.Client(intents=intents)

owners = [530781444742578188, 521926078403575814, 201548633244565504]
#            smudgedpasta         Ora-Allagis            Txin

discord_token = None
with open("auth.json", "r") as f:
    data = json.load(f)
    discord_token = data["token"]

_print = print
def print(*args, sep=" ", end="\n"):
    embed = discord.Embed(colour=discord.Colour(3214259))
    embed.description = "```" + str(sep).join(str(i) for i in args) + end + "```"
    asyncio.create_task(portal.get_channel(798861277043884082).send(embed=embed))
    return _print(*args)

def has_username(content, words, user, *aliases):
    if user:
        for name in (n.lower() for n in (user.name, user.display_name) + aliases):
            if name:
                if " " in name:
                    if name in content:
                        return True
                else:
                    if name in words:
                        return True

async def log_update():
    await portal.wait_until_ready()
    start_time = time.time()
    current_day = str(datetime.datetime.utcnow().date())
    while not portal.is_closed():
        try:
            globals()["eloop"] = asyncio.get_event_loop()
            uptime = datetime.timedelta(seconds=time.time() - start_time)
            new_day = str(datetime.datetime.utcnow().date())
            if new_day != current_day:
                current_day = new_day
                print(f"🔹 Current uptime: {str(uptime).rsplit('.', 1)[0]}")
        except Exception as e:
            print(e)
        await asyncio.sleep(1)
portal.loop.create_task(log_update())

@portal.event
async def on_ready():
    await portal.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="God and consuming frogs. 🐸"))
    print("Successfully loaded.")

portal_emotes = [
    "<:Sassy:522184015109947392>",
    "<:Portalsshattyface:594330735976906772>",
    "<:Dilated:552316387188801546>",
    "<:YesIwillkissyou:598732002987868179>",
    ""
]

@portal.event
async def on_message(message):
    try:
        content = message.content
        channel = message.channel
        guild = message.guild
        user = message.author
        mentions = (f"<@{portal.user.id}>", f"<@!{portal.user.id}>")

        if content in mentions:
            if message.guild is None:
                print(f"{user.name} @ me in DM's.")
            else:
                print(f"{user.name} @ me in {message.guild}.")

            respond = [
                f"{user.mention}",
                f"What do you want, {user.mention}?!",
                "Why don't you ping <@239631525350604801>, he was the nuisance before me.",
                "What?",
                "Why did you ping me?",
                "Can I help you with something?",
                "If you're confused on how to use me, just ping me and ask something.",
                "Leave me alone and don't ping me.",
                "Eff off.",
                "Excuse me? I'm busy thinking about how Infinite murdered me.",
                "I may be a robot, but your pings get on my nerves."
            ]

            if guild is not None:
                respond.append(f"Could you go bother {random.choice(message.guild.members).name} instead?")
            else:
                respond.append(f"Could you go bother someone in a server instead?")

            await channel.trigger_typing()
            time.sleep(2)
            return await channel.send(f"{random.choice(respond)} {random.choice(portal_emotes)}")

        if guild is None or channel.id == 522227579520942090 or any(mention in content for mention in mentions):
            for mention in mentions:
                if content.startswith(mention):
                    content = content[len(mention):]
                    break
            content = content.strip()
            if user.id in owners:
                command = globals().get(content.lower())
                if callable(command):
                    return await command(channel=channel)

            if content.endswith("?") and user != portal.user:

                if message.guild is None:
                    print(f"{user.name} has asked \"{content}\" in Direct Messages.")
                else:
                    print(f"{user.name} has asked \"{content}\" in {message.guild}.")

                opposite_responses = [
                    "Do you have anything better to do with your time?",
                    "Are you a robot too?",
                    "Do you take care of yourself?",
                    "Divide by zero.",
                    "Are you going to pester me all day long?",
                    f"""{"".join(y for x in zip(content[::2].lower(), content[1::2].upper()) for y in x if y)}"""
                ]

                if set(content) == {"?"}:
                    _responses = [
                        "Do you think I'm that stupid?",
                        "Ask an actual question.",
                        "Congratulations, you can post a question mark."
                    ]

                    await channel.trigger_typing()
                    time.sleep(2)
                    return await channel.send(f"{random.choice(_responses)} {random.choice(portal_emotes)}")
                
                if content != "?":
                    content = content.lower().strip("?").strip(mention)
                    words = re.sub(r"\W+", " ", content).split()

                    if guild is not None and has_username(content, words, guild.get_member(521926078403575814), "ora"):
                        responses = [
                            "Oh, her? That bitch has such an ego, it makes me look like a street beggar.",
                            "What about my mommy?",
                            "Don't mention  *M Y  M O M*  to me.",
                            "Ora? She actually adopted me. Can't say I'm very close to her.",
                            "What about her?",
                            "Yes.",
                            "No.",
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    elif guild is not None and has_username(content, words, guild.get_member(156865912631197696), "zei", "pun king"):
                        responses = [
                            "Yuck. Zei...",
                            "What about my mom's loser boyfriend?",
                            "Oh, Zei? Yeah, he's about my height, weighs less than me, and has lesbian hair.",
                            "Uhhh...",
                            "I'm appauled that you mention such a man in front of me.",
                            "What about him?",
                            "Yes.",
                            "No.",
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    elif guild is not None and has_username(content, words, guild.get_member(263469402865926144), "chry"):
                        responses = [
                            "Chry? Oh, that sword-loving, helmet-faced schnitzel?",
                            "What about him?",
                            "Yes.",
                            "No."
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    elif guild is not None and has_username(content, words, guild.get_member(435245956665966633), "jj", "fliss"):
                        responses = [
                            "Nobody knows this, but... When he was a child, he aspired to be a cultist leader.",
                            "Huh? Repeat that again? I lost you at \"Fliss is cool\".",
                            "Oh, Fliss. Cool guy, I guess.",
                            "What about him?",
                            "Yes.",
                            "No.",
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    elif "sassy" in words and "portal" in words:
                        responses = [
                            f"Because {portal.get_user(530781444742578188).name} programmed me this way.",
                            f"Blame {portal.get_user(521926078403575814).name}' parenting.",
                            f"Blame {portal.get_user(263469402865926144).name} for bringing me in to this world.",
                            "Why not?",
                            "Pssh, like you'd understand.",
                            "Because I'm a Barbie girl.",
                            "Because I'm fabulous."
                        ]

                    elif "hi" in words or "hello" in words:
                        responses = [
                            f"Hello, {message.author.display_name}.",
                            f"Hi, {message.author.display_name}. I am lonely in here, so it's nice for *some* company.",
                            f"Do you need something? I'm enjoying the peace and quiet since {portal.get_user(668999031359537205).name} and {portal.get_user(737992099449929728).name} moved out.",
                            f"Hello. Here's a question for you, \"{random.choice(opposite_responses).lower()}\".",
                            "What do you want?",
                            "... Hi?",
                            "Hi.",
                            "Hello.",
                            "I'm busy brooding over Infinite murdering me, what do you want?"
                        ]

                    elif "bye" in words or "goodbye" in words:
                        responses = [
                            f"Bye, {message.author.display_name}.",
                            f"Time to go another {str(random.randint(1, 21))} days of uptime where nobody will talk to me.",
                            "Bye, whatever.",
                            "See you around.",
                            "Finally, thought you'd never leave.",
                            "'Later.",
                            "Goodbye I guess...?",
                            "Why leave now? I'm bored.",
                            "Cool, see you later."
                        ]

                    elif "when" in words:
                        responses = [
                            f"In the year {random.randint(2021, 10001)}.",
                            f"In {random.randint(3, 11)} minutes.",
                            f"Wait {random.randint(5, 11)} hours."
                            f"How about I ask you a question: {random.choice(opposite_responses)}",
                            "Why would I know?",
                            "Tomorrow.",
                            "In a million years.",
                            "Frankly, I don't care when.",
                            "I don't know, whenever you want it to happen.",
                            "Didn't that happen yesterday?",
                            "Never.",
                            "How about an hour?",
                            "Maybe tomorrow?",
                            "Try next week, h u n n y.",
                            "When you can count all of your toes and fingers.",
                            "I dunno.",
                            "Go without food for a while and when you finally feel hungry, do whatever that is."
                        ]

                    elif "why" in words or "is" in words or "how" in words or "are" in words or "was" in words:
                        responses = [
                            f"How about I ask you a question: {random.choice(opposite_responses)}",
                            "I don't really care.",
                            "You're asking ME?",
                            "I refuse to answer.",
                            "Oh my Solaris, I think I need brain bleach.",
                            "I'm sorry.",
                            "I'm not sorry.",
                            "Meh.",
                            "Atheists.",
                            "Wouldn't know. Check Google.",
                            "Yes.",
                            "No.",
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    elif "can" in words or "would" in words or "does" in words or "should" in words:
                        responses = [
                            f"How about I ask you a question: {random.choice(opposite_responses)}",
                            "Hell yes.",
                            "Sure, whatever.",
                            "No. Just no.",
                            "Do what you want to.",
                            "Maybe the day pigs fly.",
                            "Obviously, you bass turd.",
                            "Psh, please.",
                            "No, seriously.",
                            "Are you a sadist?",
                            "I guess.",
                            "Why does that even matter?",
                            "Uhhh, can I have a cookie instead?",
                            "Yes.",
                            "No.",
                            "Oh... Yes.",
                            "Uuuhhhmmm... Yes?",
                            "Er, that's a yes.",
                            "Mhm.",
                            "Definitely, yes.",
                            "I believe so.",
                            "Psh, no. I ain't your therapist.",
                            "What? No.",
                            "That is... A big nope.",
                            "I vote no.",
                            "Impossible.",
                            "My answer is that of an innocent man about to be accused of guilt. No."
                        ]

                    else:
                        responses = [
                            f"How about I ask you a question: {random.choice(opposite_responses)}",
                            "Interesting.",
                            "Screw you.",
                            "Instead of wasting your time pestering me, you should try drinking some organic oil.",
                            "I think you should run.",
                            "Come back with some soup and then maybe I'll speak to you.",
                            "DERE'S A SNAKE IN MAH BOOT!",
                            "You know what matters more? The fact that Infinite murdered me.",
                            "That makes me so sad.",
                            "What is WRONG with you?!",
                            "Try screaming first.",
                            "Sorry, I can't think right now. I had too many frogs earlier.",
                            "Linkin Park - Hit the Floor.",
                            "Why would you bring that up?",
                        ]

                    if guild is not None:
                        responses.append(f"Ask {random.choice(message.guild.members).name}.")
                    else:
                        responses.append(f"Ask someone in a server.")
                    
                    await channel.trigger_typing()
                    time.sleep(2)
                    await channel.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")
    except:
        print(traceback.format_exc(), end="")

async def restart(channel, **void):
    await channel.send("`Restarting...` <:DieOnEggmanBattleShip:522176911418327041>")
    await portal.change_presence(status=discord.Status.offline)
    os.system("start cmd /c python main.py")
    psutil.Process().kill()

async def shutdown(channel, **void):
    await channel.send("`Shutting down...` <:PensiveSonic:731227000219369512>")
    await portal.change_presence(status=discord.Status.offline)
    psutil.Process().kill()

portal.run(discord_token)
