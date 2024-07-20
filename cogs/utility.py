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


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def coinflip(self, ctx):
        # Generate a random number (0 or 1)
        result = random.choice(["Heads", "Tails"])

        # Create an embed to display the result
        embed = discord.Embed(
            title="Coin Flip",
            description=f"The coin landed on: **{result}**",
            color=discord.Color.gold()
        )

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command()
    async def poll(self, ctx, question, *options):
        if len(options) < 2 or len(options) > 10:
            await ctx.send("Please provide between 2 and 10 options for the poll.")
            return

        if len(question) > 256:
            await ctx.send("The question for the poll cannot exceed 256 characters.")
            return

        if len(options) > 20:
            await ctx.send("You can only have up to 20 options for the poll.")
            return

        emojis = [
            "\N{DIGIT ONE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT TWO}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT THREE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT FOUR}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT FIVE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT SIX}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT SEVEN}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT EIGHT}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{DIGIT NINE}\N{VARIATION SELECTOR-16}\N{COMBINING ENCLOSING KEYCAP}",
            "\N{KEYCAP TEN}",
        ]

        poll_embed = discord.Embed(
            title=f"Poll: {question}", color=discord.Color.blue())

        for i, option in enumerate(options):
            poll_embed.add_field(name=f"{emojis[i]} {
                                 option}", value="\u200b", inline=False)

        poll_message = await ctx.send(embed=poll_embed)

        for i in range(len(options)):
            await poll_message.add_reaction(emojis[i])

    @bot.command()
    async def ping(self, ctx):
        latency = bot.latency * 1000  # Convert latency to milliseconds

        embed = discord.Embed(
            title="Pong!",
            description=f"Latency: {latency:.2f}ms",
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(utility(bot))
