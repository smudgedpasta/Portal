#!/usr/bin/python3

import discord
import json
import random
import os
import psutil

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

        if content.endswith("?"):

            opposite_responses = [
                "Do you have anything better to do with your time?",
                "Are you a robot too?",
                "Do you take care of yourself?",
                "Divide by zero.",
                "Are you going to pester me all day long?",
                f"""{"".join(y for x in zip(content[::2].lower(), content[1::2].upper()) for y in x if y)}"""
            ]

            responses = [
                f"How about I ask you a question: {random.choice(opposite_responses)}",
                "Hell yes.",
                "Sure, whatever.",
                "No. Just no.",
                "I don't really care.",
                "Do what you want to.",
                "Interesting.",
                "Screw you.",
                "Meh.",
                "Instead of wasting your time pestering me, you should try drinking some organic oil.",
                "Maybe the day pigs fly.",
                "I think you should run.",
                "Obviously, you bass turd.",
                "You're asking ME?",
                "I refuse to answer.",
                "Psh, please.",
                "Come back with some soup and then maybe I'll speak to you.",
                "DERE'S A SNAKE IN MAH BOOT!",
                "You know what matters more? The fact that Infinite murdered me.",
                "That makes me so sad.",
                "What is WRONG with you?!",
                "Oh my Solaris, I think I need brain bleach.",
                "Try screaming first.",
                "Sorry, I can't think right now. I had too many frogs earlier.",
                "Are you a sadist?",
                "No, seriously.",
                "Linkin Park - Hit the Floor.",
                "I'm sorry.",
                "I'm not sorry.",
                "I guess."
            ]

            portal_emotes = [
                "<:Sassy:522184015109947392>",
                "<:Portalsshattyface:594330735976906772>",
                "<:Dilated:552316387188801546>",
                "<:YesIwillkissyou:598732002987868179>",
                ""
            ]

            await channel.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")

async def restart(channel, **void):
    await channel.send("`Restarting...` <:DieOnEggmanBattleShip:522176911418327041>")
    os.system("start cmd /k python main.py")
    psutil.Process().kill()

async def shutdown(channel, **void):
    await channel.send("`Shutting down...` <:PensiveSonic:731227000219369512>")
    psutil.Process().kill()

portal.run(discord_token)