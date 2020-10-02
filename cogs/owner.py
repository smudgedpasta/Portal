import discord
from discord.ext import commands
import os
import json
import psutil

owners = [
    530781444742578188, # smudgedpasta
    521926078403575814 # Ora_Allagis
]

def is_owner(ctx):
    return ctx.message.author.id in owners

class owner(commands.Cog):
    def __init__(self, portal):
        self.portal = portal


    @commands.command()
    @commands.check(is_owner)
    async def restart(self, ctx):
        await ctx.send("Restarting... <:DieOnEggmanBattleShip:522176911418327041>")
        for vc in self.portal.voice_clients:
            await vc.disconnect(force=True)
        os.system("start cmd /k python main.py")
        psutil.Process().kill()


    @commands.command()
    @commands.check(is_owner)
    async def shutdown(self, ctx):
        await ctx.send("Shutting down... <:PensiveSonic:731227000219369512> ")
        for vc in self.portal.voice_clients:
            await vc.disconnect(force=True)
        await ctx.bot.logout()


def setup(portal):
    portal.add_cog(owner(portal))