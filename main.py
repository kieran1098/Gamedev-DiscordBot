import os
import io
import traceback
import sys
import subprocess
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
import pyflakes.api
import pyflakes.checker
from pyflakes import reporter as pyflakes_reporter
from pyflakes import messages as pyflakes_messages
import ast

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO


# Set the bot prefix
bot_prefix = ">>"
command_prefix = "/"


# Define intents
intents = discord.Intents.all()
intents.messages = True
intents.members = True  # Enable the GUILD_MEMBERS intent
intents.guilds = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix=bot_prefix,
                   intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("Bot is ready!")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')

    # Getting the number of servers the bot is in
    guild_count = len(bot.guilds)

    # Updating the bot's activity including the number of servers
    activity = discord.Game(name=f">>help | In {guild_count} servers")
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:.2f} seconds.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all the required arguments for the command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use `>>help` to see the available commands.")
    else:
        await ctx.send("An error occurred while processing the command.")


@bot.command(name='show_servers', aliases=['servers'])
async def show_servers(ctx):
    embed = discord.Embed(title="Servers Bot is in",
                          color=discord.Color.blurple())

    for guild in bot.guilds:
        invite = await guild.text_channels[0].create_invite(max_age=300, max_uses=1, unique=True)
        embed.add_field(name=guild.name, value=invite.url, inline=False)

    await ctx.send(embed=embed)


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing...")
    await bot.tree.sync()


@bot.hybrid_command()
async def pingcheck(ctx):
    latency = bot.latency * 1000  # Convert latency to milliseconds

    embed = discord.Embed(
        title="Pong!",
        description=f"Latency: {latency:.2f}ms",
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)
    await bot.tree.sync()

    @commands.command()
    async def announce_all(self, ctx, *, message):
        # Check if the command invoker is the bot owner
        if ctx.author.id != YOUR_BOT_OWNER_ID:
            return await ctx.send("You do not have permission to use this command.")

        # Create an embed for the announcement message
        embed = discord.Embed(title="Announcement",
                              description=message, color=discord.Color.green())
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Announced in {ctx.guild.name}")

        # Iterate over all guilds the bot is connected to
        for guild in self.bot.guilds:
            # Check if the bot has permissions to send messages in the guild
            if guild.me.guild_permissions.send_messages:
                # Get the announcements channel or a random channel
                channel = discord.utils.get(
                    guild.text_channels, name="announcements")
                if channel is None:
                    # If announcements channel is not found, select a random text channel
                    channel = random.choice(guild.text_channels)

                # Send the embed to the channel
                try:
                    await channel.send(embed=embed)
                except discord.Forbidden:
                    continue  # Skip if the bot doesn't have permissions to send messages in the channel

        await ctx.send("Announcement sent to all servers.")


bot.run("INSERT TOKEN HERE")
