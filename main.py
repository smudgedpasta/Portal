#!/usr/bin/python3

import discord
import json
import asyncio
import random
import os
import psutil
import traceback
import datetime

intents = discord.Intents.default()
intents.members = True
portal = discord.Client(intents=intents)

owners = [530781444742578188, 521926078403575814, 201548633244565504]
#            smudgedpasta         Ora-Allagis            Txin

discord_token = None
with open ("auth.json", "r") as f:
    data = json.load(f)
    discord_token = data["token"]

@portal.event
async def on_ready():
    await portal.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="God and consuming frogs. 🐸"))
    print("Successfully loaded.")

@portal.event
async def on_message(message):
    try:
        content = message.content
        channel = message.channel
        guild = message.guild
        user = message.author
        mentions = (f"<@{portal.user.id}>", f"<@!{portal.user.id}>")
        if guild is None or channel.id == 522227579520942090 or any(mention in content for mention in mentions):

            for mention in mentions:
                if content.startswith(mention):
                    content = content[len(mention):]
                    break
            content = content.strip()
            if user.id in owners:
                command = globals().get(content.casefold())
                if callable(command):
                    return await command(channel=channel)

            if getattr(message.channel, "guild", None) is None and user != portal.user:
                print(f"{message.author} has asked \"{content}\" in Direct Messages.")
            
            elif getattr(message.channel, "guild", None) is not None and user != portal.user:
                print(f"{user} has asked \"{content}\" in {user.guild}.")

            if content.endswith("?") and user != portal.user:

                opposite_responses = [
                    "Do you have anything better to do with your time?",
                    "Are you a robot too?",
                    "Do you take care of yourself?",
                    "Divide by zero.",
                    "Are you going to pester me all day long?",
                    f"""{"".join(y for x in zip(content[::2].lower(), content[1::2].upper()) for y in x if y)}"""
                ]
                
                content = content.lower().strip("?").split()

                if "ora" in content or portal.get_user(521926078403575814).name.casefold() in content or portal.get_user(521926078403575814).display_name.casefold() in content:
                    responses = [
                        "Oh, her? That bitch has such an ego, it makes me look like a street beggar.",
                        "What about my mommy?",
                        "Don't mention  *M Y  M O M*  to me.",
                        "Ora? She actually adopted me. Can't say I'm very close to her.",
                        "What about her?",
                        "Yes.",
                        "No."
                    ]

                elif "zei" in content or "pun king" in content or portal.get_user(156865912631197696).name.casefold() in content or portal.get_user(156865912631197696).display_name.casefold() in content:
                    responses = [
                        "Yuck. Zei...",
                        "What about my mom's loser boyfriend?",
                        "Oh, Zei? Yeah, he's about my height, weighs less than me, and has lesbian hair.",
                        "Uhhh...",
                        "I'm appauled that you mention such a man in front of me.",
                        "What about him?",
                        "Yes.",
                        "No."
                    ]

                elif "chry" in content or portal.get_user(263469402865926144).name.casefold() in content or portal.get_user(263469402865926144).display_name.casefold() in content:
                    responses = [
                        "Chry? Oh, that sword-loving, helmet-faced schnitzel?",
                        "What about him?",
                        "Yes.",
                        "No."
                    ]

                elif "jj" in content or "fliss" in content or portal.get_user(435245956665966633).name.casefold() in content or portal.get_user(435245956665966633).display_name.casefold() in content:
                    responses = [
                        "Nobody knows this, but... When he was a child, he aspired to be a cultist leader.",
                        "Huh? Repeat that again? I lost you at \"Fliss is cool\".",
                        "Oh, Fliss. Cool guy, I guess.",
                        "What about him?",
                        "Yes.",
                        "No."
                    ]

                elif "why" in content or "is" in content or "how" in content:
                    responses = [
                        "I don't really care.",
                        "You're asking ME?",
                        "I refuse to answer.",
                        "Oh my Solaris, I think I need brain bleach.",
                        "I'm sorry.",
                        "I'm not sorry.",
                        "Meh.",
                        "Athiests.",
                        "Wouldn't know. Check Google."
                    ]

                elif "can" in content or "would" in content or "does" in content:
                    responses = [
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
                        "Uhhh, can I have a cookie instead?"
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
                        "Why would you bring that up?"
                    ]

                portal_emotes = [
                    "<:Sassy:522184015109947392>",
                    "<:Portalsshattyface:594330735976906772>",
                    "<:Dilated:552316387188801546>",
                    "<:YesIwillkissyou:598732002987868179>",
                    ""
                ]

                await channel.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")
    except:
        print(traceback.format_exc(), end="")

async def code_check():
    await portal.wait_until_ready()
    while not portal.is_closed():
        try:
            print(f"Code is running at {datetime.datetime.utcnow()} GMT.")
        except Exception as e:
            print(e)
        await asyncio.sleep(300)
portal.loop.create_task(code_check())

async def restart(channel, **void):
    await channel.send("`Restarting...` <:DieOnEggmanBattleShip:522176911418327041>")
    os.system("start cmd /c python main.py")
    psutil.Process().kill()

async def shutdown(channel, **void):
    await channel.send("`Shutting down...` <:PensiveSonic:731227000219369512>")
    psutil.Process().kill()

portal.run(discord_token)