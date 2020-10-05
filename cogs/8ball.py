import discord
from discord.ext import commands
import random

class _8ball(commands.Cog):
    def __init__(self, portal):
        self.portal = portal


    @commands.command(aliases=["8ball", "ask", "question"], question=None)
    async def AskPortal(self, ctx, question):

        opposite_responses = [
            "Do you have anything better to do with your time?"
        ]

        responses = [
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
            "I guess.",
            f"How about I ask you a question: {random.choice(opposite_responses)}"
        ]

        portal_emotes = [
            "<:Sassy:522184015109947392>",
            "<:Portalsshattyface:594330735976906772>",
            "<:Dilated:552316387188801546>",
            "<:YesIwillkissyou:598732002987868179>",
            "\u200b"
        ]

        for i in ("~~", "***", "**", "*", "||", "__", "```", "'"):
            if question.startswith(i) and question.endswith(i):
                await ctx.send(f"{i}{random.choice(responses)}{i}")
                return

        await ctx.send(f"{random.choice(responses)} {random.choice(portal_emotes)}")


def setup(portal):
    portal.add_cog(_8ball(portal))