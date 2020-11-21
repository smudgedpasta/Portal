#!/usr/bin/python3

import discord
import json
import random
import os
import psutil
import traceback

portal = discord.Client()

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

            if content.endswith("?"):

                opposite_responses = [
                    "Do you have anything better to do with your time?",
                    "Are you a robot too?",
                    "Do you take care of yourself?",
                    "Divide by zero.",
                    "Are you going to pester me all day long?",
                    f"""{"".join(y for x in zip(content[::2].lower(), content[1::2].upper()) for y in x if y)}"""
                ]

                if "why" in content or "is" in content or "how" in content:
                    responses = [
                        "I don't really care.",
                        "You're asking ME?",
                        "I refuse to answer.",
                        "Oh my Solaris, I think I need brain bleach.",
                        "I'm sorry.",
                        "I'm not sorry.",
                        "Meh."
                    ]

                elif "can" in content or "would" in content or "does":
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
                        "I guess."
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
                        "Linkin Park - Hit the Floor."
                    ]

                portal_emotes = [
                    "<:Sassy:522184015109947392>",
                    "<:Portalsshattyface:594330735976906772>",
                    "<:Dilated:552316387188801546>",
                    "<:YesIwillkissyou:598732002987868179>",
                    ""
                ]

                await channel.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")
                print(f"{user} has asked \"{content}\" in {user.guild}.")
    except:
        print(traceback.format_exc(), end="")

async def restart(channel, **void):
    await channel.send("`Restarting...` <:DieOnEggmanBattleShip:522176911418327041>")
    os.system("start cmd /c python main.py")
    psutil.Process().kill()

async def shutdown(channel, **void):
    await channel.send("`Shutting down...` <:PensiveSonic:731227000219369512>")
    psutil.Process().kill()

portal.run(discord_token)