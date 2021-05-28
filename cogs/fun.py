import discord
from discord.ext import commands
import psutil
import config
import bot
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        em = discord.Embed(title = left + right)
        await ctx.send(embed = em)

    
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        if "@everyone" in choices:
            em = discord.Embed(title = "Nice try, sadly that won't work here.")
            await ctx.send(embed = em)
        else:
            if "@here" in choices:
                em = discord.Embed(title = "Nice try, sadly that won't work here.")
                await ctx.send(embed = em)
            else:
                em = discord.Embed(title = random.choice(choices))
                await ctx.send(embed = em)
    
    @commands.command(description='#emotes')
    async def emote(self, ctx, emote : discord.Emoji = None):
        """emote command"""
        if emote == None:
            em = discord.Embed(title="No emote given", description = f"Please use `{config.prefix}emote <emote>`.")
            await ctx.send(embed=em)
            return
        else:
            em = discord.Embed(timestamp=emote.created_at)
            em.set_author(name=emote.name, icon_url=emote.url)
            em.set_thumbnail(url=emote.url)
            em.set_footer(text="Created on")
            em.add_field(name="ID", value=emote.id)
            em.add_field(name="Usage", value=f"`{emote}`")
            em.add_field(name="URL", value=f"<{emote.url}>")
            await ctx.send(embed=em)
            return
        '''
        else:
            try:
                emote = discord.utils(self.bot.get_all_emojis())
                emote = discord.utils.get(self.bot.Emoji, name=emote)
            except Exception as e:
                await ctx.send(str(e))
                return
        '''

    @commands.command()
    async def f(self, ctx, *, message2):
        em = discord.Embed(title = "F in the chat to: " + message2)
        msg = await ctx.send(embed = em)
        await msg.add_reaction('🇫')


        
def setup(bot):
    bot.add_cog(Fun(bot))
