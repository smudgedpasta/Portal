import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, portal):
        self.portal = portal


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour(3214259))
        embed.set_author(name=self.portal.user.name, url="https://www.deviantart.com/ora-allagis", icon_url=self.portal.user.avatar_url_as(format="png", size=4096))
        embed.description = "```fix\n[𝐇𝐄𝐋𝐏 𝐋𝐈𝐒𝐓... 𝐀𝐥𝐥 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐬𝐭𝐚𝐫𝐭 𝐰𝐢𝐭𝐡 𝐩~]```"
        embed.set_footer(icon_url=self.portal.get_user(530781444742578188).avatar_url_as(format="png", size=4096), text="If you have any questions, feature requests or bug reports, tell smudgedpasta.")

        embed.add_field(name="help", value="```ini\n[You've found this command already, bass turd.]```")
        embed.add_field(name="AskPortal, 8ball, ask", value="```ini\n[Ask me anything, I'll answer randomly...]```")
        embed.add_field(name="\u200b", value="\u200b")
        embed.add_field(name="reload", value="```asciidoc\n[Refreshes a mentioned cog, aka command.]```")
        embed.add_field(name="unload", value="```asciidoc\n[Disables a command from use.]```")
        embed.add_field(name="load", value="```asciidoc\n[Grants access back to unloaded command.]```")
        embed.add_field(name="restart", value="```asciidoc\n[Restarts all of my code.]```")
        embed.add_field(name="shutdown", value="```asciidoc\n[Logs me out, shuts me down.]```")
        embed.add_field(name="\u200b", value="\u200b")

        await ctx.send(embed=embed)


def setup(portal):
    portal.add_cog(help(portal))