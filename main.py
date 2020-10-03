#!/usr/bin/python3

import discord
from discord.ext import commands
import os
import json
import random
import traceback

discord_token = None
with open("auth.json", "r") as f:
    data = json.load(f)
    discord_token = data["token"]

prefix = "p~"

portal = commands.Bot(command_prefix=(prefix))

portal.remove_command("help")

owners = [
    530781444742578188, # smudgedpasta
    521926078403575814 # Ora_Allagis
]

def is_owner(ctx):
    return ctx.message.author.id in owners


@portal.event
async def on_command_error(ctx, error):
    responses = [
        "What is that meant to mean?",
        "Either that command is disabled, or you're trying to make me do something doesn't exist.",
        f"Quit wasting my time, {ctx.author.display_name}, and run a real command!",
        "<:Dilated:552316387188801546> That doesn't exist.",
        "That doesn't exist. If you're confused at my functionality, ask <@530781444742578188>."
    ]

    if isinstance(error, commands.CommandNotFound):
        await ctx.send(random.choice(responses))
    try:
        raise error
    except:
        print(traceback.format_exc())


@portal.event
async def on_message(message):
    ctx = await portal.get_context(message)

    responses = [
        f"What do you want, {message.author.mention}?",
        "My prefix is `" + prefix + "` by the way... <:Sassy:522184015109947392>",
        f"Can you not ping me, {message.author.mention}?",
        f"Go bug <@239631525350604801>..."
    ]

    if portal.user in message.mentions:
        await ctx.send(random.choice(responses))

    await portal.invoke(ctx)

    if ctx.command is not None:
        if getattr(message.author, "guild", None) is None:
            print(f"{message.author} has run the following command: {message.content} in Direct Messages")
        else:
            print(f"{message.author} has run the following command: {message.content} in {message.author.guild}")

    elif getattr(message.channel, "guild", None) is None and message.author != portal.user:
        if ctx.command is None:

            embed = discord.Embed(colour=discord.Colour(3214259), timestamp=ctx.message.created_at)
            embed.set_author(name=portal.user.name, url="https://www.deviantart.com/ora-allagis", icon_url=portal.user.avatar_url_as(format="png", size=4096))
            embed.description = f"***I am getting bugged in DM's by {message.author.name}...***\n```fix\n{message.content}```"
            embed.set_footer(text=f"{message.author} | {ctx.author.id}")

            await portal.get_channel(522227579520942090).send(embed=embed)


@portal.event
async def on_ready():
    await portal.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="God and consuming frogs. 🐸"))
    print("Successfully loaded.")


@portal.event
async def on_guild_join(guild):
    target_channel = None

    embed = discord.Embed(colour=discord.Colour(3214259))
    embed.description = f"{portal.user.name}'s the name, invading's my game. <:Portalsshattyface:594330735976906772>"
    embed.set_author(name=portal.user.name, url="https://www.deviantart.com/ora-allagis", icon_url=portal.user.avatar_url_as(format="png", size=4096))

    for channel in ["general"]:
        target_channel = discord.utils.get(guild.text_channels, name=channel)
        if target_channel and target_channel.permissions_for(guild.me).send_messages:
            break

    if not target_channel:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                target_channel = channel
                break
    if target_channel:
        await target_channel.send(embed=embed)


@portal.command()
@commands.check(is_owner)
async def load(ctx, extension=None):
    if extension is None:
        await ctx.send("No extension specified.")
        return
    portal.load_extension(f"cogs.{extension}")
    await ctx.send(prefix + f"{extension} can be used again.")

@portal.command()
@commands.check(is_owner)
async def unload(ctx, extension=None):
    if extension is None:
        await ctx.send("No extension specified.")
        return
    portal.unload_extension(f"cogs.{extension}")
    await ctx.send(prefix + f"{extension} is temporarily disabled.")

@portal.command()
@commands.check(is_owner)
async def reload(ctx, extension=None):
    if extension is None:
        await ctx.send("No extension specified")
        return
    portal.unload_extension(f"cogs.{extension}")
    portal.load_extension(f"cogs.{extension}")
    await ctx.send(prefix + f"{extension} has been refreshed.")


for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            portal.load_extension(f"cogs.{filename[:-3]}")

portal.run(discord_token)