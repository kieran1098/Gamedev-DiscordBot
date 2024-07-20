import os
import sys
import discord
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
from discord import Interaction
from discord import interactions
import interactions
import logging
import sqlite3


# Set the bot prefix
bot_prefix = "??"
command_prefix = "/"


# Define intents
intents = discord.Intents.all()
intents.messages = True
intents.members = True  # Enable the GUILD_MEMBERS intent
intents.guilds = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix=bot_prefix,
                   intents=intents, help_command=None)


class support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='discord')
    async def discordlink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="Discord server",
                              description="[Click here to join the server!](https://discord.gg/ttpmZCPNwa)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command(name='patreon')
    async def patreonlink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="patreon link",
                              description="[Click here to support my work!](https://patreon.com/jezzuz1098)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)


    @bot.command(name='bump')
    async def bumplink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="discord.me link",
                              description="[Click here to support my work!](https://discord.me/gamedevlibrary)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(support(bot))
