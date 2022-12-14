import os
from datetime import datetime

import discord
from discord.ext.commands import Cog, command


class BotInfo(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        self.prefix = '!'
        if 'BOT_PREFIX' in os.environ:
            self.prefix = os.environ['BOT_PREFIX']

    @command()
    async def info(self, ctx):
        """Sends a help message"""
        info = await self.bot.application_info()
        embed = discord.Embed(
            title='Plant ID Bot Info',
            description=f'{info.description}',
            colour=0x41c03f
        ).add_field(
            name=f'`{self.prefix}info`',
            value='Shows this message',
            inline=True
        ).add_field(
            name=f'`{self.prefix}idhelp`',
            value='Gives more detailed help on the plant ID bot',
            inline=True 
        ).add_field(
            name=f'`{self.prefix}stats`',
            value='Bot stats',
            inline=True
        ).add_field(
            name=f'`{self.prefix}invite`',
            value='Bot invite link',
            inline=True
        ).add_field(
            name=f'`{self.prefix}source`',
            value='Links to the bot\'s code repo',
            inline=True
        ).set_footer(text=f'Made by {info.owner}')
        await ctx.send(embed=embed)

    @command()
    async def stats(self, ctx):
        info = await self.bot.application_info()
        embed = discord.Embed(
            title=f'{info.name}',
            description="Stats etc.",
            colour=0x1aaae5,
        ).add_field(
            name='Server Count',
            value=len(self.bot.guilds),
            inline=True
        ).add_field(
            name='User Count',
            value=len(self.bot.users),
            inline=True
        ).add_field(
            name='Uptime',
            value=f'{datetime.now() - self.start_time}',
            inline=True
        ).add_field(
            name='Latency',
            value=f'{round(self.bot.latency * 1000, 2)}ms',
            inline=True
        ).set_footer(text=f'Made by {info.owner}')
        await ctx.send(embed=embed)


    # Sends a bot invite link
    @command()
    async def invite(self, ctx):
        url = 'https://discord.com/api/oauth2/authorize?client_id=1047075947242852362&permissions=8&scope=bot'
        embed = discord.Embed(
            title=f'Invite the bot to your server:',
            description=f'[Click here]({url})',
            colour=0x1aaae5
        )
        await ctx.send(embed=embed)

    # list servers that the bot has been invited to
    @command()
    async def servers(self, ctx):
        servers = list(self.bot.guilds)
        embed = discord.Embed(
            title=f'Connected on {str(len(servers))} servers:',
            description='\n'.join(guild.name for guild in self.bot.guilds),
            colour=0x1aaae5
        )
        await ctx.send(embed=embed)
