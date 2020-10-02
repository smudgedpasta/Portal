import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, portal):
        self.portal = portal


def setup(portal):
    portal.add_cog(help(portal))