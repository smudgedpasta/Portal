import discord
from discord.ext import commands
import random

class _8ball(commands.Cog):
    def __init__(self, portal):
        self.portal = portal


    @commands.command(aliases=["8ball", "ask", "question"], question=None)
    async def AskPortal(self, ctx, question):

        responses = [
            "Hell yes.",
            "Sure, whatever.",
            "No. Just no.",
            "I don't really care.",
            "Do what you want to.",
            "Interesting.",
            "Screw you.",
            "Meh."
        ]

        portal_emotes = [
            "<:Sassy:522184015109947392>",
            "<:Portalsshattyface:594330735976906772>",
            "<:Dilated:552316387188801546>",
            "<:YesIwillkissyou:598732002987868179>",
            ""
        ]

        for i in ("~~", "***", "**", "*", "||", "__", "```", "'"):
            if question.startswith(i) and question.endswith(i):
                await ctx.send(f"{i}{random.choice(responses)}{i}")
                return

        await ctx.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")


def setup(portal):
    portal.add_cog(_8ball(portal))